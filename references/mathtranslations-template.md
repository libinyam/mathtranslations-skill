# MathTranslations Template Profile

Read this reference when the user supplies or requests
`MathTranslations-Template.zip` or `MathTranslations-Template.tex`.

## Inspected Version

The profile below was derived from the locally supplied archive:

- archive: `MathTranslations-Template.c9598d4a8d56.zip`;
- inspected: 2026-08-22;
- SHA-256:
  `F74809A3B63F2AE1FD8C7554EF3B43D8AD8C7240969838DB928BD3CF529BF2EF`;
- contents: `MathTranslations-Template.tex`,
  `MathTranslations-Template.pdf`, and `logo.pdf`.

The MathTranslations founder and copyright holder authorized the template TeX
and logo for publication in this skill under the MIT License. Bundled copies
are available at:

- `assets/MathTranslations-Template.tex`, SHA-256
  `76F7B60A428192292779766E883376D0D4D15D50E3A3A24C367BE8AE7F35A5FD`;
- `assets/logo.pdf`, SHA-256
  `8B3839ADBF870A8C5E825C9F004125816835BBB321617E619E5F589B672FC8D5`.

The compiled template example PDF is not needed at runtime and is not bundled.
Use a user-supplied or current official template when it is newer, because the
online template may change.

The TeX comments mention `logo-mark.pdf`, `logo.svg`, and `logo-mark.svg`, but
those files are not in this archive and the active sample only loads
`logo.pdf`. Check actual `\includegraphics` calls rather than treating comment
text as a dependency.

## Authority

Keep two priorities separate:

1. the source book or paper PDF is the highest authority for content, formulas,
   structure, and displayed numbering;
2. the supplied `MathTranslations-Template.tex` is the highest authority for
   typesetting when the user has selected this template;
3. OCR, MinerU Markdown, or extracted TeX is a working draft only.

If source numbering conflicts with the template counters, adapt counters or
environment definitions so the displayed result matches the relevant source
edition. Do not hard-code visible numbers in prose.

## Engine And Base Layout

The inspected template expects:

- XeLaTeX, normally run at least twice;
- `ctexart` with `UTF8`, `12pt`, and `fontset=none`;
- A4 paper with 2.5 cm left/right and 2.8 cm top/bottom margins;
- CMU Serif for English;
- Fandol Song for Chinese prose and examples;
- Fandol Kai for a newly introduced term;
- Fandol Fang for definitions, lemmas, theorems, propositions, corollaries,
  and remarks;
- 2-em paragraph indentation, no paragraph skip, and 1.16 line spacing.

Use the full project build sequence when bibliography, index, or other tools
require more than two XeLaTeX runs.

## Cover Metadata

Replace every sample value before publishing:

```tex
\BookTitleCN
\BookTitleEN
\OriginalAuthor
\OriginalEdition
\OriginalPublisher
\OriginalYear
\Translator
\ModelUsed
\TranslationDate
```

The cover includes the Chinese and English titles, author, edition, publisher,
year, translator, primary model, update date, and `logo.pdf`. Keep provenance
accurate. Do not claim a model, translator, edition, or date that was not used.

## Terminology Contract

At the first formal introduction of a concept, use:

```tex
\newterm{stable-key}{中文术语}{English term}
```

The stable key must be unique and safe for a generated `term:<key>` label. The
command typesets the Chinese term in Kai, adds the English term in parentheses,
and records the first page for the terminology index.

After first introduction, write the Chinese term normally. Use `\termcn{...}`
only for deliberate visual emphasis; it does not add an index entry.

Place exactly one `\printterminology` call at the end of the document, after
the bibliography and all other translated content.

## Semantic Environments

The template numbers these environments by subsection:

- `definition`, `lemma`, `theorem`, `corollary`, `proposition`, and `remark`
  use Fang;
- `example` and `problem` use Song;
- `proof` uses Song and ends with `\square`;
- `example` and `remark` end with `\diamond`.

Keep the source environment type. Use labels and real references such as
`\autoref`, `\ref`, and `\eqref`. The template provides Chinese `\autoref`
names.

## Long Proofs

For a proof moved to the end of its subsection, use a matched pair:

```tex
\longprooflink{first-iso-proof}{查看完整证明}

\begin{longproof}{first-iso-proof}{\autoref{thm:first-iso}}
...
\end{longproof}
```

Each key must have exactly one source link and one `longproof` environment.
Place the long proof before the subsection's exercises. Do not move a proof
merely to shorten a page; use this mechanism for genuinely long proofs and
preserve the source's logical location.

## Exercises And Answers

Place subsection exercises in:

```tex
\begin{exercises}
  \item ...
\end{exercises}
```

The template labels them from the current subsection. Put answers in an
appendix using the matching subsection prefix:

```tex
\begin{answers}{1.2}
  \item ...
\end{answers}
```

The generated exercise and answer labels provide bidirectional links. Preserve
exercise order and ensure each answer points to the intended exercise.

## Links, Bibliography, And Section Style

The inspected template uses:

- `MidnightBlue` for internal links and URLs;
- `BrickRed` for citations;
- clickable table-of-contents titles and page numbers;
- numbered PDF bookmarks and no visible link boxes;
- chapter-like numbered `section` headings;
- appendix-aware section labels;
- a local `mybibliography` wrapper around `thebibliography`.

Preserve citation keys and source bibliography facts. A project may replace the
sample bibliography implementation only when it retains equivalent citation
behavior and the selected template's presentation.

## Adoption Procedure

1. Keep an untouched copy of the supplied archive or TeX for comparison.
2. If no template is supplied, copy
   `assets/MathTranslations-Template.tex` and `assets/logo.pdf` from this skill
   into the translation project. Never edit the bundled masters in place.
3. If a template is supplied, compare it with the bundled baseline and use the
   supplied version when it is newer or project-specific.
4. Compile the unchanged project copy to establish a baseline.
5. Replace all cover metadata.
6. Remove the sample body, not the required preamble, macros, or environments.
7. Import the source structure and adapt numbering to the relevant edition.
8. Use `\newterm` once for each indexed concept.
9. Keep long-proof and exercise-answer link pairs balanced.
10. Put `\printterminology` last.
11. Compile with XeLaTeX at least twice, run the template profile audit, and
    compare the generated PDF with both the source PDF and the template sample.
