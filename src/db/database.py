from pathlib import Path
import sqlite3

import click
from flask import current_app, g


def connect_database(database_path):
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def schema_path():
    return Path(__file__).with_name("schema.sql")


def init_database(database_path):
    database_path = Path(database_path)
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = connect_database(database_path)
    try:
        connection.executescript(schema_path().read_text(encoding="utf-8"))
        connection.commit()
    finally:
        connection.close()


def get_db():
    if "db" not in g:
        database_path = Path(current_app.config["DATABASE"])
        database_path.parent.mkdir(parents=True, exist_ok=True)
        g.db = connect_database(database_path)
    return g.db


def close_db(error=None):
    database = g.pop("db", None)
    if database is not None:
        database.close()


def init_db():
    database_path = Path(current_app.config["DATABASE"])
    init_database(database_path)


@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Initialized the AstraNotes database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
