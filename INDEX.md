# Codex How-To Index

This index is the shortest map of the repository.

## Top-level docs

| File | Purpose |
|---|---|
| `README.md` | project overview and module map |
| `QUICK_REFERENCE.md` | short command/path reference |
| `LEARNING-ROADMAP.md` | suggested learning order |
| `CATALOG.md` | feature inventory by Codex surface |
| `codex_concepts_guide.md` | high-level mental model for the platform |

## Module index

| Folder | Current Codex focus |
|---|---|
| `01-slash-commands/` | built-in slash commands and skill invocation |
| `02-agents-md/` | `AGENTS.md`, nested instructions, fallback filenames |
| `03-skills/` | `.agents/skills`, `SKILL.md`, creator workflows |
| `04-subagents/` | `.codex/agents/*.toml`, built-in agents, delegation patterns |
| `05-mcp/` | `codex mcp add`, `[mcp_servers.*]`, TUI `/mcp` |
| `06-hooks/` | hook events, JSON contract, command hooks |
| `07-plugins/` | `.codex-plugin/plugin.json`, marketplaces, plugin layout |
| `08-safe-iteration/` | `/diff`, `/review`, worktrees, approvals, safe iteration |
| `09-advanced-features/` | plan mode, approvals, sandboxing, review, cloud/web features |
| `10-cli/` | install, login, flags, scripting, non-interactive usage |

## Verification commands

```bash
rg -n "([cC][lL][aA][uU][dD][eE]|[aA][nN][tT][hH][rR][oO][pP][iI][cC])" -S
UV_CACHE_DIR=/tmp/uv-cache uv run --project scripts --extra dev python -m pytest scripts/tests/test_build_epub.py -q
```
