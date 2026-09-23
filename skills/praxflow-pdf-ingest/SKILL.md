---
name: praxflow-pdf-ingest
description: Convert repository-owned PDFs into traceable raw Markdown, page images for visual evidence, and an extraction report. Use before semantic interpretation, specification, or implementation.
---

# PraxFlow PDF Ingest

Transform source PDFs into faithful, traceable raw artifacts. This skill extracts evidence; it does not design the product or generate production code.

## Inputs

Accept one or more PDF paths, normally under `input/`. If no path is provided, discover PDFs in `input/`.

## Preferred execution

For ordinary text-heavy PDFs, use the bundled helper first:

```bash
python skills/praxflow-pdf-ingest/scripts/extract_pdf.py input/<file>.pdf --out-dir docs/raw --json
```

For schematics, circuit diagrams, engineering drawings, layout-dependent tables, or other PDFs whose meaning depends on spatial relationships, render every page:

```bash
python skills/praxflow-pdf-ingest/scripts/extract_pdf.py input/<file>.pdf --out-dir docs/raw --schematic --json
```

Equivalent explicit form:

```bash
python skills/praxflow-pdf-ingest/scripts/extract_pdf.py input/<file>.pdf --out-dir docs/raw --render-images all --dpi 180 --json
```

When installed as a plugin outside the target repo, resolve the script relative to this skill directory rather than assuming the target repository contains `skills/`.

The helper tries PyMuPDF first and then pypdf for text extraction. Page rendering requires PyMuPDF. It deliberately does not OCR pages automatically.

## Extraction strategy

1. Classify each PDF as text, table-heavy, scanned, schematic/drawing, or mixed.
2. Prefer the existing PDF text layer for textual evidence.
3. Use the bundled helper or equivalent local extraction tools.
4. For schematics/drawings, always render all relevant pages and treat the page image as primary visual evidence.
5. For ordinary PDFs, the default `--render-images candidates` renders pages with little/no extractable text.
6. Inspect visually important tables, diagrams, symbols, wires, labels, and spatial relationships when text extraction is insufficient.
7. Use OCR only for pages that cannot be reliably extracted otherwise and only when textual transcription is needed.
8. Preserve page boundaries and source file identity.
9. Preserve headings, numbering, tables, units, hexadecimal values, signs, decimal points, and data types.
10. Never silently normalize an ambiguous token.

## Schematic and drawing rule

For electrical schematics and engineering drawings:

- Run with `--schematic` (or `--render-images all`).
- Generated images are written to `docs/raw/<stem>_images/page_NNN.png`.
- Use a vision-capable model to inspect the rendered page images when available.
- Do not infer electrical connectivity from extracted labels alone.
- Prefer netlist/native structured design data when exact connectivity is required.
- If the active model cannot consume images, keep the rendered artifacts and add `TODO_VERIFY` for visual relationships that cannot be established from text alone.

The rendered image is evidence for layout, symbols, wires, annotations, pin labels, and other spatial relationships. It is not a replacement for a netlist when exact electrical connectivity matters.

## Uncertainty rule

For unclear or conflicting content, write `TODO_VERIFY` with:
- source file
- page number
- observed text/image interpretation
- candidate interpretations if useful

Do not choose a candidate without evidence.

## Outputs

For each input PDF create:

```text
docs/raw/<stem>_raw.md
docs/raw/<stem>_extraction_report.md
docs/raw/<stem>_images/page_NNN.png   # when rendering is enabled for a page
```

The raw file must annotate source pages, for example:

```markdown
<!-- source_file: device.pdf -->
<!-- source_page: 18 -->
<!-- source_page_image: device_images/page_018.png -->
```

The extraction report must include:
- total pages
- extraction method by page/range
- render mode and DPI
- rendered page image list
- detected/visually relevant tables or diagrams when known
- OCR pages/candidates
- low-confidence or failed pages
- count/list of `TODO_VERIFY`
- overall result: `PASS`, `PASS_WITH_WARNINGS`, or `BLOCKED`

## Render modes

- `--render-images none`: text extraction only.
- `--render-images candidates`: default; render pages with very little extractable text.
- `--render-images all`: render every page.
- `--schematic`: shortcut for `--render-images all`.
- `--dpi N`: page render resolution, 72-600 DPI; default 180.

## Prohibited actions

- Do not create product requirements from implied meaning.
- Do not convert guesses into facts.
- Do not create ADRs.
- Do not create implementation specs.
- Do not modify source PDFs.
- Do not generate production code.
- Do not claim a wire/net connection based only on nearby extracted text.

Stop after extraction, visual follow-up for flagged/rendered pages as needed, and report generation.
