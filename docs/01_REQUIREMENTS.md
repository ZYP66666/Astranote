# 01 Requirements

## Purpose

This document migrates the AstraNotes requirement baseline from the original course artifacts into the final Python/Flask MVP direction. The final implementation decision overrides older C++17 desktop constraints.

## Source Artifacts Used

- Initial Requirement Set
- Week 2.2 Backlog and Sprint Zero Plan
- Week 5.2 Requirements-to-UML Traceability Matrix
- Working Agreement and Definition of Done

## Final MVP Product Goal

AstraNotes is a local-running web application that lets users create, manage, and reopen Markdown-compatible text notes. It demonstrates disciplined SDLC practice, basic privacy boundaries through local user accounts, SQLite persistence, MVC separation, and pytest-based validation.

## Final Flask MVP Functional Requirements

| ID | Final MVP Requirement | Source Requirement |
| --- | --- | --- |
| FR-1 | User can register and log in. | Added for final Flask MVP basic multi-user support. |
| FR-2 | User can create a note with title and content. | Original course create-note requirement. |
| FR-3 | User can list, view, and open their own notes. | Original course open/view requirement plus final user ownership rule. |
| FR-4 | User can edit their own notes. | Original course edit-note requirement plus final user ownership rule. |
| FR-5 | User can delete their own notes with confirmation. | Original course delete-note requirement plus final user ownership rule. |
| FR-6 | User can search their own notes by keyword in title or content. | Formalizes the earlier weak SearchIndex idea as a scoped MVP feature. |
| FR-7 | User cannot see, edit, delete, or search another user's notes. | Added for final Flask MVP multi-user privacy boundary. |
| FR-8 | Markdown-compatible note content is preserved exactly as typed. | Original course Markdown requirement. |

## Non-Functional Requirements Kept For MVP

| ID | Final MVP Requirement | Notes |
| --- | --- | --- |
| NFR1-FLASK | The app runs locally in a browser using Flask. | Replaces the old desktop requirement. |
| NFR2 | The data model should reasonably support at least 1,000 notes. | Kept as scale awareness, not a performance-heavy feature. |
| GR1 | Business logic is separated from UI rendering. | Preserves MVC/separation-of-concerns intent. |
| RR1-FLASK | Core behavior is testable with pytest. | Replaces Google Test. |
| DR1 | Notes and users are persisted in local SQLite. | Carries forward the original course local persistence requirement. |

## Security, Privacy, And Reliability Requirements Kept For MVP

| ID | Requirement | Scope |
| --- | --- | --- |
| SPR-MVP-1 | Each note belongs to one local user account. | Basic multi-user privacy boundary. |
| SPR-MVP-2 | Passwords are stored using a password hash, not plaintext. | Development-grade local account protection. |
| SPR-MVP-3 | Unauthorized note access is blocked at service/route boundaries. | User A cannot view, edit, or delete User B's notes. |
| REL-MVP-1 | Invalid input and failed operations show clear messages. | Preserves old failure-handling goals. |

## Deferred Requirements

- Secure notes with real encryption and passphrase unlock
- Voice notes
- Full extensible plugin architecture
- Full version history and restore
- Advanced search ranking or a dedicated SearchIndex
- Markdown preview/rendering
- Cloud sync, OAuth, enterprise admin, billing, mobile app
- AI summarization or collaborative editing
- Production encryption and production deployment hardening

## Migration From Old C++ Path

Migrated:

- Product idea: local-first technical notes for engineers
- Requirements for register/login and create/open/edit/delete/search/save
- Markdown preservation
- MVC separation
- Testing and traceability expectations
- Responsible AI and Definition of Done principles

Updated:

- C++17 desktop becomes Python/Flask local web app
- Google Test becomes pytest
- Local file/local database storage becomes SQLite
- Single-user desktop assumption becomes basic local multi-user support

Removed as implementation constraints:

- CMake
- RAII and smart pointers
- Qt or desktop GUI assumptions
- C++ class implementation details
