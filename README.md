# AstraNotes Final Defense Repository

AstraNotes is a local-running note-taking web application built for an AI-Driven Software Development final defense. The repository is both a working Flask MVP and an SDLC evidence package: requirements, planning, architecture, design, traceability, testing, security, deployment, maintenance, and AI-use documentation live beside the application code.

The project began in earlier course artifacts as a C++17 local-first desktop design. The final implementation intentionally pivots to a faster runnable Python/Flask/SQLite web MVP while preserving the product idea, MVC/separation-of-concerns principles, traceability discipline, testing strategy, and responsible AI review process.

## Final Tech Stack

- Python 3
- Flask
- SQLite
- HTML/CSS/Jinja templates
- pytest
- Local browser-based demo

## Implemented MVP Features

- FR-1: local user registration, login, logout, password hashing, and Flask sessions
- FR-2: create notes with title and content
- FR-3: list, view, and open only the current user's notes
- FR-4: edit the current user's notes without creating duplicates
- FR-5: delete the current user's notes with confirmation
- FR-6: search the current user's notes by title or content
- FR-7: user isolation across list, view, open, edit, delete, and search
- FR-8: Markdown-compatible content preserved exactly as typed for create, view, and edit

## Out Of Scope

The final MVP does not implement secure notes, production encryption, version history, cloud sync, OAuth, Docker, Kubernetes, enterprise administration, billing, mobile apps, AI summarization, collaborative editing, plugin systems, or advanced production deployment.

## Repository Structure

```text
AstraNotes/
  README.md
  AGENTS.md
  requirements.txt
  docs/
    01_REQUIREMENTS.md
    02_BACKLOG_AND_SPRINT_ZERO.md
    03_ARCHITECTURE_DECISIONS.md
    04_UML_AND_DESIGN.md
    05_TRACEABILITY.md
    06_TESTING_STRATEGY.md
    07_SECURITY_NOTES.md
    08_DEPLOYMENT_NOTES.md
    09_MAINTENANCE_NOTES.md
    10_AI_USAGE_AND_VALIDATION.md
    11_FINAL_PROJECT_SUMMARY.md
  demo/
    FINAL_DEMO_SCRIPT.md
  src/
    app.py
    db/
    models/
    repositories/
    routes/
    services/
    static/
    templates/
  tests/
    conftest.py
    feature/
    integration/
    unit/
```

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Initialize The Database

```powershell
flask --app src.app init-db
```

This creates the local SQLite database and applies `src/db/schema.sql`.

## Run The App

```powershell
flask --app src.app run
```

Open:

```text
http://127.0.0.1:5000
```

## Run Tests

```powershell
python -m pytest
```

Current status: 56 passing tests covering unit, integration, and feature/route behavior.

## Final Demo Video Focus

The recorded product demo should show the actual running app, not slides:

1. Briefly introduce the scope and Flask/SQLite pivot.
2. Register and log in.
3. Create, list, and view a note.
4. Edit the note and show Markdown-like content preservation.
5. Search notes by title/content.
6. Delete a note with confirmation.
7. Briefly show repository docs, traceability, and pytest results.
8. Close with AI-assisted development, human review, and out-of-scope items.

Use [demo/FINAL_DEMO_SCRIPT.md](demo/FINAL_DEMO_SCRIPT.md) for the 5-minute recording plan and manual verification checklist.

## Final Submission Artifacts

- GitHub repository link: submit the URL for this repository.
- Recorded product demo: approximately 5 minutes, showing the running Flask app.
- Repository evidence: documentation in `docs/`, working application code in `src/`, and pytest coverage in `tests/`.

## Instructor Review Path

1. Start with `docs/11_FINAL_PROJECT_SUMMARY.md`.
2. Review `docs/01_REQUIREMENTS.md` and `docs/05_TRACEABILITY.md`.
3. Review `docs/03_ARCHITECTURE_DECISIONS.md` and `docs/04_UML_AND_DESIGN.md`.
4. Review `docs/06_TESTING_STRATEGY.md`.
5. Review `docs/07_SECURITY_NOTES.md`, `docs/08_DEPLOYMENT_NOTES.md`, and `docs/09_MAINTENANCE_NOTES.md`.
6. Review `docs/10_AI_USAGE_AND_VALIDATION.md`.

## AI-Assisted Development Note

AI was used as a drafting, migration, implementation, and test-critique partner. Human review controlled the final stack decision, scope boundaries, feature sequencing, traceability updates, and rejection of unsupported features.
