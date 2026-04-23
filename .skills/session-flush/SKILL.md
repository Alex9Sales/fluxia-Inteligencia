---
name: session-flush
description: Close a work session cleanly by deciding what should be saved, what should update existing docs, and what should remain unsaved. Use near the end of meaningful work, before context compaction, or when preserving decisions, progress, blockers, and next steps in the project second-brain.
---

# Session Flush

Use this skill to preserve the right things at the end of a session without turning every conversation into documentation noise.

## Goal

Capture what matters from a session so future work starts cleaner.

## Flush order

### 1. Review what actually changed
Check for:
- decisions
- new priorities
- completed work
- blockers
- important new context
- new docs or skills created
- next steps worth preserving

### 2. Decide where each item belongs
Use these destinations:
- durable business or personal context → `MEMORY.md`
- daily session continuity → `memory/YYYY-MM-DD.md`
- strategic focus shifts → `PRIORITIES.md`
- execution queue changes → `TASKS.md`
- domain-specific updates → relevant file under `cerebro/`
- reusable skill workflow change → relevant file under `.skills/`

### 3. Do not save noise
Do not flush:
- every message summary
- trivial back-and-forth
- duplicate context that already exists elsewhere
- generic “we talked about X” notes with no future value

### 4. Keep it concrete
Good flush items are:
- what was decided
- what changed
- what remains open
- what future-you must remember

## Git hygiene
When meaningful edits were made, commit with a message that reflects the actual change.
Avoid vague commit messages when a clearer one is easy.

## Recommended pattern
A good session flush usually means:
1. update the right docs
2. update daily memory if continuity matters
3. commit changes if real work was done

## Avoid

Do not:
- create new files when existing files are the right home
- over-document trivial work
- treat flush as mandatory for every tiny exchange
- mix strategic memory with temporary execution clutter

## Reference

See `references/flush-checklist.md` for a compact checklist.
