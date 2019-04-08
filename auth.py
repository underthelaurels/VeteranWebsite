from flask import Blueprint, jsonify, render_template

auth = Blueprint('auth', __name__)

@auth.route('/hello', methods=['POST'])
def hello():
    resp = {
        "status":"success",
        "message":"Hello from the API!"
    }

    return jsonify(resp)

@auth.route('/login', methods=['GET'])
def render_login():
    return render_template('login.html')


@auth.route('/register', methods=['GET'])
def render_register():
    return render_template('register.html')