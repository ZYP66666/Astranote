# 09 Maintenance Notes

## Purpose

This document describes how AstraNotes should remain maintainable after the final Flask MVP is implemented.

## Source Artifacts Used

- Working Agreement and Definition of Done
- Week 2.2 Backlog and Sprint Zero Plan
- Week 5.2 Requirements-to-UML Traceability Matrix
- Week 7.2 Testing Strategy and First Test Set

## Maintenance Principles

- Keep work small, reviewable, and traceable.
- Do not add impressive-sounding features without a requirement update.
- Keep routes thin and services responsible for workflow rules.
- Keep SQL inside repositories.
- Keep templates focused on presentation.
- Keep tests tied to requirements and acceptance criteria.
- Preserve clear error messages for validation and persistence failures.

## Current Project Structure

```text
src/
  app.py
  db/
  models/
  repositories/
  routes/
  services/
  static/
  templates/
tests/
  unit/
  integration/
  feature/
```

This structure supports the current Flask MVP and keeps routes, services, repositories, templates, and tests separated.

## Change Control

Before adding a feature:

1. Update requirements or backlog.
2. Add traceability entry.
3. Add or update tests.
4. Implement the smallest useful slice.
5. Review for scope drift.

## Deferred Feature Re-Entry Criteria

| Feature | Re-entry Criteria |
| --- | --- |
| Secure notes | Add threat model, encryption design, passphrase UX, and tests. |
| Version history | Define snapshot rules, restore workflow, and duplicate prevention. |
| Search refinement | Keep FR-6 as simple SQLite keyword search unless a new requirement justifies a dedicated index. |
| Markdown preview | Decide rendering library and escaping/safety rules. |
| Voice notes | Define storage format, upload limits, and playback UX. |
| Plugin system | Define extension interface and security boundaries. |

## Technical Debt Watchlist

- Routes becoming too large
- Authorization checks duplicated inconsistently
- SQL leaking into templates or route handlers
- Tests sharing real development data
- Deferred features appearing as half-built stubs
- Security claims overstating what the MVP actually does

## Migration From Old C++ Path

Migrated:

- Definition of Done
- Traceability-first maintenance
- Scope-control rules
- Test growth strategy

Updated:

- C++ module maintenance becomes Flask package maintenance
- Memory-management concerns are replaced by session, database, and authorization concerns
