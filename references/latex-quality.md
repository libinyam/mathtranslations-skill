# LaTeX And Mathematical Fidelity

Read this reference when editing TeX, recovering content from OCR, resolving
notation, or repairing a translated project.

## Preserve Semantic Structure

- Keep definitions, lemmas, propositions, theorems, corollaries, remarks,
  examples, exercises, proofs, and solutions in their corresponding semantic
  environments.
- Preserve the distinction between assumptions and conclusions.
- Check every negation, quantifier, comparison sign, set operation, index,
  bound, and condition.
- Keep equation grouping and alignment when it communicates derivation or
  equivalence.
- Do not normalize notation merely because another notation is more familiar.

When the source seems mathematically wrong, record the exact location and the
evidence. Preservation and correction are separate editorial choices.

## Prefer Project-Native LaTeX

- Reuse existing commands, theorem styles, bibliography tools, and reference
  packages.
- Define a new macro only when it removes meaningful repetition or encodes a
  stable semantic choice.
- Avoid global package or class changes for a local translation issue.
- Keep generated files out of source directories when the project already has
  a build directory convention.

## References And Numbering

Every numbered object that is mentioned elsewhere should have a stable label.
Use the reference command already established by the project, such as `\ref`,
`\eqref`, `\autoref`, or `\cref`.

Never translate a source phrase into hard-coded output such as:

```tex
由定理 2.3 可知
```

Prefer:

```tex
由定理~\ref{thm:main}可知
```

Do not rename existing labels without updating all callers. Keep labels unique
across included files.

## Citations

- Preserve citation keys when importing source TeX.
- Check that every cited key exists in a bibliography source or `\bibitem`.
- Preserve page, theorem, chapter, and equation locators.
- Do not infer a publication year, author spelling, DOI, or title from memory.
- Distinguish a citation in the mathematical source from a translator's note.

## Chinese Typesetting

- Use natural Chinese punctuation in prose and mathematical punctuation that
  matches the surrounding syntax.
- Keep spaces, nonbreaking spaces, and line breaks intentional around references,
  names, units, and inline mathematics.
- Avoid raw Unicode mathematical lookalikes when a LaTeX command is intended.
- Keep proper names, acronyms, and transliterations consistent with the project
  glossary.
- Follow the project's existing convention for theorem names, quotation marks,
  emphasis, and parenthetical English.

## OCR And Transcription

Treat OCR as a draft, not evidence. Check common confusions including:

- `0`, `O`, `o`, and `\circ`;
- `1`, `l`, `I`, and `|`;
- `v`, `\nu`, `u`, and `\upsilon`;
- minus signs, hyphens, and long dashes;
- superscripts, subscripts, primes, bars, hats, and tildes;
- opening and closing delimiters;
- `\in`, `\ni`, `\subset`, and `\subseteq`;
- equation numbers mistaken for equation content.

For a formula recovered from an image, compare the compiled result visually
with the source before accepting it.

## Figures, Tables, And Assets

Check that every `\includegraphics` target resolves with the project's extension
and search-path rules. Do not redraw or replace mathematical diagrams unless
the user requests it or the source asset cannot legally or technically be used.
When recreating a diagram, compare geometry, labels, orientation, and semantic
relationships, not just visual style.

## Compilation Discipline

Use the project's build command. A successful single engine invocation may not
resolve bibliography, index, glossary, or cross-reference data, so run the full
build sequence.

Inspect logs for:

- LaTeX errors and undefined control sequences;
- undefined or multiply defined references and citations;
- missing files and fonts;
- overfull or underfull boxes that affect readability;
- rerun requests;
- bibliography, index, and glossary failures.

Compilation proves syntactic and toolchain consistency. It does not prove that
the translation or mathematics is correct.
