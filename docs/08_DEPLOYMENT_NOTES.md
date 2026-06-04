# 08 Deployment Notes

## Purpose

This document defines how the final AstraNotes MVP should be run and reviewed locally. It updates the older desktop deployment assumptions to a Flask local web application.

## Source Artifacts Used

- Week 4.2 UML Design Package
- Week 6 Development Environment and First Realization Slices
- Architecture Decision Log

## Final Deployment Model

AstraNotes is a local-running web application:

```text
Developer/Instructor Machine
  |
Python virtual environment
  |
Flask development server
  |
Browser at http://127.0.0.1:5000
  |
SQLite database file
```

## Intended Local Runtime

- Install Python dependencies.
- Initialize SQLite database.
- Run Flask locally.
- Open the app in a browser.
- Register a local demo user.
- Create, edit, view, and delete notes.
- Run pytest to validate behavior.

## Environment Variables To Define Later

| Variable | Purpose |
| --- | --- |
| `FLASK_APP` | Points Flask to the app entry point. |
| `FLASK_ENV` or app config | Controls development/test behavior. |
| `SECRET_KEY` | Signs session cookies. Use a local dev value for MVP. |
| `DATABASE_PATH` | Optional path to SQLite database. |

## Database Deployment Notes

The MVP should use SQLite. Development and test databases must be separate:

- Development database: local app data for manual demo
- Test database: temporary database created by pytest fixtures

The repository should not commit real user data or generated local database files.

## Non-Deployment Scope

The final MVP does not require:

- Cloud hosting
- Docker or Kubernetes
- OAuth provider setup
- Production WSGI hosting
- Mobile packaging
- CI/CD pipeline

## Migration From Old C++ Path

Migrated:

- Local-first deployment principle
- Separation between runtime app and test environment
- Avoidance of fake cloud complexity

Updated:

- Desktop executable becomes Flask development server
- Local storage folder/local DB becomes SQLite database file
- Google Test environment becomes pytest environment
