from flask import Blueprint, jsonify, render_template, request, flash, session, redirect, url_for
from flask import g

from db import get_db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def render_login():
    return render_template('login.html')


@auth.route('/register', methods=['GET'])
def render_register():
    return render_template('register.html')

@auth.route('/user/logout', methods=['POST'])
def logout_user():
    session.clear()
    resp = {
        "status":"success",
        "message":"Successfully logged user out"
    }

    return jsonify(resp)

@auth.route('/user/register', methods=['POST'])
def register_user():
    error = None
    username = request.form['username']
    password = request.form['password']

    db = get_db()

    if request.method != 'POST':
        error = "Invalid request method"
    
    if not username:
        error = "Username is required"
    elif not password:
        error = "Password is required"
    elif db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone() is not None:
        error = "Username {} is already registered".format(username)
    
    if error is None:
        db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        db.commit()

        resp = {
            "status": "success",
            "message":"Successfully registered user",
            "username":username
        }

        return jsonify(resp)
    
    resp = {
        "status":"failure",
        "messsage":"unable to regsiter user",
        "reason":error
    }

    return jsonify(resp)

@auth.route('/site/user/login', methods=['POST'])
def site_login_user():
    login_user()
    
    if session.get('username') is not None:
        flash("Login successful!", "success")
        return redirect('/')
    else:
        flash("Unable to Login!", "error")
        return redirect('/')

        
@auth.route('/user/login', methods=['POST'])
def login_user():
    error = None
    print "form:", request.form
    username = request.form['username']
    password = request.form['password']

    db = get_db()

    if request.method != 'POST':
        error = "Invalid request method"

    if not username:
        error = "Username is required"
    elif not password:
        error = "Password is required"

    user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

    if user is None:
        error = "Incorrect username"
    elif password != user['password']:
        error = "Incorrect password"

    if error is not None:
        resp = {
            "status":"failure",
            "message":"Unable to log user in",
            "reason":error
            
        }

        return jsonify(resp)
        
    session.clear()
    session['user_id'] = user['id']
    session['username'] = username

    resp = {
        "status":"success",
        "message":"User logged in",
        "user_id":user['id']
    }

    return jsonify(resp)

@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()