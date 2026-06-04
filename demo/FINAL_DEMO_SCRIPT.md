# Final Demo Script

## Purpose

This script describes the planned final AstraNotes demonstration after implementation is complete. It is written now so coding can stay aligned to the defense goals.

## Source Artifacts Used

- Week 2.2 Backlog and Sprint Zero Plan
- Week 6 Development Environment and First Realization Slices
- Week 7.2 Testing Strategy and First Test Set
- Final Flask MVP migration decision

## Demo Setup

1. Start from the repository root.
2. Install Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Initialize the SQLite database:

```powershell
flask --app src.app init-db
```

4. Run the Flask development server:

```powershell
flask --app src.app run
```

5. Open the app in a browser:

```text
http://127.0.0.1:5000
```

6. Run pytest before or after the manual demo:

```powershell
python -m pytest
```

The current implementation is a skeleton. Full registration, login, and note CRUD demo steps will become executable after later implementation slices.

## Demo Walkthrough

### 1. Introduce The Project

Explain:

- AstraNotes began as a C++17 local-first desktop design.
- The final implementation pivoted to Flask for a faster runnable MVP.
- The SDLC artifacts were preserved and migrated rather than discarded.

### 2. Show Documentation Structure

Open:

- `README.md`
- `docs/01_REQUIREMENTS.md`
- `docs/05_TRACEABILITY.md`
- `docs/06_TESTING_STRATEGY.md`
- `docs/11_FINAL_PROJECT_SUMMARY.md`

Point out how requirements, design, tests, and implementation scope connect.

### 3. Register A User

Action:

- Open the register page.
- Create a demo user.

Expected result:

- User account is created.
- User is logged in or redirected to login.

Requirement evidence:

- FR9 basic multi-user support
- SPR-MVP local privacy boundary

### 4. Create A Note

Action:

- Open New Note.
- Enter a title.
- Enter Markdown content such as a heading, bullet list, bold text, and inline code.
- Save the note.

Expected result:

- Note is saved.
- Note appears in the user's list.

Requirement evidence:

- FR1 create note
- FR5 Markdown preservation
- FR7 local persistence

### 5. Open The Saved Note

Action:

- Select the note from the list.

Expected result:

- Correct title and content are displayed.

Requirement evidence:

- FR2 open/view note

### 6. Edit The Note

Action:

- Edit the title or content.
- Save changes.
- Reopen the note.

Expected result:

- Updated content appears.
- No duplicate note is created.

Requirement evidence:

- FR3 edit note

### 7. Delete The Note

Action:

- Use delete action.
- Confirm deletion.

Expected result:

- Note is removed from the user's list.

Requirement evidence:

- FR4 delete note with confirmation

### 8. Demonstrate User Isolation

Action:

- Create a second user.
- Confirm the second user cannot see the first user's notes.

Expected result:

- Note list is scoped to current user.

Requirement evidence:

- FR9 basic multi-user support
- Security notes

### 9. Show Tests

Action:

- Run pytest.

Expected result:

- Tests pass for auth, note CRUD, Markdown preservation, and ownership checks.

Requirement evidence:

- RR1-FLASK pytest validation

### 10. Close With Scope Control

Explain deferred items:

- Secure notes
- Voice notes
- Version history
- Search
- Cloud sync
- OAuth
- AI summarization
- Collaborative editing

Closing message:

AstraNotes demonstrates a complete AI-assisted SDLC path and a focused final MVP rather than uncontrolled feature expansion.
