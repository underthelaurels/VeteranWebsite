import os

from flask import Flask, render_template

# Create app for Google App Engine
app = Flask(__name__)

# register routes in the 'routes.py' file
from auth import auth
app.register_blueprint(auth)

# register homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

