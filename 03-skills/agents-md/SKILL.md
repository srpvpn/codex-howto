---
name: agents-md
description: Create or update AGENTS.md files using Codex best practices for durable project instructions
---

## User Input

Use the user's request text directly. They may specify:

- `create`
- `update`
- `audit`
- a path such as `src/api/AGENTS.md`

## Core principles

`AGENTS.md` is the Codex durable-instruction file. Keep it concise, stable, and useful across repeated sessions.

### Rules

1. Keep only information that should survive across many sessions.
2. Prefer commands, invariants, and architecture notes over style trivia.
3. Do not turn `AGENTS.md` into a linter or a task tracker.
4. Use nested `AGENTS.md` or `AGENTS.override.md` only where narrower scope is justified.

## Workflow

1. Find existing `AGENTS.md` and `AGENTS.override.md` files.
2. Inspect project layout and actual build/test commands.
3. Draft or improve the target file.
4. Remove noisy or transient instructions.
5. Present the proposed content before writing it.

## Good `AGENTS.md` content

- repo structure
- test/build commands
- risky areas
- architectural boundaries
- non-obvious workflow constraints

## Avoid

- long code samples
- style-guide dumps
- temporary sprint instructions
- generic “write clean code” advice

## Audit output

For `audit`, report:

- line count
- noisy sections to remove
- missing operational guidance
- whether nested overrides are warranted
