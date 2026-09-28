# Thin pipeline step 2: real execution versus content acceptance

## Delivery
Continues draft PR #3; main and original binary documents unchanged.
Tested source commit: b0558327fb9f4668d72ea0b1b16696c1d69333a0.
GitHub Actions run: https://github.com/abba-labs/mp4_anyisis/actions/runs/36397246051
Artifact: thin-pipeline-validation, ID 10959371077 (7-day retention).

The four earlier ZIP-only edge fixes are now in the branch (interval tail, empty result, ROI cache normalization, non-quadratic index writing). CPU MKL-DNN acceleration is enabled with an explicit --no-mkldnn compatibility switch. A NativeParser can be reused across videos; exporter retries in the same process reuse one retained native result. The persistent successful-output cache remains hash-checked. Failed exports across a new process may still require inference; this is not a persistent native-result cache.

Additional changes: initialization/inference/export timers; verify requested export files actually exist; include python-docx in parser dependencies/cache identity; pin PaddleX 3.7.2 and avoid installing conflicting OpenCV packages; reject using the source image's parent as an export directory. No new model or service framework.

## Actual regression and execution
- Local Python 3.13.5: 28 passed, 1 skipped (no local PyAV; not the supported production Python version).
- GitHub Python 3.11: 29 passed, 0 skipped, including real codec round trip.
- Six bounded frame samples from all five recordings completed real PP-StructureV3 inference and native Word export. Two samples also produced native Excel tables.
- All six repeated runs hit the validated output cache; no repeat OCR in those successful cache runs.
- The six samples are NOT five complete videos.

| sample | inference seconds | execution result |
|---|---:|---|
| SARC requirement, frame 2891 | 31.7364 | native Word/JSON/Markdown written |
| SARC diagram, frame 479 | 24.0668 | native Word and figure image written |
| MemoryMap, frame 60 | 89.4963 | native Word/Excel written, CONTENT FAILED |
| EFC design, frame 300 | 32.7098 | native Word written |
| EFC LRS, frame 600 | 18.4346 | native Word and figure image written |
| SRC design, frame 900 | 36.0014 | native Word/Excel written |

Engine initialization: 34.1361 seconds on the first case, zero new initialization on the other five. Inference still takes 18-89 seconds per image here; this does not meet an efficient full-recording processing goal.

## Source-anchored content checks
`python scripts/check_native_samples.py <validation-directory>` reads native JSON/XLSX without OCR or rewriting. References are in tests/fixtures/native_acceptance.json. Checks are deliberately small, not an accuracy percentage.

- SARC LIMIT【01】 reset-order text anchor: PASS (native JSON and rendered Word retain it).
- SARC image detected/exported: PASS for presence, NOT complete-figure recovery. The source frame and exported crop both cut the diagram at the bottom.
- MemoryMap: FAIL. Source shows A:Q (17 columns); native XLSX is A1:O30 (15 columns), with wrong cell placement and missing P21/P23 notes. The raw artifact is retained unchanged; no patching specific addresses to manufacture a pass.
- New Word files for these three samples were rendered successfully. SARC requirement and diagram page 1 and MemoryMap page 1 were visually checked. MemoryMap spans five pages and squeezes columns into narrow vertical strings; not an acceptable document. The other three Word files were not visually accepted.
- SARC text still contains watermark/timestamp fragments. A correct text anchor does not mean the whole page is clean.
- Spreadsheet graphical preview via artifact_tool failed to start its local daemon; Excel checks here use OOXML cell/shape inspection, not a claimed spreadsheet visual acceptance.

The executed workflow completed successfully, but content acceptance FAILED. A follow-up content gate and pipefail are added after this run so future CI cannot hide a failed command behind tee or equate export success with content correctness. That follow-up has not been rerun in GitHub Actions.

## Existing FFmpeg selection probe (not promoted to default)
Locally decoded both actual recordings with the upstream mpdecimate filter. A lossless 30-frame fixture changing 0x2800 -> 0x2808 -> 0x2800 retained all three states.

| filter hi / lo / frac | SARC retained / 3325 | MemoryMap retained / 852 |
|---|---:|---:|
| 64 / 32 / 0 | 2741 | 802 |
| 512 / 512 / 0 | 715 | 225 |
| 768 / 320 / 0.33 | 714 | 215 |

These are retained frame counts, NOT coverage scores. No full-content or scroll-overlap acceptance was performed. The filter is not made the product default merely because it returns fewer frames. Existing exact-selection mode is still slow.

## Next bounded task
Use this same source-anchored check to test upstream wired-table configuration and effective-content cropping, rather than rewriting table reconstruction. Then verify cross-screen image/table reconstruction before enabling faster selection by default. Full-video acceptance, Windows installation and full spreadsheet cell validation remain incomplete.

Upstream parameter references:
- https://www.paddleocr.ai/v3.3.0/en/version3.x/pipeline_usage/PP-StructureV3.html
- https://ffmpeg.org/ffmpeg-filters.html#mpdecimate
