# AstraNotes Final Defense Repository

AstraNotes is a local-running note-taking MVP created for an AI-Driven Software Development course. This repository preserves the project's SDLC journey and now includes the first runnable Python/Flask skeleton for the final implementation path.

The original course artifacts explored a C++17 local-first desktop direction. The final realization has pivoted to a faster runnable local web MVP while preserving the product idea, requirements intent, MVC principles, traceability discipline, testing strategy, responsible AI practices, and Definition of Done.

## Final Tech Stack

- Python 3
- Flask
- SQLite
- HTML/CSS/Jinja templates
- pytest
- Local-running web application
- Basic multi-user support planned
- Simple MVC / separation-of-concerns architecture

## Current Implementation Status

This step creates the runnable Flask skeleton only. It does not yet implement registration, login, create note, edit note, delete note, search, secure notes, version history, cloud sync, OAuth, Docker, Kubernetes, enterprise admin, AI summarization, or collaborative editing.

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
    models/
    routes/
    services/
    repositories/
    db/
    templates/
    static/
  tests/
    conftest.py
    unit/
    integration/
    feature/
```

## Setup

Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run The App

From the repository root:

```powershell
flask --app src.app run
```

Then open:

```text
http://127.0.0.1:5000
```

You can also run the app directly:

```powershell
python src/app.py
```

## Initialize The Database

From the repository root:

```powershell
flask --app src.app init-db
```

This creates the configured local SQLite database and applies `src/db/schema.sql`.

## Run Tests

```powershell
python -m pytest
```

The current tests cover skeleton-level behavior only: home page smoke loading and SQLite schema initialization with a temporary database.

## Instructor Review Path

1. Start with `docs/11_FINAL_PROJECT_SUMMARY.md` for the overall story.
2. Review `docs/01_REQUIREMENTS.md` and `docs/05_TRACEABILITY.md` to see how requirements survived the pivot.
3. Review `docs/03_ARCHITECTURE_DECISIONS.md` and `docs/04_UML_AND_DESIGN.md` to understand the updated Flask architecture.
4. Review `docs/06_TESTING_STRATEGY.md` for the first pytest validation set.
5. Review `docs/10_AI_USAGE_AND_VALIDATION.md` for responsible AI use and human review.
6. Use `demo/FINAL_DEMO_SCRIPT.md` as the planned final walkthrough.

## Source Course Artifacts Used

- Initial Requirement Set
- Working Agreement and Definition of Done for AstraNotes
- Week 2.2 Backlog and Sprint Zero Plan
- Architecture Decision Log
- Week 4.2 Complete UML Design Package
- Week 5.2 Requirements-to-UML Traceability Matrix
- Week 6 Development Environment and First Realization Slices
- Week 7.2 Testing Strategy and First Test Set
