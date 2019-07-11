import sqlite3
import uuid
import time

from flask import Flask, request, Response, redirect, jsonify

from db_wrapper import request_db

db = request_db('db.db')


def add_note(data):
    if ('title' not in data) or ('text' not in data):
        return jsonify({"msg": "Bad request"}), 400
    id = str(uuid.uuid4())
    title = data['title']
    text = data['text']
    date_create = int(time.time())
    date_update = date_create
    db.request_insert_five('Notes', 'id, title, text, date_create, date_update', id, title, text, date_create, date_update)
    return jsonify(id=id), 200


def get_all_notes(data):
    return jsonify({"msg": "Not implemented yet"}), 501


def delete_note(data):
    return jsonify({"msg": "Not implemented yet"}), 501


def update_note(data):
    return jsonify({"msg": "Not implemented yet"}), 501
