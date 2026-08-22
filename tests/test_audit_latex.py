from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "audit_latex.py"
SPEC = importlib.util.spec_from_file_location("audit_latex", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class AuditLatexTests(unittest.TestCase):
    def test_clean_project(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "main.tex").write_text(
                "\\label{thm:one}\n"
                "由定理~\\ref{thm:one}可知。\\cite{sample}\n"
                "\\includegraphics{plot}\n",
                encoding="utf-8",
            )
            (root / "refs.bib").write_text(
                "@book{sample, title={Example}}\n", encoding="utf-8"
            )
            (root / "plot.png").write_bytes(b"not-a-real-png")

            errors, warnings = AUDIT.audit(root)

            self.assertEqual([], errors)
            self.assertEqual([], warnings)

    def test_reports_structural_problems(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "main.tex").write_text(
                "\\label{dup}\\label{dup}\n"
                "\\ref{missing}\\cite{unknown}\n"
                "见定理 2.3。TODO\n"
                "\\includegraphics{absent}\n",
                encoding="utf-8",
            )

            errors, warnings = AUDIT.audit(root)

            self.assertTrue(any("duplicate label" in item for item in errors))
            self.assertTrue(any("undefined reference" in item for item in errors))
            self.assertTrue(any("undefined citation" in item for item in errors))
            self.assertTrue(any("missing graphic" in item for item in errors))
            self.assertTrue(any("hard-coded reference" in item for item in warnings))
            self.assertTrue(any("unresolved marker" in item for item in warnings))


if __name__ == "__main__":
    unittest.main()
