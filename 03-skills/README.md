# Skills in Codex

Skills are reusable instruction bundles that Codex can load on demand.

## Install locations

Use the Codex skill locations:

| Scope | Location |
|---|---|
| user | `~/.agents/skills/<name>/SKILL.md` |
| repo | `.agents/skills/<name>/SKILL.md` |
| plugin | `<plugin>/skills/<name>/SKILL.md` |

## Why skills matter

The Codex best-practices guide recommends turning repeated work into skills. Skills are the documented replacement for many “save this prompt somewhere and remember to paste it later” workflows.

Good skill use cases:

- code review heuristics
- repo-specific release processes
- documentation conventions
- framework-specific debugging checklists
- packaging repeatable research workflows

## Minimal skill

```text
.agents/skills/review-diff/SKILL.md
```

```yaml
---
name: review-diff
description: Review the current diff for correctness, regressions, and missing tests.
---

Inspect the current diff. Focus on correctness first, then regressions, security, and tests.
```

## Authoring guidance

- keep the `description` concrete so Codex can match it correctly
- keep core instructions in `SKILL.md`
- move bulky examples or templates into sibling files
- use skills for durable workflows, not one-off prompts

## Relationship to slash commands

In the Codex app:

- type `$skill-name` to invoke a skill explicitly
- enabled skills can also appear in the slash-command list
