from flask import Blueprint, jsonify, render_template, request, flash, session, redirect, url_for
from flask import g

import db

chat = Blueprint('chat', __name__, url_prefix='/chat')

@chat.route('/')
def show_chat():
    return render_template('chat.html')

@chat.route('/send', methods=['POST'])
def send_message():
    try:
        message = request.form['message']
        sender = request.form['sender']
        sender_color = request.form['sender_color']
        channel_id = request.form['channel_id']

        success = db.create_message(message, sender, sender_color, channel_id)

        if success:
            resp = {
                "status":"success",
                "message":"added message to channel"
            }
        else:
            resp = {
                "status":"failure",
                "message":"failed to add message to channel"
            }

        return jsonify(resp)

    except Exception as e:
        print "Could not send_message:", e

@chat.route('/poll', methods=['GET'])
def poll_messages():
    try:
        channel_id = request.args.get('channel_id')
        if not channel_id:
            resp = {
                "status":"failure",
                "message":"No channel ID provided in url"
            }
            return jsonify(resp)
        
        messages = db.get_messages_by_channel(channel_id)

        resp = {
            "status":"success",
            "messages":convert_messages(messages)
        }

        return jsonify(resp)

    except Exception as e:
        print "Could not poll messages:", e

def convert_messages(row):
    messages = []
    for item in row:
        message = {
            'sent':item['sent'],
            'message':item['message'],
            'channel_id':item['channel_id'],
            'sender':item['sender'],
            'sender_color':item['sender_color'],
        }

        messages.append(message)
    return messages
