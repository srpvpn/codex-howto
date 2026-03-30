# Codex Quick Reference

## Install and login

```bash
npm i -g @openai/codex
codex
codex login --device-auth
```

Codex can authenticate with a ChatGPT account or an API key. Cached credentials live in `~/.codex/auth.json` or the OS credential store.

## Core paths

| Purpose | Path |
|---|---|
| user config | `~/.codex/config.toml` |
| project config | `.codex/config.toml` |
| root instructions | `AGENTS.md` |
| nested overrides | `path/to/AGENTS.md` or `path/to/AGENTS.override.md` |
| repo skills | `.agents/skills/<name>/SKILL.md` |
| user skills | `~/.agents/skills/<name>/SKILL.md` |
| project subagents | `.codex/agents/<name>.toml` |
| user subagents | `~/.codex/agents/<name>.toml` |
| personal plugins | `~/.codex/plugins/<plugin>` plus `~/.agents/plugins/marketplace.json` |
| repo plugins | `plugins/<plugin>` plus `.agents/plugins/marketplace.json` |

## CLI essentials

```bash
codex
codex exec "review the diff and list risks"
codex exec --model gpt-5.4 --sandbox workspace-write "fix the failing test"
codex mcp add context7 -- npx -y @upstash/context7-mcp
```

Useful flags from the docs:

- `--model`, `-m`
- `--profile`, `-p`
- `--sandbox`, `-s`
- `--search`
- `--ask-for-approval`
- `--full-auto`
- `--output-last-message`
- `--output-schema`

## CLI slash commands

Documented built-ins include:

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

`/approvals` still works as an alias, but the docs note that it no longer appears in the CLI slash popup.

## Codex app slash commands

- `/feedback`
- `/mcp`
- `/plan-mode`
- `/review`
- `/status`

Skills can also be invoked explicitly with `$skill-name`, and enabled skills appear in the slash command list in the app.

## Config snippet

```toml
model = "gpt-5.4"
model_reasoning_effort = "medium"
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = false
writable_roots = ["./tmp"]

[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
```

## AGENTS.md notes

- `AGENTS.md` is the default durable instruction file.
- Nested `AGENTS.md` files narrow scope.
- `AGENTS.override.md` wins in a subdirectory when you need a hard override.
- `project_doc_fallback_filenames` lets Codex treat alternate filenames as instruction files.
- `project_doc_max_bytes` controls how much instruction content Codex reads.

## Hook facts

- Hooks are configured in `~/.codex/hooks.json` or `.codex/hooks.json`.
- Command hooks receive one JSON object on `stdin`.
- Common fields include `session_id`, `cwd`, `hook_event_name`, and `model`.
- `PreToolUse` and `PostToolUse` currently support Bash only.
- `SessionStart`, `UserPromptSubmit`, and `Stop` support structured JSON responses.

## Security defaults

- Official docs state that Codex runs with network access off by default.
- Sandbox modes: `read-only`, `workspace-write`, `danger-full-access`
- In `workspace-write`, outbound access is controlled by `sandbox_workspace_write.network_access`.
