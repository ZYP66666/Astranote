# 06 Testing Strategy

## Purpose

This document adapts the Week 7.2 testing strategy to pytest and the Flask MVP. The original testing principle remains: start with small, requirement-backed tests that validate the core note workflow before expanding into future features.

## Source Artifacts Used

- Week 7.2 Testing Strategy and First Test Set
- Week 6 Development Environment and First Realization Slices
- Week 5.2 Requirements-to-UML Traceability Matrix
- Working Agreement and Definition of Done

## Testing Approach

Testing will be shift-left and incremental. The first tests should validate the smallest useful behaviors:

- Register/login/logout
- Create a text note
- Save it to SQLite
- List saved notes
- Open a saved note
- Edit a saved note
- Delete a saved note
- Preserve Markdown text
- Enforce user ownership

## Testing Levels

| Level | Purpose | First Targets |
| --- | --- | --- |
| Unit tests | Validate service validation rules without full UI. | Blank title, Markdown preservation, ownership checks. |
| Repository tests | Validate SQLite interactions using temporary databases. | Insert, list, find, update, delete notes. |
| Route tests | Validate Flask request/response workflows. | Login required, create note, open note, edit note, delete note. |
| Feature/demo checks | Validate visible user workflows. | Final demo script walkthrough. |
| AI-native critique | Ask AI to suggest missing edge cases, then review manually. | Invalid input, unauthorized access, storage failures. |

## First pytest Test Set

| Test ID | Feature | Level | Expected Result |
| --- | --- | --- | --- |
| T1 | Create note validation | Unit/service | Blank title is rejected with clear message. |
| T2 | Create note success | Unit/service or repository | Valid note gets ID, user ID, title, content, timestamps. |
| T3 | Markdown preservation | Repository/integration | Markdown text reloads exactly as saved. |
| T4 | List notes | Repository/route | Current user sees their notes. |
| T5 | User isolation | Service/route | User A cannot access User B's notes. |
| T6 | Open saved note | Repository/route | Saved note opens with correct title/content. |
| T7 | Edit note | Service/route | Existing note updates without duplicate record. |
| T8 | Delete note | Route/repository | Confirmed delete removes the note. |
| T9 | Login required | Route | Anonymous user is redirected or blocked from note pages. |
| T10 | Register/login/logout | Route | Local account workflow succeeds. |
| T11 | Invalid create workflow | Route | Validation message shown and content is not silently lost. |
| T12 | Temporary DB safety | Test infrastructure | Tests do not read/write real development data. |

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
