# PR Review Plugin

Repo-local plugin example for Codex review workflows.

## Current Codex-aligned structure

- manifest: `.codex-plugin/plugin.json`
- plugin skills and assets stay at the plugin root
- any marketplace wiring belongs in `.agents/plugins/marketplace.json`

## Intent

This plugin is an example bundle for:

- local review workflows
- security-focused review prompts
- test-gap checks
- GitHub-backed review context through MCP

The actual review entrypoints should be implemented as:

- bundled skills
- optional MCP config
- optional app config

Use the main plugin docs in [../README.md](/home/mike/pl/codex-howto/07-plugins/README.md) as the source of truth for layout.
