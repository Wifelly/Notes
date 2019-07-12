import sqlite3
import uuid
import time

from flask import Flask, request, Response, redirect, jsonify

from db_wrapper import request_db

db = request_db('db.db')


def add_note(data):
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    if ('title' not in data) or ('text' not in data):
        return jsonify({"msg": "Bad request"}), 400
    id = str(uuid.uuid4())
    title = data['title']
    text = data['text']
    if len(title) > 30 or len(text) > 500:
        return jsonify({"msg": "Bad request"}), 400
    date_create = int(time.time())
    date_update = date_create
    db.request_insert_five('Notes', 'id, title, text, date_create, date_update', id, title, text, date_create, date_update)
    return jsonify({"status": "OK"}), 200


def get_all_notes(data):
    request = db.request_select('*', 'Notes')
    response = []
    for item in request:
        print(item)
        response.append(
            {
                'id': item[0],
                'title': item[1],
                'text': item[2],
                'date_create': item[3],
                'date_update': item[4]
            }
        )
    return jsonify(response), 200


def delete_note(data):
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    if 'id' not in data:
        return jsonify({"msg": "Bad request"}), 400
    id = data['id']
    db.request_delete('Notes', 'id', id)
    return jsonify({"status": "OK"}), 200


def update_note(data):
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    if ('id' not in data) or ('title' not in data) or ('text' not in data):
        return jsonify({"msg": "Bad request"}), 400
    id = data['id']
    title = data['title']
    text = data['text']
    db.request_update('Notes', 'title', title, 'id', id)
    db.request_update('Notes', 'text', text, 'id', id)
    return jsonify({"status": "OK"}), 200
