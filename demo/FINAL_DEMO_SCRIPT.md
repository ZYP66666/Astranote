# Final Demo Script

## Purpose

Use this script to record an approximately 5-minute final product demo for AstraNotes. The video should show the actual running Flask application, not slides.

## Setup Before Recording

From the repository root:

```powershell
python -m pip install -r requirements.txt
flask --app src.app init-db
flask --app src.app run
```

Open:

```text
http://127.0.0.1:5000
```

Run tests before recording:

```powershell
python -m pytest
```

## 5-Minute Recording Flow

### 0:00-0:30 Project Intro And Scope

Show the app home page.

Say:

- AstraNotes is a local-running Flask and SQLite note-taking MVP.
- The project began as a C++17 desktop design, then pivoted to Python/Flask for the final runnable demo.
- The MVP focuses on local accounts, user-owned notes, Markdown-compatible text preservation, and pytest validation.
- Out of scope: secure notes, cloud sync, OAuth, version history, AI summarization, collaborative editing, and enterprise features.

### 0:30-1:15 Register And Log In

Show:

- Register page
- Create a demo user
- Login page
- Successful login and navigation showing the signed-in user

Requirements shown:

- FR-1 registration/login
- Basic session handling

### 1:15-2:15 Create, List, And View A Note

Show:

- Create Note page
- Enter a title
- Enter Markdown-like content, for example:

```text
# Sprint Review
- confirm Flask routes
- run pytest
```

- Save the note
- Open the notes list
- Open the saved note detail page

Requirements shown:

- FR-2 create note
- FR-3 list/view/open own notes
- FR-8 Markdown-compatible content preservation

### 2:15-3:00 Edit Note

Show:

- Click Edit from the detail page
- Update the title or content
- Save changes
- Show the updated note detail page

Point out:

- Editing updates the existing note rather than creating a duplicate.
- Markdown-like text remains exactly as typed.

Requirements shown:

- FR-4 edit own notes
- FR-8 preservation on edit

### 3:00-3:40 Search Notes

Show:

- Return to the notes list
- Search for a word in the title
- Search for a word in the content
- Search for a no-match term and show the empty state
- Clear the search to show all of the current user's notes again

Requirements shown:

- FR-6 search own notes
- FR-7 user isolation through user-scoped results

### 3:40-4:10 Delete Note With Confirmation

Show:

- Open a note detail page
- Click Delete
- Show the confirmation screen
- Cancel briefly if desired, then return and confirm delete
- Show the note removed from the list

Requirements shown:

- FR-5 delete own notes with confirmation

### 4:10-4:40 Show Repository Evidence

Briefly show the repository structure:

- `src/` for Flask app code
- `tests/` for unit, integration, and feature tests
- `docs/` for SDLC evidence
- `docs/05_TRACEABILITY.md`
- `docs/06_TESTING_STRATEGY.md`

Show pytest result:

```text
56 passed
```

### 4:40-5:00 AI Use, Human Review, And Close

Show `docs/10_AI_USAGE_AND_VALIDATION.md` or summarize it.

Say:

- AI helped draft, migrate, critique, and implement, but the final stack, scope, tests, and traceability decisions were human-reviewed.
- Deferred features were intentionally kept out to protect scope and make the MVP defensible.
- The repository demonstrates a full SDLC path and a working local web application.

## Manual Demo Verification Checklist

Before recording, verify:

- [ ] `flask --app src.app init-db` succeeds
- [ ] `flask --app src.app run` starts the app
- [ ] Home page loads at `http://127.0.0.1:5000`
- [ ] Register works
- [ ] Login works
- [ ] Create note works
- [ ] Notes list shows the created note
- [ ] Note detail page opens
- [ ] Edit note works
- [ ] Markdown-like text remains exactly as typed
- [ ] Search by title works
- [ ] Search by content works
- [ ] No-match search shows a clear empty state
- [ ] Delete confirmation page appears
- [ ] Confirmed delete removes the note
- [ ] Logout works
- [ ] A second user cannot see the first user's notes
- [ ] `python -m pytest` passes

## Recording Tips

- Keep the browser and terminal side by side only when showing tests.
- Use one simple demo account and two or three short notes.
- Do not spend time on deferred features; name them briefly near the end.
- Keep the video focused on the working product.
