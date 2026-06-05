from src.db.database import connect_database, init_database
from src.repositories.note_repository import NoteRepository
from src.repositories.user_repository import DuplicateUsernameError, UserRepository


def test_init_database_creates_users_and_notes_tables(tmp_path):
    database_path = tmp_path / "astranotes_test.sqlite3"
    init_database(database_path)

    connection = connect_database(database_path)
    try:
        table_names = {
            row["name"]
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            )
        }
        assert {"users", "notes"}.issubset(table_names)

        user_columns = {
            row["name"] for row in connection.execute("PRAGMA table_info(users)")
        }
        assert {"id", "username", "password_hash", "created_at"}.issubset(user_columns)

        note_columns = {
            row["name"] for row in connection.execute("PRAGMA table_info(notes)")
        }
        assert {
            "id",
            "user_id",
            "title",
            "content",
            "created_at",
            "updated_at",
        }.issubset(note_columns)

        foreign_keys = list(connection.execute("PRAGMA foreign_key_list(notes)"))
        assert any(row["table"] == "users" and row["from"] == "user_id" for row in foreign_keys)
    finally:
        connection.close()


def test_user_repository_can_create_and_find_user(app):
    with app.app_context():
        repository = UserRepository()
        created_user = repository.create_user("alex", "hashed-password")
        found_user = repository.find_by_username("alex")

    assert created_user.id == found_user.id
    assert found_user.username == "alex"
    assert found_user.password_hash == "hashed-password"


def test_user_repository_rejects_duplicate_username(app):
    with app.app_context():
        repository = UserRepository()
        repository.create_user("alex", "first-hash")

        try:
            repository.create_user("alex", "second-hash")
        except DuplicateUsernameError:
            duplicate_was_rejected = True
        else:
            duplicate_was_rejected = False

    assert duplicate_was_rejected is True


def test_note_repository_can_create_and_find_note_by_id(app):
    markdown_content = "# Title\n- item"
    with app.app_context():
        user = UserRepository().create_user("alex", "hashed-password")
        repository = NoteRepository()
        created_note = repository.create(user.id, "Markdown Note", markdown_content)
        found_note = repository.find_for_user(created_note.id, user.id)

    assert found_note.id == created_note.id
    assert found_note.user_id == user.id
    assert found_note.title == "Markdown Note"
    assert found_note.content == markdown_content


def test_note_repository_lists_notes_by_user_id(app):
    with app.app_context():
        user_repository = UserRepository()
        alex = user_repository.create_user("alex", "first-hash")
        blair = user_repository.create_user("blair", "second-hash")
        note_repository = NoteRepository()
        alex_note = note_repository.create(alex.id, "Alex Note", "alpha")
        note_repository.create(blair.id, "Blair Note", "beta")

        alex_notes = note_repository.list_for_user(alex.id)

    assert [note.id for note in alex_notes] == [alex_note.id]
    assert alex_notes[0].title == "Alex Note"


def test_note_repository_does_not_find_note_for_wrong_user(app):
    with app.app_context():
        user_repository = UserRepository()
        alex = user_repository.create_user("alex", "first-hash")
        blair = user_repository.create_user("blair", "second-hash")
        note_repository = NoteRepository()
        alex_note = note_repository.create(alex.id, "Alex Note", "alpha")

        wrong_user_result = note_repository.find_for_user(alex_note.id, blair.id)

    assert wrong_user_result is None
