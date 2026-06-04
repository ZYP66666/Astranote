from werkzeug.security import check_password_hash

from src.repositories.user_repository import UserRepository
from src.services.auth_service import AuthService


def test_register_rejects_empty_username(app):
    with app.app_context():
        result = AuthService().register_user("", "secret-password")

    assert result.success is False
    assert result.message == "Username is required."


def test_register_rejects_empty_password(app):
    with app.app_context():
        result = AuthService().register_user("alex", "")

    assert result.success is False
    assert result.message == "Password is required."


def test_register_rejects_duplicate_username(app):
    with app.app_context():
        service = AuthService()
        first_result = service.register_user("alex", "secret-password")
        duplicate_result = service.register_user("alex", "different-password")

    assert first_result.success is True
    assert duplicate_result.success is False
    assert duplicate_result.message == "Username is already taken."


def test_password_is_stored_as_hash_not_plain_text(app):
    with app.app_context():
        AuthService().register_user("alex", "secret-password")
        user = UserRepository().find_by_username("alex")

    assert user.password_hash != "secret-password"
    assert check_password_hash(user.password_hash, "secret-password")


def test_login_succeeds_with_valid_credentials(app):
    with app.app_context():
        service = AuthService()
        service.register_user("alex", "secret-password")
        result = service.authenticate_user("alex", "secret-password")

    assert result.success is True
    assert result.user.username == "alex"


def test_login_fails_with_invalid_credentials(app):
    with app.app_context():
        service = AuthService()
        service.register_user("alex", "secret-password")
        result = service.authenticate_user("alex", "wrong-password")

    assert result.success is False
    assert result.message == "Invalid username or password."
