# Scripts Override

These instructions apply only inside `scripts/`.

- Treat `scripts/build_epub.py` and `scripts/tests/` as the source of truth for the EPUB pipeline.
- Keep Python changes formatted and lintable with the repo's `uv` workflow.
- Update tests when chapter order, metadata, or output filenames change.
- Do not hardcode stale EPUB names or old directory paths.
