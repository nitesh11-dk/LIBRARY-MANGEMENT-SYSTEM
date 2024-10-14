# routes/user_routes.py
from flask import Blueprint, request, jsonify, session  # Import session
import sqlite3
import shortuuid
import bcrypt
from flask_session import Session


user_bp = Blueprint('user', __name__)

@user_bp.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    user_id = shortuuid.uuid()  # Generate a unique short ID
    username = data['username']  # Get the username from the request
    password = data['password']   # Get the password from the request

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        try:
            # Insert the user into the database with the username and hashed password
            cursor.execute('INSERT INTO users (id, username, password) VALUES (?, ?, ?)', (user_id, username, hashed_password))
            conn.commit()
            return jsonify({"message": f"User {username} created successfully!", "id": user_id}), 201
        except sqlite3.IntegrityError:
            return jsonify({"error": "Username already exists."}), 400

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        # Fetch both password and user ID
        cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[1]):
            # Create session for the user
            session['username'] = username  # Store username in the session
            user_id = user[0]  # Get user ID
            return jsonify({
                "message": "Login successful!",
                "username": username,
                "user_id": user_id
            }), 200
        else:
            return jsonify({"error": "Invalid username or password."}), 400
        

        
@user_bp.route('/logout', methods=['POST'])
def logout():
    # Clear the session
    session.clear()
    return jsonify({"message": "Logout successful!"}), 200
