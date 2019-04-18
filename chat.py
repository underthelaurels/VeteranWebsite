from flask import Blueprint, jsonify, render_template, request, flash, session, redirect, url_for
from flask import g

import db

chat = Blueprint('chat', __name__, url_prefix='/chat')

