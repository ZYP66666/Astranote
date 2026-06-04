# 06 Testing Strategy

## Purpose

This document adapts the Week 7.2 testing strategy to pytest and the Flask MVP. The original testing principle remains: start with small, requirement-backed tests that validate the core note workflow before expanding into future features.

## Source Artifacts Used

- Week 7.2 Testing Strategy and First Test Set
- Week 6 Development Environment and First Realization Slices
- Week 5.2 Requirements-to-UML Traceability Matrix
- Working Agreement and Definition of Done

## Testing Approach

Testing will be shift-left and incremental. The first implemented tests validate FR-1 local authentication and the Flask/SQLite skeleton. Later tests should expand into note behavior one feature slice at a time.

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
| Unit tests | Validate service validation rules without full UI. | Auth validation now; note validation later. |
| Repository tests | Validate SQLite interactions using temporary databases. | User create/find now; note insert/list/search later. |
| Route tests | Validate Flask request/response workflows. | Register/login/logout now; note workflows later. |
| Feature/demo checks | Validate visible user workflows. | Final demo script walkthrough. |
| AI-native critique | Ask AI to suggest missing edge cases, then review manually. | Invalid input, unauthorized access, storage failures. |

## Current FR-1 pytest Coverage

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

## Future pytest Test Set

| Test ID | Feature | Level | Expected Result |
| --- | --- | --- | --- |
| T1 | FR-2 create note validation | Unit/service | Blank title is rejected with clear message. |
| T2 | FR-2 create note success | Unit/service or repository | Valid note gets ID, user ID, title, content, timestamps. |
| T3 | FR-8 Markdown preservation | Repository/integration | Markdown text reloads exactly as saved. |
| T4 | FR-3 list notes | Repository/route | Current user sees only their notes. |
| T5 | FR-7 user isolation | Service/route | User A cannot access User B's notes. |
| T6 | FR-3 open saved note | Repository/route | Saved note opens with correct title/content. |
| T7 | FR-4 edit note | Service/route | Existing note updates without duplicate record. |
| T8 | FR-5 delete note | Route/repository | Confirmed delete removes the note. |
| T9 | FR-6 search notes | Service/repository/route | Search results are scoped to current user. |
| T10 | Invalid create workflow | Route | Validation message shown and content is not silently lost. |
| T11 | Temporary DB safety | Test infrastructure | Tests do not read/write real development data. |

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
