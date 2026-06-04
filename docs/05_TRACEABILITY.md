# 05 Traceability

## Purpose

This document preserves the traceability discipline from the course artifacts while updating the implementation target to Flask, SQLite, and pytest.

## Source Artifacts Used

- Week 5.2 Requirements-to-UML Traceability Matrix
- Initial Requirement Set
- Week 2.2 Backlog and Sprint Zero Plan
- Week 4.2 UML Design Package
- Week 7.2 Testing Strategy and First Test Set

## Final MVP Traceability Matrix

| Requirement | User Story | Design Element | Implementation Target | Test Target | Status |
| --- | --- | --- | --- | --- | --- |
| FR1 Create note | Story 1 | Note, NoteService, NoteRepository | `/notes/new`, SQLite insert | Reject blank title, create valid note | Scaffolded route/template only |
| FR2 Open/view note | Story 2 | NoteService, NoteRepository, note detail template | `/notes/<id>` | Open saved note, block unauthorized note | Scaffolded notes workspace only |
| FR3 Edit note | Story 3 | NoteService update path | `/notes/<id>/edit` | Update without duplicate, preserve ownership | Planned |
| FR4 Delete note | Story 4 | NoteService delete path | `/notes/<id>/delete` | Confirm delete, cancel leaves note | Planned |
| FR5 Markdown preservation | Story 5 | Note content field | Textarea and SQLite text column | Markdown saved/reloaded exactly | Scaffolded form field/schema only |
| FR7 Local persistence | Stories 1-3 | SQLite database, repositories | `users` and `notes` tables | Data persists across app context/reload | Schema/init scaffolded |
| FR9 Basic multi-user | Story 6 | User, AuthService, Flask session | Register/login/logout routes | User A cannot access User B notes | Scaffolded forms/schema only |
| GR1 MVC separation | All stories | Routes, services, repositories, templates | App package structure | Service/repository tests avoid UI dependency | Skeleton implemented |
| RR1-FLASK pytest validation | All stories | pytest suite | `tests/` | Unit, integration, route tests | Smoke/database baseline implemented |

## Deferred Traceability Items

| Original Requirement | Final Decision | Reason |
| --- | --- | --- |
| FR6 multiple note types | Defer | Text notes only for MVP. |
| SPR1 encrypted secure notes | Defer | Real encryption is explicitly out of scope. |
| SPR2 passphrase unlock | Defer | Secure notes are not part of MVP. |
| FR8 version history/restore | Defer | Useful but not required for final runnable MVP. |
| SearchIndex/Search Notes | Defer or remove | Earlier traceability identified this as weakly justified. |
| Voice Notes | Defer | Future extension only. |

## Traceability Rules For Implementation

- Every route should map to at least one user story.
- Every user-facing workflow should have at least one pytest or demo-script validation step.
- Every repository method should have a clear requirement reason.
- Deferred requirements should not appear as half-built code.
- New scope should be added only after updating requirements and traceability.

## Skeleton Implementation Note

The current codebase has a runnable Flask app, registered auth and notes blueprints, Jinja placeholder pages, SQLite schema initialization, service/repository placeholders, and skeleton-level pytest coverage. Full register/login and note CRUD behavior is intentionally not implemented yet.

## Migration From Old C++ Path

Migrated:

- Requirement IDs and user story structure
- Fully traced FR1 and FR7 emphasis
- Partial-trace warnings for open failure behavior, edit behavior, and deferred features
- Gold-plating warning about SearchIndex

Updated:

- UML evidence becomes web design evidence
- Google Test evidence becomes pytest evidence
- Local deployment evidence becomes local Flask + SQLite evidence
- UserSession becomes Flask session and local account ownership
