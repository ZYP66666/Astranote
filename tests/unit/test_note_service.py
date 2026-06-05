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
