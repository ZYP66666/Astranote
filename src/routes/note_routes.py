from flask import Blueprint, abort, flash, g, redirect, render_template, request, url_for

from src.routes.auth_routes import login_required
from src.services.note_service import NoteService


note_bp = Blueprint("notes", __name__, url_prefix="/notes")
note_service = NoteService()


@note_bp.route("/")
@login_required
def list_notes():
    result = note_service.list_notes_for_user(g.user.id)
    return render_template(
        "notes.html",
        notes=result.notes,
    )


@note_bp.route("/new", methods=["GET", "POST"])
@login_required
def new_note():
    if request.method == "POST":
        result = note_service.create_note(
            g.user.id,
            request.form.get("title"),
            request.form.get("content"),
        )
        if result.success:
            flash(result.message, "success")
            return redirect(url_for("notes.view_note", note_id=result.note.id))

        flash(result.message, "error")
        return render_template(
            "note_form.html",
            form_title="New Note",
            title=request.form.get("title", ""),
            content=request.form.get("content", ""),
        ), 400

    return render_template(
        "note_form.html",
        form_title="New Note",
        title="",
        content="",
    )


@note_bp.route("/<int:note_id>")
@login_required
def view_note(note_id):
    result = note_service.get_note_for_user(note_id, g.user.id)
    if not result.success:
        abort(404, description=result.message)
    return render_template("note_detail.html", note=result.note)


@note_bp.route("/<int:note_id>/edit", methods=["GET", "POST"])
@login_required
def edit_note(note_id):
    existing_result = note_service.get_note_for_user(note_id, g.user.id)
    if not existing_result.success:
        abort(404, description=existing_result.message)

    if request.method == "POST":
        result = note_service.update_note(
            note_id,
            g.user.id,
            request.form.get("title"),
            request.form.get("content"),
        )
        if result.success:
            flash(result.message, "success")
            return redirect(url_for("notes.view_note", note_id=result.note.id))

        flash(result.message, "error")
        return render_template(
            "note_form.html",
            form_title="Edit Note",
            title=request.form.get("title", ""),
            content=request.form.get("content", ""),
        ), 400

    return render_template(
        "note_form.html",
        form_title="Edit Note",
        title=existing_result.note.title,
        content=existing_result.note.content,
    )
