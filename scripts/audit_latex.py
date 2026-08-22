#!/usr/bin/env python3
"""Audit a LaTeX translation project for common structural defects."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


EXCLUDED_DIRS = {
    ".git",
    ".svn",
    "_build",
    "build",
    "dist",
    "node_modules",
    "out",
}

COMMAND_PATTERNS = {
    "label": re.compile(r"\\label\s*\{([^{}]+)\}"),
    "reference": re.compile(
        r"\\(?:ref|eqref|pageref|autoref|cref|Cref|vref)\*?\s*\{([^{}]+)\}"
    ),
    "citation": re.compile(
        r"\\(?:cite|citep|citet|parencite|textcite|autocite|footcite)"
        r"\*?(?:\[[^\]]*\]){0,2}\s*\{([^{}]+)\}"
    ),
    "bibitem": re.compile(r"\\bibitem(?:\[[^\]]*\])?\s*\{([^{}]+)\}"),
    "bibliography": re.compile(r"\\bibliography\s*\{([^{}]+)\}"),
    "addbibresource": re.compile(r"\\addbibresource(?:\[[^\]]*\])?\s*\{([^{}]+)\}"),
    "includegraphics": re.compile(
        r"\\includegraphics(?:\[[^\]]*\])?\s*\{([^{}]+)\}"
    ),
}

BIB_ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE)
TODO_RE = re.compile(r"\b(?:TODO|FIXME|XXX)\b|待译|待确认|待校", re.IGNORECASE)
HARDCODED_REFERENCE_RE = re.compile(
    r"(?:定理|引理|命题|推论|定义|公式|方程|式|图|表|章节?|附录)"
    r"\s*[~ ]*(?:第\s*)?\(?\d+(?:\.\d+){0,3}\)?"
)
LOG_PATTERNS = (
    ("error", re.compile(r"^! (?:LaTeX|Package|Class)? ?Error", re.IGNORECASE)),
    ("error", re.compile(r"Undefined control sequence", re.IGNORECASE)),
    ("error", re.compile(r"Emergency stop", re.IGNORECASE)),
    ("error", re.compile(r"Fatal error", re.IGNORECASE)),
    ("warning", re.compile(r"undefined references?", re.IGNORECASE)),
    ("warning", re.compile(r"Citation .+ undefined", re.IGNORECASE)),
    ("warning", re.compile(r"multiply defined", re.IGNORECASE)),
    ("warning", re.compile(r"Rerun to get cross-references right", re.IGNORECASE)),
    ("warning", re.compile(r"Overfull \\\\hbox", re.IGNORECASE)),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit TeX sources, bibliography keys, assets, and LaTeX logs."
    )
    parser.add_argument("path", type=Path, help="A .tex file or project directory")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return a nonzero exit status when warnings are found",
    )
    return parser.parse_args()


def is_excluded(path: Path) -> bool:
    return any(part.lower() in EXCLUDED_DIRS for part in path.parts)


def collect_files(root: Path, suffix: str) -> list[Path]:
    if root.is_file():
        return [root] if root.suffix.lower() == suffix else []
    return sorted(
        path
        for path in root.rglob(f"*{suffix}")
        if path.is_file() and not is_excluded(path.relative_to(root))
    )


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig", errors="replace")


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def split_keys(value: str) -> list[str]:
    return [key.strip() for key in value.split(",") if key.strip()]


def resolve_asset(project_root: Path, tex_file: Path, target: str) -> bool:
    asset = Path(target)
    bases = (tex_file.parent, project_root)
    extensions = ("", ".pdf", ".png", ".jpg", ".jpeg", ".eps", ".svg")
    for base in bases:
        for extension in extensions:
            candidate = base / Path(f"{asset}{extension}")
            if candidate.is_file():
                return True
    return False


def resolve_bib(project_root: Path, tex_file: Path, target: str) -> list[Path]:
    result: list[Path] = []
    for key in split_keys(target):
        candidate = Path(key)
        if candidate.suffix.lower() != ".bib":
            candidate = candidate.with_suffix(".bib")
        for base in (tex_file.parent, project_root):
            resolved = base / candidate
            if resolved.is_file() and resolved not in result:
                result.append(resolved)
    return result


def audit(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not root.exists():
        return [f"Path does not exist: {root}"], warnings

    project_root = root if root.is_dir() else root.parent
    tex_files = collect_files(root, ".tex")
    if not tex_files:
        return [f"No TeX files found under: {root}"], warnings

    label_locations: dict[str, list[str]] = {}
    reference_locations: dict[str, list[str]] = {}
    citation_locations: dict[str, list[str]] = {}
    bibliography_keys: set[str] = set()
    bibliography_files: set[Path] = set(collect_files(project_root, ".bib"))

    for tex_file in tex_files:
        text = read_text(tex_file)
        display = tex_file.relative_to(project_root)

        for name, pattern in COMMAND_PATTERNS.items():
            for match in pattern.finditer(text):
                value = match.group(1).strip()
                location = f"{display}:{line_number(text, match.start())}"
                if name == "label":
                    label_locations.setdefault(value, []).append(location)
                elif name == "reference":
                    for key in split_keys(value):
                        reference_locations.setdefault(key, []).append(location)
                elif name == "citation":
                    for key in split_keys(value):
                        citation_locations.setdefault(key, []).append(location)
                elif name == "bibitem":
                    bibliography_keys.add(value)
                elif name in {"bibliography", "addbibresource"}:
                    bibliography_files.update(
                        resolve_bib(project_root, tex_file, value)
                    )
                elif name == "includegraphics":
                    if not resolve_asset(project_root, tex_file, value):
                        errors.append(f"{location}: missing graphic asset {value!r}")

        for match in TODO_RE.finditer(text):
            warnings.append(
                f"{display}:{line_number(text, match.start())}: unresolved marker "
                f"{match.group(0)!r}"
            )

        for match in HARDCODED_REFERENCE_RE.finditer(text):
            line_start = text.rfind("\n", 0, match.start()) + 1
            line_end = text.find("\n", match.end())
            if line_end == -1:
                line_end = len(text)
            line = text[line_start:line_end]
            if "\\ref{" not in line and "\\eqref{" not in line:
                warnings.append(
                    f"{display}:{line_number(text, match.start())}: possible "
                    f"hard-coded reference {match.group(0)!r}"
                )

    for bib_file in bibliography_files:
        for match in BIB_ENTRY_RE.finditer(read_text(bib_file)):
            bibliography_keys.add(match.group(1).strip())

    for label, locations in sorted(label_locations.items()):
        if len(locations) > 1:
            errors.append(f"duplicate label {label!r}: {', '.join(locations)}")

    for label, locations in sorted(reference_locations.items()):
        if label not in label_locations:
            errors.append(f"undefined reference {label!r}: {', '.join(locations)}")

    for key, locations in sorted(citation_locations.items()):
        if key not in bibliography_keys:
            errors.append(f"undefined citation {key!r}: {', '.join(locations)}")

    for log_file in collect_files(project_root, ".log"):
        text = read_text(log_file)
        display = log_file.relative_to(project_root)
        seen: Counter[tuple[str, str]] = Counter()
        for number, line in enumerate(text.splitlines(), start=1):
            for severity, pattern in LOG_PATTERNS:
                if pattern.search(line):
                    normalized = line.strip()
                    key = (severity, normalized)
                    seen[key] += 1
                    if seen[key] == 1:
                        message = f"{display}:{number}: {normalized}"
                        (errors if severity == "error" else warnings).append(message)

    return errors, warnings


def main() -> int:
    args = parse_args()
    errors, warnings = audit(args.path.resolve())

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")

    print(
        f"Audit complete: {len(errors)} error(s), {len(warnings)} warning(s)."
    )
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
