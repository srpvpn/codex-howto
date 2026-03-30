# Slash Commands in Codex

This folder documents the built-in command surfaces exposed by Codex.

## Primary command surfaces

The current docs describe these reusable entry points:

- built-in slash commands in the CLI
- built-in slash commands in the Codex app
- explicit skill invocation with `$skill-name`
- skills surfaced in the slash menu when enabled

## Codex CLI slash commands

The current Codex CLI docs describe built-ins such as:

- `/permissions`
- `/sandbox-add-read-dir`
- `/agent`
- `/apps`
- `/clear`
- `/compact`
- `/copy`
- `/diff`
- `/exit`
- `/experimental`
- `/fast`
- `/feedback`
- `/init`
- `/logout`
- `/mcp`
- `/mention`
- `/model`
- `/plan`
- `/personality`
- `/ps`
- `/fork`
- `/resume`
- `/new`
- `/quit`
- `/review`
- `/status`
- `/debug-config`
- `/statusline`

Notes from the docs:

- `/approvals` remains available as an alias.
- `/init` is the documented way to scaffold `AGENTS.md`.
- `/review` runs a Codex review workflow on local changes.

## Codex app slash commands

The Codex app docs list:

- `/feedback`
- `/mcp`
- `/plan-mode`
- `/review`
- `/status`

The app docs also state that:

- typing `/` opens the slash list
- typing `$` explicitly invokes a skill
- enabled skills can also appear in the slash menu

## Recommended replacement for command-like workflows

If you want a reusable workflow in Codex, prefer one of these:

1. A repo skill in `.agents/skills/<name>/SKILL.md`
2. A bundled plugin that ships skills and MCP/app config
3. A `codex exec` wrapper in shell or CI for non-interactive workflows

## Example: replace an old custom command with a skill

```bash
mkdir -p .agents/skills/code-review
```

Create `.agents/skills/code-review/SKILL.md`:

```yaml
---
name: code-review
description: Review local changes for correctness, regressions, and missing tests.
---

Review the current diff. Prioritize correctness, regressions, security, and test gaps.
```

Then invoke it explicitly in the app with `$code-review`, or let Codex discover it automatically when relevant.
