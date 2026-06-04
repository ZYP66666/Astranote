# 07 Security Notes

## Purpose

This document clarifies what security means for the final MVP and separates basic local demo protection from deferred production security features.

## Source Artifacts Used

- Initial Requirement Set
- Working Agreement and Definition of Done
- Week 2.2 Backlog and Sprint Zero Plan
- Week 4.2 UML Design Package
- Week 5.2 Requirements-to-UML Traceability Matrix

## MVP Security Scope

The final MVP includes basic local multi-user privacy controls:

- Local registration and login
- Password hashing
- Flask session-based login state
- User-owned notes
- Authorization checks on note view/edit/delete
- Validation messages that avoid silent failure

## Explicit Non-Goals

The MVP does not implement:

- Real production encryption
- Secure-note passphrase unlock
- OAuth
- Cloud identity
- Enterprise roles/admin
- Billing security
- Production secret management
- Collaborative editing security
- Compliance-grade audit logs

## Security Requirements Kept

| Area | MVP Decision |
| --- | --- |
| Password storage | Store password hashes, not plaintext passwords. |
| Session access | Require login for note routes. |
| Note ownership | Query notes by both note ID and current user ID. |
| Error handling | Show controlled messages for invalid or unauthorized operations. |
| Data privacy | Keep data local in SQLite for the demo. |

## Responsible Handling Of Old Secure Notes Scope

Earlier artifacts included SecureNote, EncryptionService, passphrase unlock, and encrypted local records. Those ideas remain important product background, but they are deferred because the final prompt explicitly excludes real production encryption and secure-note implementation.

The final project should not pretend that basic login is equivalent to encrypted secure notes. The defense should state clearly:

- Basic local accounts separate demo users.
- Secure notes are future scope.
- Production encryption would require additional design, threat modeling, and testing.

## Security Test Ideas For MVP

- Anonymous users cannot access `/notes`.
- User A cannot open User B's note by guessing an ID.
- User A cannot edit or delete User B's note.
- Duplicate usernames are rejected.
- Blank passwords are rejected.
- Passwords are not stored in plaintext.

## Migration From Old C++ Path

Migrated:

- Privacy awareness
- Clear security boundaries
- Requirement that security claims must be defensible

Updated:

- UserSession becomes Flask session
- Secure-note encryption is deferred
- Basic multi-user access control is added for the Flask MVP
