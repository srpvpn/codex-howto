# Advanced Codex Features

This section covers the documented advanced workflows that matter most once the basics are in place.

## Plan mode

The Codex app exposes `/plan-mode`, and the CLI exposes `/plan`.

Use plan mode for:

- multi-file refactors
- architectural changes
- risky migrations
- tasks where you want a plan before edits

## Review workflows

Codex exposes `/review` in both the app and CLI documentation. Use it for local change review rather than inventing a custom review command layer.

## Sandbox and approvals

The official security docs describe:

- default network access off
- sandbox modes `read-only`, `workspace-write`, `danger-full-access`
- approval controls that determine when Codex must stop and ask

These are the primary controls for how aggressively Codex can act in a local environment.

## Web search and cloud tasks

Codex docs explicitly cover:

- web search in the CLI
- Codex Cloud tasks
- agent internet access for cloud tasks

Do not assume full internet access by default. The docs say cloud-task internet access is configurable and local/network behavior is restricted by sandboxing and policy.

## Worktrees and local environments

The Codex app docs include worktrees and local environments. Use them to isolate experiments, compare branches, and keep reviewable work streams separate.
