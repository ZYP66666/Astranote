# 06 Testing Strategy

## Purpose

This document adapts the Week 7.2 testing strategy to pytest and the Flask MVP. The original testing principle remains: start with small, requirement-backed tests that validate the core note workflow before expanding into future features.

## Source Artifacts Used

- Week 7.2 Testing Strategy and First Test Set
- Week 6 Development Environment and First Realization Slices
- Week 5.2 Requirements-to-UML Traceability Matrix
- Working Agreement and Definition of Done

## Testing Approach

Testing is shift-left and incremental. The current implemented tests validate FR-1 local authentication, FR-2 note creation, FR-3 list/view/open own notes, FR-4 edit own notes, FR-5 delete own notes, FR-6 search own notes, and the Flask/SQLite skeleton.

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
| Unit tests | Validate service validation rules without full UI. | Auth validation and note create/open/edit/delete/search ownership. |
| Repository tests | Validate SQLite interactions using temporary databases. | User create/find and note create/list/find/update/delete/search. |
| Route tests | Validate Flask request/response workflows. | Register/login/logout and create/list/view/edit/delete/search notes. |
| Feature/demo checks | Validate visible user workflows. | Final demo script walkthrough. |
| AI-native critique | Ask AI to suggest missing edge cases, then review manually. | Invalid input, unauthorized access, storage failures. |

## Current FR-1 Through FR-6 pytest Coverage

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
| NoteService edit validation | Empty edit title is rejected with a clear message. |
| NoteService edit success | Existing owner note updates title and content. |
| NoteRepository update | Title, content, and `updated_at` update without creating a duplicate note. |
| Edit ownership | User A cannot edit User B's note through repository, service, or route behavior. |
| Edit route workflow | Logged-in users can open a prefilled edit form and save changes. |
| Markdown-like edit content | Content such as `# Updated` and `- item` is preserved exactly after edit. |
| NoteRepository delete | Owner-scoped delete removes the note from SQLite. |
| NoteService delete | Owner delete succeeds and wrong-user delete fails. |
| Delete confirmation route | Logged-in users can reach a confirmation page for their own note. |
| Confirmed delete route | POST delete removes the note and redirects to the notes list. |
| Deleted note detail | Opening a deleted note returns a controlled 404-style response. |
| Delete ownership | User A cannot delete User B's note through repository, service, or route behavior. |
| NoteRepository search | Title/content keyword search returns only current user's notes. |
| NoteService search | Search workflow returns user-scoped results. |
| Empty search | Empty query returns all notes for the current user. |
| No-match search | No matches show a clear empty-state message. |
| Search route | Logged-in users can search by title or content. |
| Search ownership | User A cannot discover User B's notes through search. |

## Future pytest Ideas

| Test ID | Feature | Level | Expected Result |
| --- | --- | --- | --- |
| T1 | Regression after UI polish | Route/feature | Core auth and note workflows remain intact. |
| T2 | Optional edge cases | Service/repository | Special characters in search do not break user-scoped results. |

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
