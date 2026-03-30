# Hooks in Codex

Hooks let you enforce policy or add automation around Codex events.

## Where hooks live

Codex hooks are configured in `~/.codex/hooks.json` or `.codex/hooks.json`.

Typical layout:

```text
repo/
├── .codex/
│   ├── config.toml
│   ├── hooks.json
│   └── hooks/
│       ├── pre_tool_use_bash_guard.py
│       └── post_tool_use_log.py
```

## Hook contract

The docs state that every command hook receives one JSON object on `stdin`.

Common input fields include:

- `session_id`
- `transcript_path`
- `cwd`
- `hook_event_name`
- `model`

For turn-scoped hooks, `turn_id` appears in the event-specific payload.

## Important event facts

- `SessionStart`, `UserPromptSubmit`, and `Stop` support structured JSON responses.
- `PreToolUse` currently supports Bash interception only.
- `PostToolUse` currently supports Bash post-tool results only.
- Commands should read one JSON payload from `stdin`.

## Example hook configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_bash_guard.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ]
  }
}
```

## Practical use cases

- block dangerous shell commands before execution
- append context after a formatter or test run
- inject extra repo guidance at session start
- stop completion when required verification did not run

Working examples in this repository:

- [.codex/hooks.json](/home/mike/pl/codex-howto/.codex/hooks.json)
- [.codex/hooks/pre_tool_use_bash_guard.py](/home/mike/pl/codex-howto/.codex/hooks/pre_tool_use_bash_guard.py)
- [.codex/hooks/post_tool_use_log.py](/home/mike/pl/codex-howto/.codex/hooks/post_tool_use_log.py)
- [.codex/hooks/user_prompt_submit_context.py](/home/mike/pl/codex-howto/.codex/hooks/user_prompt_submit_context.py)
