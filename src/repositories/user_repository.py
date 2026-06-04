import sqlite3

from src.db.database import get_db
from src.models.user import User


class DuplicateUsernameError(Exception):
    """Raised when attempting to create a user with an existing username."""


class UserRepository:
    """SQLite persistence operations for local AstraNotes users."""

    def __init__(self, connection_factory=get_db):
        self.connection_factory = connection_factory

    def create_user(self, username, password_hash):
        database = self.connection_factory()
        try:
            cursor = database.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash),
            )
            database.commit()
        except sqlite3.IntegrityError as exc:
            raise DuplicateUsernameError(username) from exc
        return self.find_by_id(cursor.lastrowid)

    def find_by_username(self, username):
        row = self.connection_factory().execute(
            "SELECT id, username, password_hash, created_at FROM users WHERE username = ?",
            (username,),
        ).fetchone()
        return self._to_user(row)

    def find_by_id(self, user_id):
        row = self.connection_factory().execute(
            "SELECT id, username, password_hash, created_at FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()
        return self._to_user(row)

    @staticmethod
    def _to_user(row):
        if row is None:
            return None
        return User(
            id=row["id"],
            username=row["username"],
            password_hash=row["password_hash"],
            created_at=row["created_at"],
        )
