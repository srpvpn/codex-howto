# DevOps Automation Plugin

Example Codex plugin for deployment and operations workflows.

## What belongs here in Codex

- reusable operational skills
- optional MCP config for infrastructure systems
- scripts invoked by skills or hooks
- plugin metadata in `.codex-plugin/plugin.json`

## Safe usage guidance

For Codex, deployment and incident workflows should usually be:

- explicit user-invoked skills
- constrained by approvals and sandbox policy
- paired with hooks for validation

Do not let this example imply that Codex should auto-deploy without explicit operator intent.
