# 10 AI Usage And Validation

## Purpose

This document explains how AI contributed to AstraNotes and how human review controlled the final project direction.

## Source Artifacts Used

- Working Agreement and Definition of Done
- Architecture Decision Log
- Week 2.2 Backlog and Sprint Zero Plan
- Week 5.2 Requirements-to-UML Traceability Matrix
- Week 6 Development Environment and First Realization Slices
- Week 7.2 Testing Strategy and First Test Set

## AI Working Agreement Summary

The project treats AI as a drafting and critique partner, not as an unquestioned authority.

Key rules:

- AI output must be explainable in the student's own words.
- AI-generated ideas must fit the current project direction.
- Polished but vague output should be challenged or discarded.
- Requirements, traceability, architecture, and Definition of Done remain human-owned.
- New features must connect to real AstraNotes objectives.

## How AI Helped

AI helped draft or critique:

- User stories and acceptance criteria
- Backlog structure
- Architecture options
- UML responsibility mapping
- Traceability matrix wording
- First implementation slice selection
- Testing strategy and edge cases
- Migration from C++ desktop direction to Flask web MVP

## Human Validation Actions

The final package reflects several human-controlled decisions:

- The final implementation stack is Python/Flask/SQLite/pytest, even though old PDFs selected C++17.
- Secure notes, voice notes, version history, cloud sync, and plugin systems were deferred.
- The earlier weak SearchIndex idea was narrowed into final FR-6: simple SQLite keyword search over the current user's notes.
- The app remains local-running and reviewable rather than becoming cloud/enterprise-heavy.
- Testing remains focused on requirement behavior rather than UI decoration.
- Basic multi-user support was added because the final implementation prompt requires it.

## AI Suggestions Rejected Or Deferred

| Suggestion Area | Decision | Reason |
| --- | --- | --- |
| Cloud sync | Rejected for MVP | Explicitly out of scope. |
| OAuth | Rejected for MVP | Too large for local demo. |
| Secure-note encryption | Deferred | Important but explicitly not implemented now. |
| Voice notes | Deferred | Future extension only. |
| Full plugin system | Deferred | Overbuilt for MVP. |
| Dedicated SearchIndex | Deferred | Search is now a scoped MVP requirement, but should be implemented later as simple SQLite search. |
| UI color/layout tests | Rejected as first tests | Noisy and not core requirement behavior. |

## Validation Checklist

Before final coding is considered done:

- Requirements map to implemented routes/services/tests.
- Deferred features are not half-implemented.
- pytest passes.
- Demo script can be followed from a fresh local run.
- The final summary explains the implementation pivot honestly.
- Security notes do not overclaim production readiness.

## Migration From Old C++ Path

Migrated:

- AI as drafting partner
- Human judgment as final authority
- Traceability and explainability rules
- Rejection of scope drift

Updated:

- AI validation now checks fit against Python/Flask, not C++17/CMake
- Test critique now targets pytest and Flask client workflows
