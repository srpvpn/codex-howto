# Subagents in Codex

Codex supports built-in agents and custom project/user agents.

## Built-in agents

The official subagents docs list:

- `default`
- `worker`
- `explorer`

Use them as the baseline before inventing custom agents.

## Custom agent locations

| Scope | Location |
|---|---|
| user | `~/.codex/agents/<name>.toml` |
| repo | `.codex/agents/<name>.toml` |

Each custom agent file is a standalone TOML configuration layer.
This repository includes working examples in [.codex/agents](/home/mike/pl/codex-howto/.codex/agents).

## Required fields

Every standalone custom agent file must define:

- `name`
- `description`
- `developer_instructions`

Optional fields can include:

- `nickname_candidates`
- `model`
- `model_reasoning_effort`
- `sandbox_mode`
- `mcp_servers`
- `skills.config`

## Example

```toml
name = "reviewer"
description = "Review diffs for correctness, security, and missing tests."
developer_instructions = """
Prioritize correctness, regressions, and test coverage.
Do not implement fixes unless explicitly asked.
"""
sandbox_mode = "read-only"
model_reasoning_effort = "high"
```

See also:

- [example-agents.md](/home/mike/pl/codex-howto/04-subagents/example-agents.md)
- [.codex/agents/reviewer.toml](/home/mike/pl/codex-howto/.codex/agents/reviewer.toml)
- [.codex/agents/docs-researcher.toml](/home/mike/pl/codex-howto/.codex/agents/docs-researcher.toml)

## Global agent settings

Project-wide agent controls live under `[agents]` in `config.toml`, including:

- `agents.max_threads`
- `agents.max_depth`
- `agents.job_max_runtime_seconds`
