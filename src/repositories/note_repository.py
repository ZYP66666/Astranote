from src.db.database import get_db
from src.models.note import Note


class NoteRepository:
    """SQLite persistence operations for user-owned notes."""

    def __init__(self, connection_factory=get_db):
        self.connection_factory = connection_factory

    def create(self, user_id, title, content):
        database = self.connection_factory()
        cursor = database.execute(
            """
            INSERT INTO notes (user_id, title, content)
            VALUES (?, ?, ?)
            """,
            (user_id, title, content),
        )
        database.commit()
        return self.find_for_user(cursor.lastrowid, user_id)

    def list_for_user(self, user_id):
        rows = self.connection_factory().execute(
            """
            SELECT id, user_id, title, content, created_at, updated_at
            FROM notes
            WHERE user_id = ?
            ORDER BY updated_at DESC, id DESC
            """,
            (user_id,),
        ).fetchall()
        return [self._to_note(row) for row in rows]

    def search_for_user(self, user_id, keyword):
        keyword = (keyword or "").strip()
        if not keyword:
            return self.list_for_user(user_id)

        pattern = f"%{keyword}%"
        rows = self.connection_factory().execute(
            """
            SELECT id, user_id, title, content, created_at, updated_at
            FROM notes
            WHERE user_id = ? AND (title LIKE ? OR content LIKE ?)
            ORDER BY updated_at DESC, id DESC
            """,
            (user_id, pattern, pattern),
        ).fetchall()
        return [self._to_note(row) for row in rows]

    def find_for_user(self, note_id, user_id):
        row = self.connection_factory().execute(
            """
            SELECT id, user_id, title, content, created_at, updated_at
            FROM notes
            WHERE id = ? AND user_id = ?
            """,
            (note_id, user_id),
        ).fetchone()
        return self._to_note(row)

    def update_for_user(self, note_id, user_id, title, content):
        database = self.connection_factory()
        cursor = database.execute(
            """
            UPDATE notes
            SET title = ?, content = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ? AND user_id = ?
            """,
            (title, content, note_id, user_id),
        )
        database.commit()
        if cursor.rowcount == 0:
            return None
        return self.find_for_user(note_id, user_id)

    def delete_for_user(self, note_id, user_id):
        database = self.connection_factory()
        cursor = database.execute(
            "DELETE FROM notes WHERE id = ? AND user_id = ?",
            (note_id, user_id),
        )
        database.commit()
        return cursor.rowcount > 0

    @staticmethod
    def _to_note(row):
        if row is None:
            return None
        return Note(
            id=row["id"],
            user_id=row["user_id"],
            title=row["title"],
            content=row["content"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )
