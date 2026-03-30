# Codex Learning Roadmap

This roadmap follows the current Codex docs and the structure of this repository.

## Phase 1: First productive session

- [ ] Install Codex with `npm i -g @openai/codex`
- [ ] Start `codex` in a real repository
- [ ] Authenticate with a ChatGPT account or API key
- [ ] Run `/status` and `/model`
- [ ] Run `/init` and inspect the generated `AGENTS.md`

## Phase 2: Durable project setup

- [ ] Create or refine `AGENTS.md`
- [ ] Add a nested `AGENTS.override.md` for one subdirectory
- [ ] Create one repo skill in `.agents/skills/`
- [ ] Create one project subagent in `.codex/agents/`
- [ ] Add one MCP server with `codex mcp add ...`

## Phase 3: Safe execution controls

- [ ] Understand `read-only`, `workspace-write`, and `danger-full-access`
- [ ] Inspect current approvals with `/permissions` or `/status`
- [ ] Add a hook in `.codex/config.toml`
- [ ] Review the diff with `/diff`
- [ ] Run `/review` on local changes

## Phase 4: Reusable automation

- [ ] Package a skill into a plugin
- [ ] Learn the `.codex-plugin/plugin.json` manifest
- [ ] Add a repo marketplace in `.agents/plugins/marketplace.json`
- [ ] Use `codex exec` for scripted one-shot tasks
- [ ] Explore Codex app slash commands and plan mode

## Suggested module order

1. [10-cli](10-cli/)
2. [01-slash-commands](01-slash-commands/)
3. [02-agents-md](02-agents-md/)
4. [03-skills](03-skills/)
5. [04-subagents](04-subagents/)
6. [05-mcp](05-mcp/)
7. [06-hooks](06-hooks/)
8. [07-plugins](07-plugins/)
9. [08-safe-iteration](08-safe-iteration/)
10. [09-advanced-features](09-advanced-features/)

## Primary docs to read alongside this repo

- Codex CLI
- Command line options
- Slash commands in Codex CLI
- Codex app commands
- Custom instructions with `AGENTS.md`
- Agent Skills
- Subagents
- Model Context Protocol
- Hooks
- Build plugins
- Authentication
- Agent approvals & security
- Best practices
