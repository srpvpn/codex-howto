# Codex CLI Reference

## Install

```bash
npm i -g @openai/codex
codex
```

The CLI docs state that the first run prompts you to sign in with a ChatGPT account or an API key.

## Primary commands

| Command | Purpose |
|---|---|
| `codex` | interactive TUI |
| `codex exec "prompt"` | non-interactive execution |
| `codex exec resume --last` | continue the last exec session |
| `codex login --device-auth` | login flow |
| `codex login status` | inspect current auth state |
| `codex mcp add ...` | register an MCP server |
| `codex mcp --help` | inspect MCP subcommands |

## Useful flags

| Flag | Purpose |
|---|---|
| `--model`, `-m` | override model for the run |
| `--profile`, `-p` | select a profile from `config.toml` |
| `--sandbox`, `-s` | choose `read-only`, `workspace-write`, or `danger-full-access` |
| `--search` | enable built-in web search |
| `--ask-for-approval` | control approval behavior |
| `--full-auto` | run with an automation-oriented approval preset |
| `--output-last-message` | write the final assistant message to a file |
| `--output-schema` | validate the final response against a JSON schema |
| `--json` | emit newline-delimited JSON events |

## Slash commands

The CLI slash-command docs describe built-ins including:

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
- `/new`
- `/quit`
- `/resume`
- `/review`
- `/status`
- `/debug-config`
- `/statusline`

## Config locations

| Scope | Path |
|---|---|
| user | `~/.codex/config.toml` |
| project | `.codex/config.toml` |

## Minimal config

```toml
model = "gpt-5.4"
model_reasoning_effort = "medium"
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = false
```

## Authentication notes

The official auth docs describe login via ChatGPT account or API key. The CLI docs also mention cached authentication state in `~/.codex/auth.json`.
