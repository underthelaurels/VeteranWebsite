import os

from flask import Flask, render_template
import click

# personal imports
import db
from auth import auth
from user import user

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'veteran-connect.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import other files and modules
    db.init_app(app)

    app.register_blueprint(auth)

    app.register_blueprint(user)

    @app.route('/')
    def show_hompage():
        return render_template('homepage.html')

    @app.route('/base')
    def show_base():
        return render_template('base.html')

    return app



if __name__ == '__main__':
    app = create_app()
    app.run()