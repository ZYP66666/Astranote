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
    assert b"Notes" in login_response.data
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


def test_logged_in_user_can_create_note(auth_client):
    client = auth_client()
    response = client.post(
        "/notes/new",
        data={"title": "Sprint Notes", "content": "Planning content"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Note created." in response.data
    assert b"Sprint Notes" in response.data
    assert b"Planning content" in response.data


def test_create_note_rejects_empty_title(auth_client):
    client = auth_client()
    response = client.post(
        "/notes/new",
        data={"title": "", "content": "Draft content"},
    )

    assert response.status_code == 400
    assert b"Title is required." in response.data
    assert b"Draft content" in response.data


def test_logged_in_user_can_list_and_view_own_note(auth_client):
    client = auth_client()
    create_response = client.post(
        "/notes/new",
        data={"title": "Design Notes", "content": "MVC boundaries"},
    )
    note_location = create_response.headers["Location"]

    list_response = client.get("/notes/")
    assert list_response.status_code == 200
    assert b"Design Notes" in list_response.data

    detail_response = client.get(note_location)
    assert detail_response.status_code == 200
    assert b"Design Notes" in detail_response.data
    assert b"MVC boundaries" in detail_response.data


def test_user_cannot_open_another_users_note(client):
    client.post(
        "/auth/register",
        data={"username": "alex", "password": "secret-password"},
    )
    client.post(
        "/auth/login",
        data={"username": "alex", "password": "secret-password"},
    )
    create_response = client.post(
        "/notes/new",
        data={"title": "Private Note", "content": "Alex-only content"},
    )
    note_location = create_response.headers["Location"]
    client.post("/auth/logout")

    client.post(
        "/auth/register",
        data={"username": "blair", "password": "secret-password"},
    )
    client.post(
        "/auth/login",
        data={"username": "blair", "password": "secret-password"},
    )

    response = client.get(note_location)

    assert response.status_code == 404
    assert b"Alex-only content" not in response.data


def test_markdown_like_content_is_preserved(auth_client):
    client = auth_client()
    markdown_content = "# Title\n- item"
    response = client.post(
        "/notes/new",
        data={"title": "Markdown Note", "content": markdown_content},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"# Title\n- item" in response.data


def test_logged_out_user_is_redirected_from_edit_route(client):
    response = client.get("/notes/1/edit")

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]


def test_logged_in_user_can_edit_own_note(auth_client):
    client = auth_client()
    create_response = client.post(
        "/notes/new",
        data={"title": "Original", "content": "old content"},
    )
    note_location = create_response.headers["Location"]

    edit_page = client.get(f"{note_location}/edit")
    assert edit_page.status_code == 200
    assert b"Original" in edit_page.data
    assert b"old content" in edit_page.data

    edit_response = client.post(
        f"{note_location}/edit",
        data={"title": "Updated", "content": "new content"},
        follow_redirects=True,
    )

    assert edit_response.status_code == 200
    assert b"Note updated." in edit_response.data
    assert b"Updated" in edit_response.data
    assert b"new content" in edit_response.data
    assert b"Original" not in edit_response.data

    list_response = client.get("/notes/")
    assert b"Updated" in list_response.data
    assert b"Original" not in list_response.data


def test_edit_note_rejects_empty_title(auth_client):
    client = auth_client()
    create_response = client.post(
        "/notes/new",
        data={"title": "Original", "content": "old content"},
    )
    note_location = create_response.headers["Location"]

    response = client.post(
        f"{note_location}/edit",
        data={"title": "", "content": "still here"},
    )

    assert response.status_code == 400
    assert b"Title is required." in response.data
    assert b"still here" in response.data


def test_user_cannot_edit_another_users_note(client):
    client.post(
        "/auth/register",
        data={"username": "alex", "password": "secret-password"},
    )
    client.post(
        "/auth/login",
        data={"username": "alex", "password": "secret-password"},
    )
    create_response = client.post(
        "/notes/new",
        data={"title": "Private Note", "content": "Alex-only content"},
    )
    note_location = create_response.headers["Location"]
    client.post("/auth/logout")

    client.post(
        "/auth/register",
        data={"username": "blair", "password": "secret-password"},
    )
    client.post(
        "/auth/login",
        data={"username": "blair", "password": "secret-password"},
    )

    get_response = client.get(f"{note_location}/edit")
    post_response = client.post(
        f"{note_location}/edit",
        data={"title": "Changed", "content": "Blair content"},
    )

    assert get_response.status_code == 404
    assert post_response.status_code == 404


def test_markdown_like_content_is_preserved_after_edit(auth_client):
    client = auth_client()
    create_response = client.post(
        "/notes/new",
        data={"title": "Markdown", "content": "# Title\n- item"},
    )
    note_location = create_response.headers["Location"]

    response = client.post(
        f"{note_location}/edit",
        data={"title": "Markdown Updated", "content": "# Updated\n- item"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"# Updated\n- item" in response.data


def test_logged_out_user_is_redirected_from_delete_route(client):
    response = client.get("/notes/1/delete")

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]


def test_logged_in_user_can_reach_delete_confirmation_for_own_note(auth_client):
    client = auth_client()
    create_response = client.post(
        "/notes/new",
        data={"title": "Delete Candidate", "content": "content"},
    )
    note_location = create_response.headers["Location"]

    response = client.get(f"{note_location}/delete")

    assert response.status_code == 200
    assert b"Delete Note" in response.data
    assert b"Delete Candidate" in response.data
    assert b"Cancel" in response.data


def test_delete_confirmation_does_not_delete_until_post(auth_client):
    client = auth_client()
    create_response = client.post(
        "/notes/new",
        data={"title": "Keep Me", "content": "content"},
    )
    note_location = create_response.headers["Location"]

    confirmation_response = client.get(f"{note_location}/delete")
    detail_response = client.get(note_location)

    assert confirmation_response.status_code == 200
    assert b"Cancel" in confirmation_response.data
    assert detail_response.status_code == 200
    assert b"Keep Me" in detail_response.data


def test_confirmed_delete_removes_note_from_list(auth_client):
    client = auth_client()
    create_response = client.post(
        "/notes/new",
        data={"title": "Delete Candidate", "content": "content"},
    )
    note_location = create_response.headers["Location"]

    delete_response = client.post(f"{note_location}/delete", follow_redirects=True)

    assert delete_response.status_code == 200
    assert b"Note deleted." in delete_response.data
    assert b"Delete Candidate" not in delete_response.data
    assert b"No notes yet." in delete_response.data


def test_deleted_note_detail_returns_404(auth_client):
    client = auth_client()
    create_response = client.post(
        "/notes/new",
        data={"title": "Delete Candidate", "content": "content"},
    )
    note_location = create_response.headers["Location"]

    client.post(f"{note_location}/delete")
    response = client.get(note_location)

    assert response.status_code == 404


def test_user_cannot_delete_another_users_note(client):
    client.post(
        "/auth/register",
        data={"username": "alex", "password": "secret-password"},
    )
    client.post(
        "/auth/login",
        data={"username": "alex", "password": "secret-password"},
    )
    create_response = client.post(
        "/notes/new",
        data={"title": "Private Note", "content": "Alex-only content"},
    )
    note_location = create_response.headers["Location"]
    client.post("/auth/logout")

    client.post(
        "/auth/register",
        data={"username": "blair", "password": "secret-password"},
    )
    client.post(
        "/auth/login",
        data={"username": "blair", "password": "secret-password"},
    )

    get_response = client.get(f"{note_location}/delete")
    post_response = client.post(f"{note_location}/delete")

    assert get_response.status_code == 404
    assert post_response.status_code == 404

    client.post("/auth/logout")
    client.post(
        "/auth/login",
        data={"username": "alex", "password": "secret-password"},
    )
    detail_response = client.get(note_location)

    assert detail_response.status_code == 200
    assert b"Alex-only content" in detail_response.data
