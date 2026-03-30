# Codex Feature Catalog

Quick inventory of the repository’s documented Codex surfaces.

## Core surfaces

| Area | Codex concept | Primary path |
|---|---|---|
| CLI | `codex`, `codex exec`, flags, slash commands | `10-cli/` |
| Durable instructions | `AGENTS.md`, nested overrides, fallback filenames | `02-agents-md/` |
| Skills | `.agents/skills/<name>/SKILL.md` | `03-skills/` |
| Subagents | `.codex/agents/*.toml` | `04-subagents/` |
| MCP | `codex mcp add`, `[mcp_servers.*]` | `05-mcp/` |
| Hooks | hook events and command JSON contract | `06-hooks/` |
| Plugins | `.codex-plugin/plugin.json`, `.app.json`, optional `.mcp.json` | `07-plugins/` |
| Safe iteration | `/diff`, `/review`, worktrees, sandbox, approvals | `08-safe-iteration/` |
| Advanced workflows | plan mode, cloud/web features, review, approvals | `09-advanced-features/` |

## Recommended command-like workflow shapes

Use these patterns when you want reusable behavior in Codex:

1. Built-in slash commands for native CLI/app actions
2. `$skill-name` or auto-triggered skills for repeated workflows
3. Plugins for packaged skills and integrations
4. `codex exec` wrappers for one-shot automation and CI
