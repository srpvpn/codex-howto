# Contributing to Codex How-To

Contributions should improve the repository’s alignment with current official Codex documentation.

## Contribution rules

- prefer official OpenAI Codex docs over memory or third-party blog posts
- prefer documented Codex-native paths, commands, and config locations
- do not introduce undocumented features or guessed equivalents
- keep examples executable where possible

## High-value contribution areas

- tighten examples against current CLI/app docs
- improve skills, subagents, hooks, and plugin examples
- replace vague prose with file-backed workflows and verification commands
- tighten module READMEs against current docs
- add tests for build metadata and generated output names

## Before opening a PR

Run a targeted stale-reference audit:

```bash
rg -n "([cC][lL][aA][uU][dD][eE]|[aA][nN][tT][hH][rR][oO][pP][iI][cC])" -S
```
