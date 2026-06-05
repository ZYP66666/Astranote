from time import sleep

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


def test_note_repository_updates_title_content_and_updated_at_without_duplicate(app):
    with app.app_context():
        user = UserRepository().create_user("alex", "hashed-password")
        repository = NoteRepository()
        created_note = repository.create(user.id, "Original", "content")
        original_updated_at = created_note.updated_at

        sleep(1.1)
        updated_note = repository.update_for_user(
            created_note.id,
            user.id,
            "Updated",
            "# Updated\n- item",
        )
        notes = repository.list_for_user(user.id)

    assert updated_note.id == created_note.id
    assert updated_note.title == "Updated"
    assert updated_note.content == "# Updated\n- item"
    assert updated_note.updated_at != original_updated_at
    assert len(notes) == 1


def test_note_repository_does_not_update_note_for_wrong_user(app):
    with app.app_context():
        user_repository = UserRepository()
        alex = user_repository.create_user("alex", "first-hash")
        blair = user_repository.create_user("blair", "second-hash")
        note_repository = NoteRepository()
        alex_note = note_repository.create(alex.id, "Alex Note", "alpha")

        wrong_user_result = note_repository.update_for_user(
            alex_note.id,
            blair.id,
            "Changed",
            "beta",
        )
        unchanged_note = note_repository.find_for_user(alex_note.id, alex.id)

    assert wrong_user_result is None
    assert unchanged_note.title == "Alex Note"
    assert unchanged_note.content == "alpha"


def test_note_repository_deletes_note_by_id_and_user_id(app):
    with app.app_context():
        user = UserRepository().create_user("alex", "hashed-password")
        repository = NoteRepository()
        note = repository.create(user.id, "Delete Me", "content")

        deleted = repository.delete_for_user(note.id, user.id)
        after_delete = repository.find_for_user(note.id, user.id)

    assert deleted is True
    assert after_delete is None


def test_note_repository_delete_does_not_delete_another_users_note(app):
    with app.app_context():
        user_repository = UserRepository()
        alex = user_repository.create_user("alex", "first-hash")
        blair = user_repository.create_user("blair", "second-hash")
        note_repository = NoteRepository()
        alex_note = note_repository.create(alex.id, "Alex Note", "alpha")

        deleted = note_repository.delete_for_user(alex_note.id, blair.id)
        still_exists = note_repository.find_for_user(alex_note.id, alex.id)

    assert deleted is False
    assert still_exists is not None
    assert still_exists.title == "Alex Note"


def test_note_repository_search_finds_notes_by_title_for_current_user(app):
    with app.app_context():
        user = UserRepository().create_user("alex", "hashed-password")
        repository = NoteRepository()
        repository.create(user.id, "Sprint Planning", "alpha")
        repository.create(user.id, "Architecture Notes", "beta")

        results = repository.search_for_user(user.id, "Sprint")

    assert [note.title for note in results] == ["Sprint Planning"]


def test_note_repository_search_finds_notes_by_content_for_current_user(app):
    with app.app_context():
        user = UserRepository().create_user("alex", "hashed-password")
        repository = NoteRepository()
        repository.create(user.id, "Planning", "Discuss MVC layers")
        repository.create(user.id, "Other", "No matching term")

        results = repository.search_for_user(user.id, "MVC")

    assert [note.title for note in results] == ["Planning"]


def test_note_repository_search_does_not_return_another_users_notes(app):
    with app.app_context():
        user_repository = UserRepository()
        alex = user_repository.create_user("alex", "first-hash")
        blair = user_repository.create_user("blair", "second-hash")
        note_repository = NoteRepository()
        note_repository.create(alex.id, "Shared Keyword", "alpha")
        note_repository.create(blair.id, "Shared Keyword", "beta")

        results = note_repository.search_for_user(alex.id, "Shared")

    assert len(results) == 1
    assert results[0].user_id == alex.id


def test_note_repository_empty_search_returns_all_notes_for_user(app):
    with app.app_context():
        user_repository = UserRepository()
        alex = user_repository.create_user("alex", "first-hash")
        blair = user_repository.create_user("blair", "second-hash")
        note_repository = NoteRepository()
        note_repository.create(alex.id, "First", "alpha")
        note_repository.create(alex.id, "Second", "beta")
        note_repository.create(blair.id, "Third", "gamma")

        results = note_repository.search_for_user(alex.id, "")

    assert {note.title for note in results} == {"First", "Second"}
