from pathlib import Path

from flask import Flask, render_template

from src.db.database import init_app as init_database_app
from src.routes.auth_routes import auth_bp
from src.routes.note_routes import note_bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=str(Path(app.instance_path) / "astranotes.sqlite3"),
    )

    if test_config:
        app.config.update(test_config)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    init_database_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(note_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
