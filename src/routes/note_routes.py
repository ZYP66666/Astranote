from flask import Blueprint, render_template

from src.services.note_service import NoteService


note_bp = Blueprint("notes", __name__, url_prefix="/notes")
note_service = NoteService()


@note_bp.route("/")
def list_notes():
    return render_template(
        "notes.html",
        is_placeholder=True,
        message="The notes workspace is scaffolded. Note CRUD is not implemented yet.",
    )


@note_bp.route("/new", methods=["GET", "POST"])
def new_note():
    return render_template(
        "note_form.html",
        is_placeholder=True,
        form_title="New Note",
        message="Create-note behavior is scaffolded for the next implementation slice.",
    )
