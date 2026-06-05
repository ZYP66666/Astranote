# 06 Testing Strategy

## Purpose

This document adapts the Week 7.2 testing strategy to pytest and the Flask MVP. The original testing principle remains: start with small, requirement-backed tests that validate the core note workflow before expanding into future features.

## Source Artifacts Used

- Week 7.2 Testing Strategy and First Test Set
- Week 6 Development Environment and First Realization Slices
- Week 5.2 Requirements-to-UML Traceability Matrix
- Working Agreement and Definition of Done

## Testing Approach

Testing will be shift-left and incremental. The current implemented tests validate FR-1 local authentication, FR-2 note creation, the first part of FR-3 list/view/open own notes, and the Flask/SQLite skeleton. Later tests should expand into edit, delete, and search one feature slice at a time.

- Register/login/logout
- Create a text note
- Save it to SQLite
- List saved notes
- Open a saved note
- Edit a saved note
- Delete a saved note
- Search own notes
- Preserve Markdown text
- Enforce user ownership

## Testing Levels

| Level | Purpose | First Targets |
| --- | --- | --- |
| Unit tests | Validate service validation rules without full UI. | Auth validation and note create/open ownership now; edit/delete/search later. |
| Repository tests | Validate SQLite interactions using temporary databases. | User create/find and note create/list/find now; search later. |
| Route tests | Validate Flask request/response workflows. | Register/login/logout and create/list/view notes now; edit/delete/search later. |
| Feature/demo checks | Validate visible user workflows. | Final demo script walkthrough. |
| AI-native critique | Ask AI to suggest missing edge cases, then review manually. | Invalid input, unauthorized access, storage failures. |

## Current FR-1 Through FR-3 pytest Coverage

| Test Area | Expected Result |
| --- | --- |
| AuthService empty username | Registration fails with a clear message. |
| AuthService empty password | Registration fails with a clear message. |
| UserRepository create/find | Created users can be retrieved from SQLite. |
| Duplicate username | Duplicate registration is rejected clearly. |
| Password storage | Stored password is a hash, not plaintext. |
| Valid login | Correct credentials authenticate successfully. |
| Invalid login | Wrong password returns a clear failure. |
| Register/login/logout route flow | Session is created on login and cleared on logout. |
| Protected notes workspace | Logged-out users are redirected to login. |
| NoteService empty title | Note creation fails with a clear message. |
| NoteService valid create | A note is created for the current user. |
| NoteRepository create/find | A note can be saved and retrieved by ID and user ID. |
| NoteRepository list by user | A user sees only their own notes. |
| Note ownership | Another user's note is not returned by service/repository/view route. |
| Note route create/list/view | Logged-in users can create, list, and open their own notes. |
| Markdown-like content | Content such as `# Title` and `- item` is preserved exactly as typed. |

## Future pytest Test Set

| Test ID | Feature | Level | Expected Result |
| --- | --- | --- | --- |
| T1 | FR-4 edit note | Service/route | Existing note updates without duplicate record. |
| T2 | FR-5 delete note | Route/repository | Confirmed delete removes the note. |
| T3 | FR-6 search notes | Service/repository/route | Search results are scoped to current user. |
| T4 | FR-7 user isolation | Service/route | Edit/delete/search cannot access another user's notes. |
| T5 | FR-8 Markdown preservation on edit | Repository/integration | Edited Markdown text reloads exactly as saved. |

## pytest Fixtures Needed Later

- Temporary SQLite database fixture
- Flask app fixture using test configuration
- Test client fixture
- User factory/helper
- Logged-in client helper
- Note factory/helper

## Testing Guardrails

- Do not test UI styling details as core behavior.
- Do not add tests for secure notes, voice notes, cloud sync, or version history until those features are scoped.
- Do not let tests depend on a real local database file.
- Use clear assertions tied to requirements and acceptance criteria.

## Migration From Old C++ Path

Migrated:

- Test-first/shift-left mindset
- First focus on create/save/list/open
- Storage failure and validation awareness
- Human review of AI-suggested tests

Updated:

- Google Test names become pytest test functions
- Temporary storage folder becomes temporary SQLite database
- Feature-level checks become Flask client tests and final demo walkthrough
