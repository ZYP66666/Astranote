from src.services.auth_service import AuthService
from src.services.note_service import NoteService


def test_note_service_rejects_empty_title(app):
    with app.app_context():
        user = AuthService().register_user("alex", "secret-password").user
        result = NoteService().create_note(user.id, "", "content")

    assert result.success is False
    assert result.message == "Title is required."


def test_note_service_creates_valid_note_for_user(app):
    with app.app_context():
        user = AuthService().register_user("alex", "secret-password").user
        result = NoteService().create_note(user.id, "Sprint Notes", "content")

    assert result.success is True
    assert result.note.user_id == user.id
    assert result.note.title == "Sprint Notes"
    assert result.note.content == "content"


def test_note_service_allows_empty_content(app):
    with app.app_context():
        user = AuthService().register_user("alex", "secret-password").user
        result = NoteService().create_note(user.id, "Empty Content Note", "")

    assert result.success is True
    assert result.note.content == ""


def test_note_service_rejects_edit_when_title_is_empty(app):
    with app.app_context():
        user = AuthService().register_user("alex", "secret-password").user
        service = NoteService()
        note = service.create_note(user.id, "Original", "content").note

        result = service.update_note(note.id, user.id, "", "updated content")

    assert result.success is False
    assert result.message == "Title is required."


def test_note_service_updates_existing_note_for_owner(app):
    with app.app_context():
        user = AuthService().register_user("alex", "secret-password").user
        service = NoteService()
        note = service.create_note(user.id, "Original", "content").note

        result = service.update_note(note.id, user.id, "Updated", "updated content")
        notes = service.list_notes_for_user(user.id).notes

    assert result.success is True
    assert result.note.id == note.id
    assert result.note.title == "Updated"
    assert result.note.content == "updated content"
    assert len(notes) == 1


def test_note_service_does_not_return_another_users_note(app):
    with app.app_context():
        auth_service = AuthService()
        alex = auth_service.register_user("alex", "secret-password").user
        blair = auth_service.register_user("blair", "secret-password").user
        service = NoteService()
        alex_note = service.create_note(alex.id, "Private", "Alex-only content").note

        result = service.get_note_for_user(alex_note.id, blair.id)

    assert result.success is False
    assert result.note is None


def test_note_service_does_not_update_another_users_note(app):
    with app.app_context():
        auth_service = AuthService()
        alex = auth_service.register_user("alex", "secret-password").user
        blair = auth_service.register_user("blair", "secret-password").user
        service = NoteService()
        alex_note = service.create_note(alex.id, "Private", "Alex-only content").note

        result = service.update_note(alex_note.id, blair.id, "Changed", "Blair content")
        unchanged = service.get_note_for_user(alex_note.id, alex.id).note

    assert result.success is False
    assert result.note is None
    assert unchanged.title == "Private"
    assert unchanged.content == "Alex-only content"


def test_note_service_deletes_existing_note_for_owner(app):
    with app.app_context():
        user = AuthService().register_user("alex", "secret-password").user
        service = NoteService()
        note = service.create_note(user.id, "Delete Me", "content").note

        result = service.delete_note(note.id, user.id)
        after_delete = service.get_note_for_user(note.id, user.id)

    assert result.success is True
    assert result.message == "Note deleted."
    assert after_delete.success is False


def test_note_service_refuses_delete_for_unowned_note(app):
    with app.app_context():
        auth_service = AuthService()
        alex = auth_service.register_user("alex", "secret-password").user
        blair = auth_service.register_user("blair", "secret-password").user
        service = NoteService()
        alex_note = service.create_note(alex.id, "Private", "Alex-only content").note

        result = service.delete_note(alex_note.id, blair.id)
        still_exists = service.get_note_for_user(alex_note.id, alex.id)

    assert result.success is False
    assert result.message == "Note not found."
    assert still_exists.success is True
