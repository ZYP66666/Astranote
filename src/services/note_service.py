from dataclasses import dataclass

from src.models.note import Note
from src.repositories.note_repository import NoteRepository


@dataclass(frozen=True)
class NoteResult:
    success: bool
    message: str
    note: Note | None = None
    notes: list[Note] | None = None


class NoteService:
    """Validation, ownership, and workflow rules for user-owned notes."""

    def __init__(self, note_repository=None):
        self.note_repository = note_repository or NoteRepository()

    def create_note(self, user_id, title, content):
        title = (title or "").strip()
        content = "" if content is None else content
        if not title:
            return NoteResult(False, "Title is required.")

        note = self.note_repository.create(user_id, title, content)
        return NoteResult(True, "Note created.", note=note)

    def list_notes_for_user(self, user_id):
        notes = self.note_repository.list_for_user(user_id)
        return NoteResult(True, "Notes loaded.", notes=notes)

    def get_note_for_user(self, note_id, user_id):
        note = self.note_repository.find_for_user(note_id, user_id)
        if note is None:
            return NoteResult(False, "Note not found.")
        return NoteResult(True, "Note loaded.", note=note)
