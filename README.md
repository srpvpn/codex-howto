<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/codex-howto-logo-dark.svg">
  <img alt="Codex How-To" src="resources/logos/codex-howto-logo.svg">
</picture>

# Codex How-To

Practical, repo-backed notes for learning Codex from the current official OpenAI documentation.

This repository is intentionally Codex-native. It focuses on documented Codex paths, commands, and extension points instead of carrying over undocumented behaviors from other tools.

## What This Repo Covers

- Codex CLI setup and authentication
- `AGENTS.md` project instructions
- skills in `.agents/skills/`
- subagents in `.codex/agents/*.toml`
- MCP in `.codex/config.toml` or via `codex mcp add`
- hooks and approval/sandbox controls
- plugins with `.codex-plugin/plugin.json`
- Codex app and CLI slash commands

## Design Principles

- Prefer documented Codex surfaces over inferred equivalents.
- Use Codex-native filenames and config locations throughout the repository.
- Keep examples small, runnable, and aligned with current CLI/app behavior.
- Treat the official Codex docs as the source of truth; this repo is a learning layer on top.

## Table of Contents

- [Quick Start](#quick-start)
- [Learning Path](#learning-path)
- [Repo-Backed Examples](#repo-backed-examples)
- [Primary References](#primary-references)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

Install Codex:

```bash
npm i -g @openai/codex
codex
```

Recommended first session:

```text
1. Start `codex` in your repository
2. Run `/init` to scaffold `AGENTS.md`
3. Add one reusable skill under `.agents/skills/`
4. Add one MCP server with `codex mcp add ...`
5. Add one project subagent under `.codex/agents/`
```

Example setup:

```bash
# add AGENTS instructions interactively from the TUI
codex

# add an MCP server
codex mcp add context7 -- npx -y @upstash/context7-mcp

# create repo-local skill and subagent folders
mkdir -p .agents/skills/code-review
mkdir -p .codex/agents
```

## Learning Path

| Order | Module | Focus |
|---|---|---|
| 1 | [10-cli](10-cli/) | CLI commands, flags, profiles, and automation |
| 2 | [01-slash-commands](01-slash-commands/) | Built-in Codex slash commands and skill invocation |
| 3 | [02-agents-md](02-agents-md/) | `AGENTS.md` and instruction discovery |
| 4 | [03-skills](03-skills/) | Repo/user skills and `SKILL.md` authoring |
| 5 | [04-subagents](04-subagents/) | Built-in agents and custom TOML agents |
| 6 | [05-mcp](05-mcp/) | MCP via CLI and `config.toml` |
| 7 | [06-hooks](06-hooks/) | Hook events, `hooks.json`, JSON I/O, policy guardrails |
| 8 | [07-plugins](07-plugins/) | `.codex-plugin/plugin.json` and marketplaces |
| 9 | [08-safe-iteration](08-safe-iteration/) | Diff, review, sandbox, worktrees, and approval-safe iteration |
| 10 | [09-advanced-features](09-advanced-features/) | plan mode, review, sandbox, approvals, cloud/web features |

## Repo-Backed Examples

The repository now includes minimal working Codex-native artifacts:

- root [AGENTS.md](/home/mike/pl/codex-howto/AGENTS.md)
- scoped override at [scripts/AGENTS.override.md](/home/mike/pl/codex-howto/scripts/AGENTS.override.md)
- project config at [.codex/config.toml](/home/mike/pl/codex-howto/.codex/config.toml)
- project hooks config at [.codex/hooks.json](/home/mike/pl/codex-howto/.codex/hooks.json)
- runnable hook scripts under [.codex/hooks](/home/mike/pl/codex-howto/.codex/hooks)
- custom subagent examples under [.codex/agents](/home/mike/pl/codex-howto/.codex/agents)

## Primary References

- [Codex CLI](https://developers.openai.com/codex/cli)
- [Command line options](https://developers.openai.com/codex/cli/reference)
- [Slash commands in Codex CLI](https://developers.openai.com/codex/cli/slash-commands)
- [Codex app commands](https://developers.openai.com/codex/app/commands)
- [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- [Agent Skills](https://developers.openai.com/codex/skills)
- [Subagents](https://developers.openai.com/codex/subagents)
- [Model Context Protocol](https://developers.openai.com/codex/mcp)
- [Hooks](https://developers.openai.com/codex/hooks)
- [Build plugins](https://developers.openai.com/codex/plugins/build)
- [Authentication](https://developers.openai.com/codex/auth)
- [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security)
- [Best practices](https://developers.openai.com/codex/learn/best-practices)

## Contributing

See [CONTRIBUTING.md](/home/mike/pl/codex-howto/CONTRIBUTING.md) for contribution rules and validation commands.

## License

This repository is released under the [MIT License](/home/mike/pl/codex-howto/LICENSE).
