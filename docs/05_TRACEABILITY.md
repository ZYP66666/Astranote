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
| FR-1 Register/login | Story 0 | User, AuthService, UserRepository, Flask session | `/auth/register`, `/auth/login`, `/auth/logout` | Validation, duplicate username, password hash, valid/invalid login, route flow | Implemented |
| FR-2 Create note | Story 1 | Note, NoteService, NoteRepository | `/notes/new`, SQLite insert | Reject blank title, create valid note | Implemented |
| FR-3 List/view/open own notes | Story 2 | NoteService, NoteRepository, notes templates | `/notes/`, `/notes/<id>` | List only current user's notes, open saved note | Implemented |
| FR-4 Edit own notes | Story 3 | NoteService update path | `/notes/<id>/edit` | Update without duplicate, preserve ownership | Implemented |
| FR-5 Delete own notes | Story 4 | NoteService delete path | `/notes/<id>/delete` | Confirm delete, cancel leaves note | Implemented |
| FR-6 Search own notes | Story 7 | NoteService search path, NoteRepository query | `/notes/?q=keyword` | Search title/content and scope to current user | Implemented |
| FR-7 Block cross-user note access | Story 6 | AuthService session, NoteService ownership checks | All note routes and repository queries | User A cannot access User B's notes | Implemented for list/view/open/edit/delete/search |
| FR-8 Markdown preservation | Story 5 | Note content field | Textarea and SQLite text column | Markdown saved/reloaded exactly | Implemented for create/view/edit |
| GR1 MVC separation | All stories | Routes, services, repositories, templates | App package structure | Service/repository tests avoid UI dependency | Implemented |
| RR1-FLASK pytest validation | All stories | pytest suite | `tests/` | Unit, integration, route tests | Auth, create/list/view/edit/delete/search notes, smoke, and database baseline implemented |

## Deferred Traceability Items

| Original Requirement | Final Decision | Reason |
| --- | --- | --- |
| Original multiple note types | Defer | Text notes only for MVP. |
| SPR1 encrypted secure notes | Defer | Real encryption is explicitly out of scope. |
| SPR2 passphrase unlock | Defer | Secure notes are not part of MVP. |
| Original version history/restore | Defer | Useful but not required for final runnable MVP. |
| Dedicated SearchIndex | Defer | FR-6 is implemented with simple SQLite keyword search, not a separate search-index subsystem. |
| Voice Notes | Defer | Future extension only. |

## Traceability Rules For Implementation

- Every route should map to at least one user story.
- Every user-facing workflow should have at least one pytest or demo-script validation step.
- Every repository method should have a clear requirement reason.
- Deferred requirements should not appear as half-built code.
- New scope should be added only after updating requirements and traceability.

## Implementation Status Note

The current codebase has a runnable Flask app, implemented FR-1 auth routes, session handling, user persistence, password hashing, FR-2 note creation, FR-3 own-note list/view/open behavior, FR-4 edit own notes, FR-5 confirmed note deletion, FR-6 user-scoped search, SQLite schema initialization, service/repository ownership checks for notes, and pytest coverage for the implemented auth and note slices.

## Migration From Old C++ Path

Migrated:

- Requirement IDs and user story structure
- Fully traced original create-note and local persistence emphasis
- Partial-trace warnings for failure behavior and deferred features
- Gold-plating warning about SearchIndex

Updated:

- UML evidence becomes web design evidence
- Google Test evidence becomes pytest evidence
- Local deployment evidence becomes local Flask + SQLite evidence
- UserSession becomes Flask session and local account ownership
