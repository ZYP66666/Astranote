from src.db.database import get_db


class NoteRepository:
    """Placeholder for note persistence operations."""

    def __init__(self, connection_factory=get_db):
        self.connection_factory = connection_factory

    def create(self, user_id, title, content):
        raise NotImplementedError("Note persistence is not implemented in the skeleton.")

    def list_for_user(self, user_id):
        raise NotImplementedError("Note listing is not implemented in the skeleton.")
