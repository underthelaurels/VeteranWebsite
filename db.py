import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def create_user(username, password, first=None, last=None, email=None):
    """Creates a user based on required username and password, and
    optional firstname, lastname, and email
    """
    database = get_db()
    database.execute('INSERT INTO users (username, password, firstName, lastName, email) VALUES (?, ?, ?, ?, ?)', (username, password, first, last, email))
    database.commit()

def user_exists(username):
    """Checks to see if user exists
    """
    database = get_db()
    return database.execute('SELECT user_id FROM users WHERE username = ?', (username,)).fetchone() is not None

def get_user_by_id(user_id):
    """Gets the user with the associated user_id
    """
    return get_db().execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()

def get_user_by_username(username):
    """Gets the user with the associated user_id
    """
    return get_db().execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as file:
        db.executescript(file.read().decode('utf-8'))

# Create click commands
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Deletes and recreates the tables"""
    init_db()
    click.echo('Initialized the databse!')