from flask import Blueprint, jsonify, render_template, request, flash, session, redirect, url_for
from flask import g

import db

service = Blueprint('service', __name__, url_prefix='/service')

@service.route('/', methods=['GET'])
def show_service():
    return render_template('community_service.html')

@service.route('/add-event', methods=['POST'])
def add_event():
    try:
        name = request.form['name']
        date = request.form['date']
        time = request.form.get('time')
        street = request.form.get('street_address')
        city = request.form.get('city')
        state = request.form.get('state')
        zipcode = request.form.get('zipcode')

        res = db.create_service(name, date, time, street, city, state, zipcode)

        resp = {
            'status': 'success',
            'message': 'Successfully added community service event'
        }

        if not res:
            resp = {
                'status': 'failure',
                'message': 'Failed to add community service event'
            }

        return jsonify(resp)
    except Exception as e:
        print "Could not add job:", e

@service.route('/get-event', methods=['GET'])
def get_event():
    uid = request.args.get('id')
    get_all = request.args.get('all')
    
    if uid:
        row = db.get_service_by_id(uid)
        event = convert_event(row)
        
        resp = {
            'status': 'success',
            'event': event
        }

        return jsonify(resp)

    if get_all:
        rows = db.get_all_services()

        events = [convert_event(x) for x in rows]

        resp = {
            'status': 'success',
            'events': events
        }

        return jsonify(resp)

    resp = {
        'status': 'failure',
        'message': 'must specifiy either id or all as arguments to request'
    }
    return jsonify(resp)

@service.route('/delete-event', methods=['POST'])
def delete_service():
    try:
        uid = request.form['id']
        success = db.delete_service(uid)

        resp = {
            "status":"success",
            "message": success
        }

        return jsonify(resp)
    except Exception as e:
        print "Could not delete service:", e

def convert_event(row):
    event = {
        'name': row['name'],
        'date': row['date'],
        'time': row['time'],
        'street_address': row['street_address'],
        'city': row['city'],
        'state': row['state'],
        'zip': row['zip'],
    }

    return event