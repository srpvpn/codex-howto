# Plugins in Codex

Plugins package skills and integrations for reuse.

## Required manifest

Every Codex plugin must have:

```text
.codex-plugin/plugin.json
```

The Codex plugin docs describe this as the required entry point.

## Plugin structure

```text
my-plugin/
├── .codex-plugin/
│   └── plugin.json
├── skills/
│   └── my-skill/
│       └── SKILL.md
├── .mcp.json
├── .app.json
└── assets/
```

Only `plugin.json` belongs inside `.codex-plugin/`. Keep `skills/`, `.mcp.json`, `.app.json`, and assets at the plugin root.

## Repo-local marketplace

For repo plugins, the docs describe:

- plugin folders under `plugins/`
- marketplace file at `.agents/plugins/marketplace.json`

## Minimal manifest

```json
{
  "name": "my-plugin",
  "version": "0.1.0",
  "description": "Bundle reusable skills and app integrations.",
  "skills": "./skills/"
}
```

## Useful manifest fields

- `name`
- `version`
- `description`
- `author`
- `homepage`
- `repository`
- `license`
- `keywords`
- `skills`
- `mcpServers`
- `apps`
- `interface`

Package reusable skills and integrations around this structure:

- `.codex-plugin/plugin.json`
- `skills/`
- optional `.mcp.json`
- optional `.app.json`
- marketplace entries
