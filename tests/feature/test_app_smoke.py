def test_home_page_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"AstraNotes" in response.data


def test_register_login_logout_flow(client):
    register_response = client.post(
        "/auth/register",
        data={"username": "alex", "password": "secret-password"},
        follow_redirects=True,
    )
    assert register_response.status_code == 200
    assert b"Registration successful. Please log in." in register_response.data
    assert b"Login" in register_response.data

    login_response = client.post(
        "/auth/login",
        data={"username": "alex", "password": "secret-password"},
        follow_redirects=True,
    )
    assert login_response.status_code == 200
    assert b"Notes Workspace" in login_response.data
    assert b"alex" in login_response.data

    with client.session_transaction() as session:
        assert session.get("user_id") is not None

    logout_response = client.post("/auth/logout", follow_redirects=True)
    assert logout_response.status_code == 200
    assert b"You have been logged out." in logout_response.data

    with client.session_transaction() as session:
        assert "user_id" not in session


def test_login_with_invalid_credentials_shows_error(client):
    client.post(
        "/auth/register",
        data={"username": "alex", "password": "secret-password"},
    )

    response = client.post(
        "/auth/login",
        data={"username": "alex", "password": "wrong-password"},
    )

    assert response.status_code == 400
    assert b"Invalid username or password." in response.data


def test_logged_out_notes_workspace_redirects_to_login(client):
    response = client.get("/notes/")

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]
