---
name: mathtranslations
description: Translate mathematical books, papers, notes, and existing LaTeX projects into rigorous Chinese LaTeX, or review and repair an existing mathematical translation. Use when source fidelity, mathematical correctness, terminology consistency, cross-references, citations, compilation, and PDF-level proofreading all matter. Do not use for ordinary non-mathematical translation.
---

# MathTranslations

Produce a Chinese mathematical translation that can be compiled, checked against
the source, and maintained as a real LaTeX project.

## Establish The Source Of Truth

1. Inventory the supplied PDF, TeX sources, bibliography, figures, fonts,
   templates, and any existing translated files before editing.
2. Treat the published source PDF as the authority for visible mathematical
   content and structure. Use source TeX to recover markup and reduce
   transcription errors, but do not follow it when it conflicts with the
   published PDF.
3. If the source PDF is unavailable, state that limitation and use the best
   available source without pretending that page-level comparison was done.
4. Never silently repair a suspected error in the source. Preserve it by
   default and clearly record the issue; apply a correction only when the user
   requests it or reliable evidence resolves it.

## Prepare The Project

- Preserve an existing project's document class, packages, file layout, labels,
  citation keys, macros, and build system unless a change is necessary.
- For a new project, consult the current MathTranslations guide before choosing
  a template or terminology source. Prefer the latest stable resources linked
  from <https://mathtranslations.org/guide/> over bundled stale copies.
- Build a small project glossary before translating substantial text. Reuse
  established Chinese mathematical terms; keep named objects and symbols
  stable across chapters.
- Read [references/workflow.md](references/workflow.md) when starting a new
  translation, importing a long source, or deciding how to stage the work.

## Translate

- Translate mathematical meaning rather than sentence shape. Use natural,
  concise Chinese while preserving definitions, hypotheses, quantifiers,
  logical dependencies, notation, equation content, theorem status, and the
  force of words such as "if", "only if", "unique", and "respectively".
- Keep math in LaTeX. Reuse the source's macros and environments when they are
  sound. Do not convert formulas into prose, screenshots, or Unicode lookalikes.
- Preserve theorem-like environments, equation structure, bibliography links,
  footnotes, figures, tables, and section hierarchy.
- Use `\label` plus the project's reference command for numbered objects. Do
  not hard-code theorem, equation, section, figure, table, or page numbers in
  translated prose.
- Do not invent missing proof steps, citations, definitions, labels, or
  references. Mark unresolved source ambiguity explicitly.
- Read [references/latex-quality.md](references/latex-quality.md) when editing
  TeX, resolving ambiguous notation, handling OCR, or repairing references.

## Verify

Verification is part of the translation, not an optional final polish.

1. Compile early and repeatedly with the project's actual build command.
2. Compare the generated PDF with the source PDF section by section.
3. Perform three separate passes: Chinese language and terminology;
   mathematics and structural fidelity; compilation and visual layout.
4. Run `scripts/audit_latex.py <project-or-tex-file>` for deterministic checks.
   Use `--strict` when warnings should fail CI.
5. Read [references/review-checklist.md](references/review-checklist.md) before
   declaring a chapter or project complete.

## Report The Result

Summarize:

- translated or reviewed scope;
- source files and authority used;
- build command and whether it succeeded;
- checks performed;
- unresolved ambiguities, suspected source errors, missing assets, or visual
  differences that still need human judgment.
