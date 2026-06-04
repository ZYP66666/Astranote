from src.repositories.note_repository import NoteRepository


class NoteService:
    """Placeholder for note validation, ownership checks, and CRUD workflows."""

    def __init__(self, note_repository=None):
        self.note_repository = note_repository or NoteRepository()

    def create_note(self, user_id, title, content):
        raise NotImplementedError("Create-note behavior is not implemented in the skeleton.")

    def list_notes_for_user(self, user_id):
        raise NotImplementedError("List-notes behavior is not implemented in the skeleton.")
