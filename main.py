# Imports
from flask import jsonify
from flask import Flask, request

#python2 /home/ctom96/google-cloud-sdk/bin/dev_appserver.py app.yaml

# create master app object
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world! /hello will return data after POST request'

@app.route('/hello', methods=['POST'])
def hello():
    resp = {
        "status":"success",
        "message":"Hello from the API!"
    }

    return jsonify(resp)