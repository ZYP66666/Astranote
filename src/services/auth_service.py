from dataclasses import dataclass

from werkzeug.security import check_password_hash, generate_password_hash

from src.models.user import User
from src.repositories.user_repository import DuplicateUsernameError
from src.repositories.user_repository import UserRepository


@dataclass(frozen=True)
class AuthResult:
    success: bool
    message: str
    user: User | None = None


class AuthService:
    """Registration and login workflow rules for local users."""

    def __init__(self, user_repository=None):
        self.user_repository = user_repository or UserRepository()

    def register_user(self, username, password):
        username = self._normalize_username(username)
        if not username:
            return AuthResult(False, "Username is required.")
        if not password:
            return AuthResult(False, "Password is required.")
        if self.user_repository.find_by_username(username):
            return AuthResult(False, "Username is already taken.")

        password_hash = generate_password_hash(password)
        try:
            user = self.user_repository.create_user(username, password_hash)
        except DuplicateUsernameError:
            return AuthResult(False, "Username is already taken.")
        return AuthResult(True, "Registration successful. Please log in.", user)

    def authenticate_user(self, username, password):
        username = self._normalize_username(username)
        if not username:
            return AuthResult(False, "Username is required.")
        if not password:
            return AuthResult(False, "Password is required.")

        user = self.user_repository.find_by_username(username)
        if user is None or not check_password_hash(user.password_hash, password):
            return AuthResult(False, "Invalid username or password.")
        return AuthResult(True, "Login successful.", user)

    @staticmethod
    def _normalize_username(username):
        return (username or "").strip()
