import sqlite3

from flask import Flask, request, Response, redirect, jsonify

from db_wrapper import request_db
from functions import (
    add_note,
    get_all_notes,
    delete_note,
    update_note
)

app = Flask(__name__)
db = request_db('db.db')


@app.route('/', methods=['POST', 'GET', 'DELETE', 'UPDATE'])
def index():
    data = request.json
    if request.method == 'POST':
        response = add_note(data)
    elif request.method == 'GET':
        response = get_all_notes(data)
    elif request.method == 'DELETE':
        response = delete_note(data)
    elif request.method == 'UPDATE':
        response = update_note(data)
    return response

