# AstraNotes Agent Notes

## Project Direction

Use the final defense documentation as the source of truth. The final implementation stack is Python, Flask, SQLite, Jinja templates, HTML/CSS, and pytest.

## Do Not Generate

- C++17 implementation code
- CMake files
- Google Test files
- Qt or desktop GUI code
- Cloud sync
- OAuth
- Docker or Kubernetes deployment
- Enterprise admin
- Billing
- AI summarization
- Collaborative editing
- Advanced version history

## Current Scope

The current codebase is only the initial runnable Flask skeleton. Full authentication and note CRUD behavior are intentionally deferred to later implementation tasks.

## Architecture Rules

- Keep route handlers thin.
- Keep validation and workflow rules in services.
- Keep SQL in repositories or database helpers, never templates.
- Keep templates focused on rendering.
- Use temporary SQLite databases for tests.
- Update traceability documentation when implementation status changes.
