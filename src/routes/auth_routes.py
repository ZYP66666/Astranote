from flask import Blueprint, render_template

from src.services.auth_service import AuthService


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
auth_service = AuthService()


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template(
        "login.html",
        is_placeholder=True,
        message="Login behavior is scaffolded for the next implementation slice.",
    )


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    return render_template(
        "register.html",
        is_placeholder=True,
        message="Registration behavior is scaffolded for the next implementation slice.",
    )
