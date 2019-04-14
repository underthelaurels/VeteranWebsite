from flask import Blueprint, jsonify, render_template, request, flash, session, redirect, url_for
from flask import g

from db import get_db

user = Blueprint('user', __name__)

@user.route('/profile', methods=['GET'])
def user_profile():
    return render_template('profile.html')