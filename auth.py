from flask import Blueprint, jsonify, render_template, request, flash, session, redirect, url_for
from flask import g

import db

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

@auth.route('/site/user/register', methods=['POST'])
def site_register_user():
    register_user()
    
    if session.get('username') is not None:
        flash("Registration successful!", "success")
        return redirect('/')
    else:
        flash("Unable to register!", "error")
        return redirect('/')

@auth.route('/user/register', methods=['POST'])
def register_user():
    error = None
    username = request.form['username']
    password = request.form['password']
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    isEmployer = request.form.get('isEmployer')

    if request.method != 'POST':
        error = "Invalid request method"
    
    if not username:
        error = "Username is required"
    elif not password:
        error = "Password is required"
    elif db.user_exists(username):
        error = "Username {} is already registered".format(username)
    
    if error is None:
        db.create_user(username, password, first_name, last_name, email, isEmployer)

        resp = {
            "status": "success",
            "message":"Successfully registered user",
            "username":username
        }

        user = db.get_user_by_username(username)
        session['user_id'] = user['user_id']
        session['username'] = username
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

    if request.method != 'POST':
        error = "Invalid request method"

    if not username:
        error = "Username is required"
    elif not password:
        error = "Password is required"

    user = db.get_user_by_username(username)

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
    session['user_id'] = user['user_id']
    session['username'] = username

    resp = {
        "status":"success",
        "message":"User logged in",
        "user_id":user['user_id']
    }

    return jsonify(resp)

@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db.get_user_by_id(user_id)