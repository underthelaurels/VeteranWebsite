from flask import Blueprint, jsonify, render_template, request, flash, session, redirect, url_for
from flask import g

import db

employment = Blueprint('employment', __name__, url_prefix='/employment')


@employment.route('/')
def show_employment():
    return render_template('employment.html')

# POSTs to add data to the db:
@employment.route('/add-job', methods=['POST'])
def add_job():
    try:
        title = request.form['title']
        desc = request.form['description']
        industry = request.form.get('industry')
        due = request.form.get('due_date')

        last = db.create_job(title, desc, industry=industry, due_date=due)

        resp = {
            "status": "success",
            "id": last[0][0]
        }
    except Exception as e:
        resp = {
            "status": "failure",
            "message": "Could not add job: " + str(e)
        }
    return jsonify(resp)

@employment.route('/get-job', methods=['GET'])
def get_job():
    try:
        uid = request.args['id']
        job = db.get_job_by_id(uid)

        resp = {
            "status":"success",
            "job": convert_job(job)
        }

    except Exception as e:
        print "Error getting job:", e
        resp = {
            "status":"failure",
            "job": ""
        }
        
    return jsonify(resp)

@employment.route('/delete-job', methods=['POST'])
def delete_job():
    try:
        uid = request.form['id']
        success = db.delete_job(uid)

        resp = {
            "status":"success",
            "message": success
        }

        return jsonify(resp)
    except Exception as e:
        print "error in delete_job:", e

@employment.route('/make-employee', methods=['POST'])
def make_employee():
    return "not implemented yet..."


@employment.route('/make-employer', methods=['POST'])
def make_employer():
    return "not implemented yet..."


# Helper functions

def convert_job(row):
    job = {
        'job_id': row['job_id'],
        'title': row['title'],
        'description': row['description'],
        'industry': row['industry'],
        'time_posted': row['time_posted'],
        'due_date': row['due_date'],
    }

    return job