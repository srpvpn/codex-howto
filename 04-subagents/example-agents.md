# Example Custom Agents

This repository includes working project-local custom agent files under [.codex/agents](/home/mike/pl/codex-howto/.codex/agents).

## Included examples

- [reviewer.toml](/home/mike/pl/codex-howto/.codex/agents/reviewer.toml)
- [docs-researcher.toml](/home/mike/pl/codex-howto/.codex/agents/docs-researcher.toml)

## Why these matter

They demonstrate the documented Codex format directly:

- TOML files, not markdown agent prompts
- required fields: `name`, `description`, `developer_instructions`
- optional config keys such as `model`, `model_reasoning_effort`, and `sandbox_mode`

## Suggested exercise

1. Start Codex in this repository.
2. Ask for a review task that benefits from one of these agents.
3. Inspect how the agent role changes the result.
