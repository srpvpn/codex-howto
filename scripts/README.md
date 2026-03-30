# EPUB Builder Script

Build an EPUB ebook from the Codex How-To markdown files.

## Quick start

```bash
uv run scripts/build_epub.py
```

## Output

By default the script creates `codex-howto-guide.epub`.

## Tests

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run --project scripts --extra dev python -m pytest scripts/tests/test_build_epub.py -q
```
