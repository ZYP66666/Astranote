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

The current implementation supports FR-1 registration/login/logout, FR-2 note creation, FR-3 list/view/open own notes, FR-4 edit own notes, and FR-5 delete own notes with confirmation. Search demo steps will become executable after a later implementation slice.

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

- FR-1 registration/login
- SPR-MVP local privacy boundary

### 4. Create A Note

Action:

- Open New Note.
- Enter a title.
- Enter Markdown content such as a heading, bullet list, bold text, and inline code.
- Save the note.

Expected result:

- Note is saved.
- The app redirects to the saved note detail page.
- The note appears in the user's list.

Requirement evidence:

- FR-2 create note
- FR-8 Markdown preservation

### 5. Open The Saved Note

Action:

- Select the note from the list.

Expected result:

- Correct title and content are displayed.

Requirement evidence:

- FR-3 list/view/open own notes

### 6. Edit The Note

Action:

- Edit the title or content.
- Save changes.
- Reopen the note.

Expected result:

- Updated content appears.
- No duplicate note is created.
- Markdown-like text remains exactly as typed.

Requirement evidence:

- FR-4 edit own notes

### 7. Delete The Note

Action:

- Use delete action.
- Confirm deletion.

Expected result:

- Note is removed from the user's list.
- Opening the deleted note returns a controlled not-found response.

Requirement evidence:

- FR-5 delete own notes with confirmation

### 8. Search Notes

Action:

- Search for a keyword in the user's own note title or content.

Expected result:

- Matching notes owned by the current user are shown.
- Notes owned by other users are not shown.

Requirement evidence:

- FR-6 search own notes
- FR-7 cross-user note isolation

### 9. Demonstrate User Isolation

Action:

- Create a second user.
- Confirm the second user cannot see the first user's notes.

Expected result:

- Note list is scoped to current user.

Requirement evidence:

- FR-7 cross-user note isolation
- Security notes

### 10. Show Tests

Action:

- Run pytest.

Expected result:

- Tests pass for auth, note CRUD, Markdown preservation, and ownership checks.
- At this stage, search tests are still future work.

Requirement evidence:

- RR1-FLASK pytest validation

### 11. Close With Scope Control

Explain deferred items:

- Secure notes
- Voice notes
- Version history
- Cloud sync
- OAuth
- AI summarization
- Collaborative editing

Closing message:

AstraNotes demonstrates a complete AI-assisted SDLC path and a focused final MVP rather than uncontrolled feature expansion.
