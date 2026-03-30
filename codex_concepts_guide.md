# Codex Concepts Guide

This file is the shortest mental model for the surfaces used throughout this repository.

## 1. Instructions are files

Durable project guidance lives in `AGENTS.md`. Narrower directories can add their own `AGENTS.md`, and a directory can hard-replace inherited rules with `AGENTS.override.md`.

## 2. Skills are reusable workflows

Skills live under `.agents/skills/<name>/SKILL.md` or `~/.agents/skills/<name>/SKILL.md`. Use them for repeatable workflows that should be easy for Codex to discover and re-run.

## 3. Subagents are dedicated specialists

Custom subagents live in `.codex/agents/*.toml` or `~/.codex/agents/*.toml`. Use them when a task benefits from a separate role, model choice, or sandbox profile.

## 4. MCP connects Codex to external systems

For repository setup, configure servers with `codex mcp add` or `[mcp_servers.*]` in `.codex/config.toml`. Use MCP for tools and live system access, not for durable prose instructions.

## 5. Hooks enforce policy

Hooks run around Codex events and receive structured JSON on `stdin`. Use them to validate commands, append context, or stop a flow when required verification did not happen.

## 6. Safety is explicit

Sandbox mode, network access, and approvals are first-class controls. Safe Codex workflows usually combine conservative sandboxing, `/plan`, `/diff`, `/review`, and worktrees.
