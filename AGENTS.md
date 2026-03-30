# Codex How-To Workspace Rules

## Purpose

This repository documents Codex-native workflows. Keep examples aligned with current official Codex docs and avoid undocumented feature shapes.

## Working rules

- Prefer official OpenAI Codex docs over memory or third-party blog posts.
- Keep examples runnable or clearly marked as illustrative.
- Do not reintroduce old non-Codex paths or unsupported command-file conventions.
- When changing docs, verify commands, file paths, and config locations against current Codex documentation.
- Run the EPUB builder tests before claiming the scripts layer is complete.

## Validation

- Stale-reference audit: `rg -n "([cC][lL][aA][uU][dD][eE]|[aA][nN][tT][hH][rR][oO][pP][iI][cC])" -S`
- EPUB tests: `UV_CACHE_DIR=/tmp/uv-cache uv run --project scripts --extra dev python -m pytest scripts/tests/test_build_epub.py -q`
- EPUB build: `UV_CACHE_DIR=/tmp/uv-cache uv run scripts/build_epub.py`
