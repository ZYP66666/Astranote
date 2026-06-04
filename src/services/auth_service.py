from src.repositories.user_repository import UserRepository


class AuthService:
    """Placeholder for registration, login, logout, and session workflow rules."""

    def __init__(self, user_repository=None):
        self.user_repository = user_repository or UserRepository()

    def register_user(self, username, password):
        raise NotImplementedError("Registration is not implemented in the skeleton.")

    def authenticate_user(self, username, password):
        raise NotImplementedError("Login is not implemented in the skeleton.")
