# 04 UML And Design

## Purpose

This document adapts the Week 4.2 UML design package to the final Flask web architecture. It preserves the design intent without requiring the original C++ class structure.

## Source Artifacts Used

- Week 4.2 Complete UML Design Package
- Week 5.2 Requirements-to-UML Traceability Matrix
- Week 6 Development Environment and First Realization Slices

## Design Scope

The final MVP design supports:

- Local user registration and login
- User-owned text notes
- Create, list, open, edit, and delete workflows
- Markdown text preservation
- SQLite persistence
- MVC-style separation
- pytest validation

## Updated Conceptual Class Model

```mermaid
classDiagram
    class User {
        id
        username
        password_hash
        created_at
    }

    class Note {
        id
        user_id
        title
        content
        created_at
        updated_at
    }

    class AuthService {
        register()
        authenticate()
        get_current_user()
    }

    class NoteService {
        create_note()
        list_notes()
        get_note()
        update_note()
        delete_note()
    }

    class UserRepository {
        create_user()
        find_by_username()
        find_by_id()
    }

    class NoteRepository {
        create()
        list_for_user()
        find_for_user()
        update_for_user()
        delete_for_user()
    }

    User "1" --> "*" Note
    AuthService --> UserRepository
    NoteService --> NoteRepository
```

## Updated Web Workflow: Create And Save Note

```mermaid
flowchart TD
    A["User opens New Note page"] --> B["Enter title and Markdown content"]
    B --> C["Submit form"]
    C --> D["Flask route receives POST"]
    D --> E["NoteService validates input"]
    E --> F{"Title valid?"}
    F -->|No| G["Return validation message"]
    F -->|Yes| H["NoteRepository inserts note for current user"]
    H --> I["SQLite commits note"]
    I --> J["Redirect to note detail or note list"]
```

## Updated Web Workflow: Open Existing Note

```mermaid
flowchart TD
    A["Logged-in user requests note id"] --> B["Flask route calls NoteService"]
    B --> C["NoteRepository queries by note id and user id"]
    C --> D{"Owned note found?"}
    D -->|No| E["Return not found or unauthorized response"]
    D -->|Yes| F["Render note detail template"]
```

## MVC Mapping

| Original UML Concept | Flask MVP Equivalent |
| --- | --- |
| MainView / NotesWorkspace | Jinja templates and CSS |
| NoteController | Flask routes/controllers |
| NoteManager | NoteService |
| NoteRepository | NoteRepository using SQLite |
| LocalStorage | SQLite connection and schema |
| UserSession | Flask session |
| TextNote | Note row with Markdown-compatible content |

## Removed Or Deferred UML Elements

- SecureNote is deferred.
- EncryptionService is deferred.
- VersionHistory is deferred.
- A dedicated SearchIndex is deferred. FR-6 will be implemented later as a simple SQLite title/content search scoped by user.
- VoiceNote is deferred.
- Plugin-style extensibility is deferred.

## Migration From Old C++ Path

Migrated:

- Note, TextNote, NoteManager, NoteRepository, LocalStorage, NoteController, and UserSession responsibilities
- Create/save/open workflow logic
- MVC separation and thin-view principle
- Failure handling for validation and unauthorized access

Updated:

- C++ classes become Python service/repository/data responsibilities
- Desktop use case flows become Flask request/response workflows
- MainView and NotesWorkspace become Jinja templates
- LocalStorage becomes SQLite database access
- UserSession becomes Flask session plus user ownership checks

## Design Quality Notes

- Views should not own validation or persistence.
- Routes should stay thin and delegate business rules to services.
- Repositories should hide SQL details from services and templates.
- Every note operation must include `user_id` to preserve basic multi-user boundaries.
- Error messages should be clear and controlled.
