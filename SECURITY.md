# Security Policy

This repository documents Codex workflows. Vulnerabilities in Codex itself should be reported to OpenAI through official security channels, not filed here as if they were repository bugs.

## Scope

Use this repository issue flow for:

- malicious or unsafe example scripts in the repo
- secrets committed to the repo
- insecure plugin or hook examples
- documentation that instructs unsafe Codex usage against current official guidance

Do not use this repository for:

- product vulnerabilities in Codex
- account issues
- OpenAI service abuse reports unrelated to this codebase

## Secure-by-default guidance for this repo

- prefer `read-only` or `workspace-write` examples over unrestricted access
- note that official Codex docs say network access is off by default
- treat hook and MCP examples as sensitive because they can run local commands or reach external systems
- require explicit wording when a sample escalates privileges or enables network access

## Reporting

Open a private security advisory or contact the maintainers with:

- affected files
- exact reproduction steps
- impact
- suggested fix
