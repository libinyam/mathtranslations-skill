# MathTranslations Template Profile

Read this reference when the user supplies or requests
`mathtranslations-translation-template.zip` or
`mathtranslations-translation-template.tex`. Archives named
`MathTranslations-Template.zip` or `MathTranslations-Template.tex` are earlier
releases of the same template.

## Inspected Version

The profile below was derived from the locally supplied archive:

- archive: `mathtranslations-translation-template.zip`;
- inspected: 2026-08-23;
- SHA-256:
  `4C2E5AD1C81646B4E8AD53F4B5FD5BAA7D477C749915E32CF52B5EE71F85F12E`;
- contents: `mathtranslations-translation-template.tex`,
  `mathtranslations-translation-template.pdf`, and `logo.pdf`.

The MathTranslations founder and copyright holder authorized the template TeX
and logo for publication in this skill under the MIT License. Bundled copies
are available at:

- `assets/mathtranslations-translation-template.tex`, SHA-256
  `B2CC106209969E77878F3BA6DFE0BF050D4D38DA0C68E558A96241350827531E`;
- `assets/logo.pdf`, SHA-256
  `8B3839ADBF870A8C5E825C9F004125816835BBB321617E619E5F589B672FC8D5`.

The compiled template example PDF is not needed at runtime and is not bundled.
Use a user-supplied or current official template when it is newer, because the
online template may change.

## Authority

Keep two priorities separate:

1. the source book or paper PDF is the highest authority for content, formulas,
   structure, and displayed numbering;
2. the supplied `mathtranslations-translation-template.tex` is the highest
   authority for typesetting when the user has selected this template;
3. OCR, MinerU Markdown, or extracted TeX is a working draft only.

If source numbering conflicts with the template counters, adapt counters or
environment definitions so the displayed result matches the relevant source
edition. Do not hard-code visible numbers in prose.

## Engine And Base Layout

The inspected template expects:

- XeLaTeX, normally run at least twice;
- `ctexart` with `UTF8`, `12pt`, and `fontset=none`;
- `tikz-cd` for commutative and arrow-and-node mathematical diagrams;
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
year, translator, primary model, update date, and `logo.pdf`. In the
bottom-right corner the publisher line (`\OriginalEdition · \OriginalPublisher
· \OriginalYear`) is followed by a `\Translator 翻译及重排` credit line set
slightly larger than the publisher line. Keep provenance accurate. Do not
claim a model, translator, edition, or date that was not used.

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

## Display Math, Lists, And Quotes

The template requires three uniform typesetting habits:

- display formulas use `align`, `aligned`, or `align*` environments only;
  multiple `\[ \]` blocks in a row must be merged into one environment. The
  sample body demonstrates numbered `align` with `\label`/`\eqref` and
  unnumbered `align*`;
- every ordered list uses `enumerate`; manual numbering is not accepted;
- Chinese double quotes use the TeX ligatures — two grave accents for the
  opening quote and two straight apostrophes for the closing quote — never
  Unicode curly quotes, because the apostrophe pair alone renders a closing
  quote.

The audit script flags consecutive display-math blocks, Unicode curly quotes,
and manually numbered lists under the `mathtranslations` profile.

## Figures

Figure handling follows this priority:

1. when the source PDF has good quality and the figure is clear, crop a
   faithful screenshot as the preferred asset;
2. redraw simple figures with ordinary TikZ;
3. rebuild every commutative diagram, morphism diagram, category diagram,
   pullback or pushout square, and similar arrow-and-node diagram in a
   `tikzcd` environment — never as a screenshot.

The bundled template loads `tikz` and `tikz-cd`. Compare the compiled result
with the source for node placement, labels, arrow directions, hooks,
two-headed arrows, isomorphisms, dashed arrows, bends, and commutative
relationships. Record any figure that cannot follow this priority.

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
   `assets/mathtranslations-translation-template.tex` and `assets/logo.pdf`
   from this skill into the translation project. Never edit the bundled
   masters in place.
3. If a template is supplied, compare it with the bundled baseline and use the
   supplied version when it is newer or project-specific.
4. Compile the unchanged project copy to establish a baseline.
5. Replace all cover metadata and keep the `\Translator 翻译及重排` credit
   line below the publisher line.
6. Remove the sample body, not the required preamble, macros, or environments.
7. Import the source structure and adapt numbering to the relevant edition.
8. Use `\newterm` once for each indexed concept.
9. Keep long-proof and exercise-answer link pairs balanced.
10. Typeset display math with `align`-family environments, ordered lists with
    `enumerate`, and Chinese quotes with the TeX ligatures.
11. Put `\printterminology` last.
12. Compile with XeLaTeX at least twice, run the template profile audit, and
    compare the generated PDF with both the source PDF and the template sample.
