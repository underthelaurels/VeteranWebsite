from flask import Blueprint, jsonify, render_template, request, flash, session, redirect, url_for
from flask import g

import db

user = Blueprint('user', __name__)

@user.route('/profile', methods=['GET'])
def user_profile():
    user = db.get_user_by_username(session['username'])
    return render_template('profile.html')

@user.route('/dashboard', methods=['GET'])
def user_dashboard():
    return render_template('dashboard.html')