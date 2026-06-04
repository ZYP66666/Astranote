from functools import wraps

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from src.services.auth_service import AuthService
from src.repositories.user_repository import UserRepository


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
auth_service = AuthService()


@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    g.user = None
    if user_id is not None:
        g.user = UserRepository().find_by_id(user_id)
        if g.user is None:
            session.clear()


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash("Please log in to continue.", "error")
            return redirect(url_for("auth.login"))
        return view(**kwargs)

    return wrapped_view


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        result = auth_service.authenticate_user(
            request.form.get("username"),
            request.form.get("password"),
        )
        if result.success:
            session.clear()
            session["user_id"] = result.user.id
            flash(result.message, "success")
            return redirect(url_for("notes.list_notes"))

        flash(result.message, "error")
        return render_template("login.html", username=request.form.get("username", "")), 400

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        result = auth_service.register_user(
            request.form.get("username"),
            request.form.get("password"),
        )
        if result.success:
            flash(result.message, "success")
            return redirect(url_for("auth.login"))

        flash(result.message, "error")
        return render_template("register.html", username=request.form.get("username", "")), 400

    return render_template("register.html")


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("index"))
