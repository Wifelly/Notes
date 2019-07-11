import sqlite3

from flask import Flask, request, Response, redirect, jsonify

from db_wrapper import request_db

db = request_db('db.db')


def add_note(data):
    return jsonify({"msg": "Not implemented yet"}), 501


def get_all_notes(data):
    return jsonify({"msg": "Not implemented yet"}), 501


def delete_note(data):
    return jsonify({"msg": "Not implemented yet"}), 501


def update_note(data):
    return jsonify({"msg": "Not implemented yet"}), 501
