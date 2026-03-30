# AGENTS.md Guide

This module covers durable instruction discovery through `AGENTS.md`.

## Core rule

Use `AGENTS.md` for durable, repo-scoped guidance that Codex should keep applying over time.

The official Codex best-practices guide explicitly recommends using `AGENTS.md` for durable guidance, then layering skills, MCP, and automation on top.

## Recommended layout

```text
repo/
├── AGENTS.md
├── .codex/
│   ├── config.toml
│   └── agents/
└── services/
    └── payments/
        ├── AGENTS.md
        └── AGENTS.override.md
```

## Discovery behavior

The Codex `AGENTS.md` guide describes three important ideas:

- root `AGENTS.md` for repository-wide expectations
- nested `AGENTS.md` files for narrower local guidance
- `AGENTS.override.md` when a subdirectory needs to replace, not just extend, inherited guidance

The docs also note that Codex stops searching once it reaches the current directory, so overrides should live close to the specialized code they govern.

## Useful config keys

In `config.toml`, the docs expose keys for instruction-file handling, including:

- `project_doc_fallback_filenames`
- `project_doc_max_bytes`

Use these when you need alternate instruction filenames or tighter control over how much instruction content Codex ingests.

## Good `AGENTS.md` content

Keep it durable and operational:

- repo structure
- test commands
- formatting/linting commands
- approval expectations
- risky directories or deployment rules
- architectural constraints

Avoid transient ticket-specific details that will rot quickly.

## Minimal example

```md
# AGENTS

## Repository rules
- Run `pytest -q` before claiming a Python change is complete.
- Prefer `rg` for code search.
- Do not edit generated files under `dist/` by hand.

## API area
- Validate request payloads before persistence.
- Keep handlers thin; move business logic into service modules.
```

## Practical workflow

1. Run `codex`
2. Use `/init` to scaffold `AGENTS.md`
3. Edit the file until it reflects stable project rules
4. Add nested `AGENTS.md` or `AGENTS.override.md` only where the root rules become too broad
