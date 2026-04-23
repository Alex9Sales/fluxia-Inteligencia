---
name: cerebro-openclaw
description: Load and orient on the project second-brain inside this OpenClaw workspace. Use when reconnecting to project context, checking current priorities, finding the right source of truth for business/agent/brand docs, or briefing yourself before important work in this repo.
---

# Cerebro OpenClaw

Use this skill to reconnect to the second-brain structure of this workspace without overloading context or inventing a parallel system.

## Goal

Quickly orient on:
- what this workspace is
- where truth lives
- what the current priorities are
- which files matter for the task at hand

## Core rule

Do not read everything by default.
Read only the files needed for the current task.

## Orientation order

### 1. Start with the map
Read `MAPA.md` when you need to understand where a topic should live.

### 2. Check strategic state
Read these selectively when relevant:
- `PRIORITIES.md`
- `TASKS.md`
- `MEMORY.md`

### 3. Move to domain-specific context
Use the task to choose the next file:
- business and positioning → `cerebro/empresa/`
- operational area → `cerebro/areas/`
- agent roles/personas → `cerebro/agents/`
- reusable flows/capabilities → `cerebro/skills/`
- OpenClaw or system skills → `.skills/`

### 4. Respect source of truth
If a topic already has a clear home, update or read that file instead of creating a parallel note.

## Good usage examples
- Before working on Fluxia brand, read the relevant files in `cerebro/empresa/`.
- Before changing agent behavior, read `SOUL.md`, `STYLE.md`, and relevant agent docs.
- Before making new docs, check `SECOND-BRAIN-OPERATING-RULES.md`.

## Avoid

Do not:
- dump the entire second brain into context
- reread identity files unnecessarily
- create duplicate context docs when a source already exists
- confuse tasks with memory or strategy

## Recommended files
- `MAPA.md`
- `SECOND-BRAIN-OPERATING-RULES.md`
- `PRIORITIES.md`
- `TASKS.md`
- `cerebro/empresa/*`
- `cerebro/agents/*`
- `cerebro/areas/*`

## Reference

See `references/brain-routing.md` for quick routing logic.
