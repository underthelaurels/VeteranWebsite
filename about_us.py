from flask import Blueprint, jsonify, render_template, request, flash, session, redirect, url_for
from flask import g


about_us = Blueprint('about_us', __name__)

@about_us.route('/about_us')
def show_about():
    return render_template('about_us.html')
