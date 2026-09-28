# Step 3: upstream table configuration and grid candidate validation

## Result
Development branch only; main and previous binary deliverables unchanged. Content acceptance remains FAILED. No output cells were manually corrected and no fixture was relaxed.

## Adapter change and regression
Added optional --table-mode cells, forwarding only upstream use_wired_table_cells_trans_to_html/use_wireless_table_cells_trans_to_html. Prediction options are part of the cache identity and exported metadata. Default remains upstream default. No new production parser, table solver or platform was added.
Code commit: 6abee20daeeee87dc08f46d163e3461af420164f. Regression commit: b13036de4e36077e7800c65ba4e0ec7f1e24d64f.
GitHub Actions run 36399527379: 35 tests passed, zero failures/skips, including real video codecs. Local: 34 passed / 1 skipped (PyAV absent). All eight local source/test SHA256 values were compared with the CI source manifest and matched. These are adapter regressions, not OCR accuracy scores.

## Real PP-StructureV3 comparison
Run 36399214526, commit 47a07854dbebfafea3dd1547d68e58ef9bdfdeed, artifact 10960011229. Original MP4/GameViewer_96iLJ4Cokv.mp4 frame 60, PTS 2 seconds. Same six source-cell anchors from tests/fixtures/native_acceptance.json, expected 17 complete columns. One unchanged native engine, unmodified JSON/Markdown/HTML/XLSX/DOCX exports.

| Input/mode | Native Excel | Columns | Matched exact cell anchors | Inference seconds |
|---|---|---:|---:|---:|
| full/default | A1:O30 | 15 | 0/6 | 94.8181 |
| full/cells | A1:P36 | 16 | 0/6 | 74.0651 |
| viewport/default | A1:O29 | 15 | 0/6 | 83.6276 |
| viewport/cells | A1:N35 | 14 | 0/6 | 69.1814 |
| viewport/cells, 2x | A1:O35 | 15 | 0/6 | 92.8633 |

Viewport xyxy=(18,0,1660,675) is a test-fixture crop, not hardcoded production detection. All five experiments executed and exported, but none passed content checks. Increasing image size did not solve this sample.
The default native Excel contains the two SRAM notes at J19/K20, whereas source anchors are P21/P23. Thus at least these errors are assignment/structure errors, not entirely missing OCR text. In geometry-mode variants those notes are missing from Excel. Raw native results already fail before our adapters can rewrite content.
Rendered full/cells Word and inspected its first page: extremely narrow, vertically wrapped columns remain. Not a complete document visual review.

## Isolated open-source grid candidate
img2table 1.4.2 plus Tesseract eng+chi_sim, no production dependency added. Initial run 36400273600 failed before inference because Pillow was missing in the isolated installation; fixed explicitly. Retry run 36400488876 at a8c7c66832c369f032c1709d2659357cd75d410e completed, artifact 10960695465.
- Full image: native A1:R37, 18 columns, extraction 26.7307 seconds, 0/6 exact anchors.
- Viewport: native A1:Q36, 17 columns, extraction 10.8763 seconds, 0/6 exact anchors.
- Column count alone is NOT acceptance. The viewport candidate still has wrong/missing source-cell text and addresses. No claim that all detected column boundaries or source row mappings are correct.

## Next bounded investigation
The grid candidate is worth a controlled geometry-versus-OCR comparison, but must not replace the production engine yet. Check its native cell bounding boxes against the screenshot, then evaluate the library-supported OCR integration with an appropriate existing OCR engine. Retain original frame/coordinates and unmodified candidate artifacts; do not hardcode six anchor answers. Still pending: complete cross-screen table/figure recovery, efficient verified frame selection, full-video and held-out acceptance.
