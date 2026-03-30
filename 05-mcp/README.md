# MCP in Codex

MCP gives Codex access to external tools and live systems.

## Two supported setup paths

The Codex MCP docs describe two primary ways to configure servers:

1. `codex mcp add ...`
2. `config.toml` with `[mcp_servers.<name>]`

## CLI example

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp
```

From the TUI, `/mcp` shows active servers.

## `config.toml` example

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]

[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
```

The docs describe both stdio and streamable HTTP servers, plus options such as:

- `command`
- `args`
- `env`
- `env_vars`
- `cwd`
- `url`
- `bearer_token_env_var`
- `http_headers`
- `env_http_headers`

For repository configuration, prefer `.codex/config.toml` and `codex mcp add`. Plugin bundles can additionally ship `.mcp.json` when they package their own MCP wiring.
