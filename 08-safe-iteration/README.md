# Safe Iteration in Codex

This section gathers the documented controls that make larger edits safer.

## Core safety toolkit

Use these mechanisms together:

- `/diff` to inspect local changes
- `/review` before keeping a branch of work
- git branches and worktrees
- `read-only` or `workspace-write` sandboxing while exploring
- plan mode before risky edits

## Recommended sequence

1. Start with `/plan` or `/plan-mode` for risky work.
2. Keep sandboxing conservative while exploring.
3. Inspect `/diff` before accepting broad edits.
4. Run `/review` on meaningful changesets.
5. Use git branches or worktrees when comparing alternative implementations.

## Scope of this module

This module focuses on the safety controls that are explicitly documented in the current Codex docs set used by this repository.
