#!/usr/bin/python3
"""
Simple RESTful API developed using Flask framework.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Root endpoint returning a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """
    Returns a list of all stored usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """
    Returns operational status of the API.
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Returns user details for a given username or 404 if not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user from JSON request body.
    """
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
