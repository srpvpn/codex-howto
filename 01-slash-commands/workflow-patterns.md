# Codex Workflow Patterns

When you want command-like reuse in Codex, use documented surfaces instead of filesystem-backed custom command files.

## Pattern 1: Built-in slash command

Use a native slash command when Codex already provides the action:

- `/review` for review mode
- `/diff` for working tree inspection
- `/plan` for planning
- `/mcp` for MCP visibility

## Pattern 2: Skill

Use a skill when the workflow is reusable and instruction-heavy.

```text
.agents/skills/code-review/SKILL.md
```

## Pattern 3: `codex exec`

Use `codex exec` when the workflow is one-shot or CI-friendly.

```bash
codex exec --output-schema review-schema.json "Review the current diff and return structured risks."
```

## Pattern 4: Plugin

Use a plugin when the workflow needs to package skills and integration metadata for reuse across repositories.
