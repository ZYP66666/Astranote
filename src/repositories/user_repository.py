from src.db.database import get_db


class UserRepository:
    """Placeholder for user persistence operations."""

    def __init__(self, connection_factory=get_db):
        self.connection_factory = connection_factory

    def create_user(self, username, password_hash):
        raise NotImplementedError("User persistence is not implemented in the skeleton.")

    def find_by_username(self, username):
        raise NotImplementedError("User lookup is not implemented in the skeleton.")
