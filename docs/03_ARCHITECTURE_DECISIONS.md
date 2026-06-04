# 03 Architecture Decisions

## Purpose

This document records the final architecture decision for AstraNotes and explains how it evolved from the earlier C++17 desktop decision.

## Source Artifacts Used

- Architecture Decision Log
- Week 4.2 UML Design Package
- Week 6 Development Environment and First Realization Slices
- Working Agreement and Definition of Done

## Original Architecture Direction

The earlier project artifacts selected:

- C++17
- Cross-platform desktop application
- MVC architecture
- RAII and smart pointers
- Local-first persistence
- Google Test
- Modular support for text, secure, and future note types

That path was coherent for the original course design work, but it is no longer the final implementation direction.

## Final Architecture Decision

AstraNotes will be implemented as a local-running Flask web application using Python, SQLite, Jinja templates, HTML/CSS, and pytest.

## Decision Drivers

- Faster path to a runnable final demo
- Simpler local setup for instructor review
- Easier end-to-end demonstration in a browser
- SQLite provides persistent local storage without cloud infrastructure
- Flask supports clean route/controller separation for a small MVC-style app
- pytest supports lightweight automated validation
- The stack fits the final MVP better than a desktop C++ application

## Selected Architecture

```text
Browser
  |
Flask Routes / Controllers
  |
Services
  |
Repositories
  |
SQLite Database
```

## Main Components

| Component | Responsibility |
| --- | --- |
| Flask app factory | Creates and configures the application. |
| Routes/controllers | Handle HTTP requests, forms, redirects, and template rendering. |
| Services | Enforce validation, note workflow rules, and ownership checks. |
| Repositories | Encapsulate SQLite queries for users and notes. |
| Models/data objects | Represent user and note records passed through the app. |
| Templates | Render pages using Jinja. |
| Static CSS | Provides local browser UI styling. |
| Tests | Validate service, repository, and route behavior with pytest. |

## Data Persistence Decision

SQLite is the final MVP persistence layer. It replaces the older local file/local DB abstraction and is sufficient for a local demo with at least 1,000 notes.

## Authentication Decision

The MVP includes basic local user accounts using password hashing and Flask sessions. This is not OAuth, enterprise authentication, or production-grade account management.

## Deferred Architecture Elements

- SecureNote class hierarchy
- EncryptionService
- VersionHistory/HistoryManager
- SearchIndex
- Plugin manager
- Voice note storage
- Cloud sync or API backend

## Migration From Old C++ Path

Migrated:

- MVC separation
- Service/repository/storage boundaries
- Local-first persistence
- Testable core behavior
- Scope-control discipline

Updated:

- NoteController becomes Flask routes plus service calls
- NoteRepository remains conceptually, but uses SQLite
- LocalStorage becomes database initialization and connection handling
- MainView/NotesWorkspace become Jinja templates
- Google Test becomes pytest

Rejected as final constraints:

- C++17
- CMake
- RAII/smart pointer concerns
- Desktop-only deployment
