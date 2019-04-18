import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

import datetime

# DB Specific stuff


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# User methods

def create_user(username, password, first=None, last=None, email=None):
    """Creates a user based on required username and password, and
    optional firstname, lastname, and email
    """
    database = get_db()
    database.execute('INSERT INTO users (username, password, firstName, lastName, email) VALUES (?, ?, ?, ?, ?)',
                     (username, password, first, last, email))
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


# employment methods

def create_job(title, description, industry=None, due_date=None):
    """Adds a job to the db
    """
    # get current time as string
    try:
        current = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        db = get_db()
        db.execute('INSERT INTO jobs (title, description, industry, time_posted, due_date) VALUES (?, ?, ?, ?, ?)',
                [title, description, industry, current, due_date])
        last = query_db('SELECT last_insert_rowid()')
        db.commit()
        return last
    except Exception as e:
        print "failed to insert job:", e
        return False

def get_job_by_id(uid):
    try:
        return query_db('SELECT * FROM jobs WHERE job_id = ?', (uid,), one=True)
    except Exception as e:
        print "Error getting job in db", e

def delete_job(id):
    try:
        db = get_db()
        db.execute('DELETE FROM jobs WHERE job_id = ?', (id,))
        db.commit()
        return True
    except Exception as e:
        print "Could not delete job from db:", e
        return False

# Flask methods

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
