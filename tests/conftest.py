from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.app import create_app
from src.db.database import init_db


@pytest.fixture
def app(tmp_path):
    database_path = tmp_path / "astranotes_test.sqlite3"
    app = create_app(
        {
            "TESTING": True,
            "DATABASE": str(database_path),
            "SECRET_KEY": "test-secret",
        }
    )
    with app.app_context():
        init_db()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth_client(client):
    def register_and_login(username="alex", password="secret-password"):
        client.post(
            "/auth/register",
            data={"username": username, "password": password},
        )
        client.post(
            "/auth/login",
            data={"username": username, "password": password},
        )
        return client

    return register_and_login
