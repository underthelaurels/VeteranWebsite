from flask import Blueprint, jsonify, render_template, request, flash, session, redirect, url_for
from flask import g

import db

user = Blueprint('user', __name__)

@user.route('/profile', methods=['GET'])
def user_profile():
    if not session.get('user_id'):
        return redirect('/')

    row = db.get_user_by_id(session['user_id'])
    user = convert_user(row)
    for k, v in user.items():
        session[k] = v

    return render_template('profile.html')

@user.route('/dashboard', methods=['GET'])
def user_dashboard():
    return render_template('dashboard.html')

@user.route('/site/user/update', methods=['POST'])
def site_update_user():
    update_user()

    if session.get('update_outcome') == 'success':
        flash("Update successful!", "success")
        return redirect('/')
    else:
        flash("Update unsuccessful", "failure")
        return redirect('/')

@user.route('/user/update', methods=['POST'])
def update_user():
    try:
        print request.form
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        isEmployer = request.form.get('isEmployer')

        if isEmployer:
            isEmployer = True
        else:
            isEmployer = False

        r = db.update_user(session['user_id'], username, first_name, last_name, email, isEmployer)

        if r:
            resp = {
                "status":"success",
                "message":"Updated user"
            }
            session['update_outcome'] = 'success'

            return jsonify(resp)

        resp = {
            "status":"failure",
            "message":"Failed to update user"
        }
        session['update_outcome'] = 'failure'

        return jsonify(resp)
    except Exception as e:
        print "Could not update user:", e
        resp = {
            "status":"failure",
            "message":"Failed to update user"
        }

        return jsonify(resp)

def convert_user(row):
    user = {
        'user_id': row['user_id'],
        'username': row['username'],
        'firstName': row['firstName'],
        'lastName': row['lastName'],
        'email': row['email'],
        'isEmployer': row['isEmployer'],
    }
    return user