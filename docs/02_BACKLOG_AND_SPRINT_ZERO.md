# 02 Backlog And Sprint Zero

## Purpose

This document adapts the Week 2.2 backlog and Sprint Zero plan to the final Flask/SQLite realization path. It keeps the original traceability chain:

Requirements -> User Stories -> Acceptance Criteria -> Backlog -> Sprint Zero Plan

## Source Artifacts Used

- Week 2.2 Backlog and Sprint Zero Plan
- Initial Requirement Set
- Week 6 Development Environment and First Realization Slices
- Working Agreement and Definition of Done

## Updated User Stories And Acceptance Criteria

### User Story 1: Create A Note

As a logged-in user, I want to create a note with a title and content so that I can capture information quickly.

Acceptance criteria:

- The user can open a new-note page.
- The user can enter title and content.
- The note is saved to SQLite.
- The note appears in the user's note list.
- A blank title shows a validation message without silently losing content.

### User Story 2: Open And View A Note

As a logged-in user, I want to open a saved note so that I can review previous work.

Acceptance criteria:

- The app lists notes owned by the current user.
- Selecting a note shows the saved title and content.
- A user cannot open another user's note.
- Missing or unauthorized notes produce a controlled response.

### User Story 3: Edit And Save A Note

As a logged-in user, I want to edit an existing note so that my notes stay current.

Acceptance criteria:

- The user can update title and content.
- Saving updates the existing note rather than creating an accidental duplicate.
- Reopening the note shows the latest saved content.
- Ownership and timestamps remain consistent.

### User Story 4: Delete A Note Safely

As a logged-in user, I want to delete a note only after confirmation so that I do not remove important content accidentally.

Acceptance criteria:

- Existing notes have a delete action.
- The delete page or form requires confirmation.
- Canceling leaves the note unchanged.
- Confirming removes only that user's selected note.

### User Story 5: Preserve Markdown Text

As a user writing technical notes, I want Markdown syntax preserved so that headings, bullets, bold text, and inline code survive save/reopen cycles.

Acceptance criteria:

- Markdown is accepted as plain text input.
- Markdown is stored and reloaded exactly.
- Markdown handling is not tightly coupled to template rendering.

### User Story 6: Basic Local Multi-User Support

As a local user, I want my own account so that my notes are separated from other local demo users.

Acceptance criteria:

- A user can register with username and password.
- A user can log in and log out.
- Passwords are hashed.
- Every note query is scoped to the current user.

## Prioritized Backlog

### Priority 1: Must Do First

1. Flask project skeleton with app factory and configuration
2. SQLite schema for users and notes
3. Repository layer for users and notes
4. Service layer for validation and ownership checks
5. Registration, login, and logout flow
6. Create/list/open note workflow

### Priority 2: Core MVP Completion

7. Edit existing note workflow
8. Delete with confirmation workflow
9. Jinja templates and CSS for a usable local demo
10. Flash messages for validation and errors
11. pytest coverage for service, repository, and route behavior

### Priority 3: Polish And Defense Readiness

12. Seed/demo data helper if needed
13. Final demo script execution check
14. Deployment notes and environment instructions
15. Traceability review against final requirements

## Updated Sprint Zero Plan

Sprint Zero goal: prepare a small, testable Flask application foundation that can deliver the first note workflow without scope drift.

Sprint Zero deliverables:

- Confirm Python/Flask/SQLite/pytest stack
- Create repository layout for app, templates, static assets, tests, and docs
- Define SQLite schema
- Define MVC/separation boundaries
- Define first test targets
- Confirm no deferred feature is accidentally implemented early

## Migration From Old C++ Path

Migrated:

- Small, reviewable work slices
- Create/open/save as the first meaningful vertical slice
- Local persistence as a central risk
- Validation and clear error messages
- Traceable backlog discipline

Updated:

- C++ project setup becomes Flask app setup
- Google Test setup becomes pytest setup
- Desktop UI shell becomes browser-based Jinja templates
- Single local user becomes basic local accounts
