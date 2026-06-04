# 11 Final Project Summary

## Project Overview

AstraNotes is a note-taking application concept for engineers and technical users. Across the course, the project moved through requirements, planning, architecture, UML design, traceability, implementation planning, and testing strategy.

The original artifacts selected a C++17 local-first desktop path. The final implementation direction intentionally pivots to a faster runnable local web MVP using Python, Flask, SQLite, HTML/CSS/Jinja, and pytest.

## Source Artifacts Used

- Initial Requirement Set
- Working Agreement and Definition of Done
- Week 2.2 Backlog and Sprint Zero Plan
- Architecture Decision Log
- Week 4.2 UML Design Package
- Week 5.2 Requirements-to-UML Traceability Matrix
- Week 6 Development Environment and First Realization Slices
- Week 7.2 Testing Strategy and First Test Set

## Final MVP

The final MVP will allow local users to:

- Register and log in
- Create notes
- View a list of their own notes
- Open saved notes
- Edit notes
- Delete notes with confirmation
- Search their own notes by keyword
- Avoid access to another user's notes
- Preserve Markdown-compatible text
- Reopen notes from SQLite storage

## SDLC Journey Preserved

| SDLC Area | Evidence In Repository |
| --- | --- |
| Requirements | `01_REQUIREMENTS.md` |
| Planning | `02_BACKLOG_AND_SPRINT_ZERO.md` |
| Architecture | `03_ARCHITECTURE_DECISIONS.md` |
| Design | `04_UML_AND_DESIGN.md` |
| Traceability | `05_TRACEABILITY.md` |
| Testing | `06_TESTING_STRATEGY.md` |
| Security | `07_SECURITY_NOTES.md` |
| Deployment | `08_DEPLOYMENT_NOTES.md` |
| Maintenance | `09_MAINTENANCE_NOTES.md` |
| AI use | `10_AI_USAGE_AND_VALIDATION.md` |
| Final demo | `demo/FINAL_DEMO_SCRIPT.md` |

## What Stayed The Same

- AstraNotes remains local-first.
- Notes remain the core product object.
- Register/login and create/open/edit/delete/search/save remain the main MVP workflows.
- Markdown preservation remains important.
- MVC/separation of concerns remains a design requirement.
- Testing and traceability remain part of the Definition of Done.
- AI remains a drafting and review partner, not the final authority.

## What Changed

- C++17 desktop implementation became Python/Flask local web implementation.
- Google Test became pytest.
- Desktop views became Jinja templates.
- Local file/storage abstraction became SQLite.
- Single-user desktop assumptions became basic local multi-user support.
- Secure notes, version history, voice notes, and plugin architecture moved to future scope.

## Migration From Old C++ Path

Migrated:

- Product vision
- Core note workflows
- MVC/separation-of-concerns principle
- Testing and traceability discipline
- Responsible AI review process

Updated:

- Technology stack
- Deployment model
- Data model
- Authentication/session assumptions
- First implementation slices

## Final Defense Message

The most important project decision was scope control. The final MVP does not try to implement every attractive feature from the original idea. Instead, it demonstrates the full SDLC path with a focused, runnable product slice:

Create and manage local Markdown-compatible notes with basic user separation, SQLite persistence, clean architecture boundaries, and requirement-backed tests.

## Current Status

Implementation has started with the initial runnable Flask skeleton and FR-1 local authentication slice. The repository now includes `src/app.py`, registered auth and note blueprints, SQLite schema/init helpers, Jinja templates, CSS, implemented user repository/auth service behavior, Flask session handling, and pytest coverage for registration/login/logout.

The next phase is to implement FR-2 and FR-3: create notes and list/view/open the logged-in user's own notes. Edit, delete, search, cross-user note protection, and Markdown persistence tests remain follow-up slices.
