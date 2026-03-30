# Safe Iteration Examples

These examples show Codex-safe workflows grounded in documented features.

## Example 1: Try two implementations with git worktrees

```text
1. Create a worktree for approach A
2. Run Codex there and implement the first version
3. Create a second worktree for approach B
4. Run Codex there and implement the alternative
5. Compare diffs and keep the better branch
```

## Example 2: Review before keeping changes

```text
1. Ask Codex to implement a refactor
2. Inspect `/diff`
3. Run `/review`
4. If the review surfaces regressions, revert with git or discard the worktree
5. Re-run in a safer plan-driven pass
```

## Example 3: Use plan mode before risky migrations

```text
User: /plan Migrate the auth layer from sessions to JWT

Codex:
- outlines files to change
- calls out migration and rollback risks
- waits for approval before broad edits
```
