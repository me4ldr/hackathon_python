from flask import Blueprint, jsonify
from flask import Flask, request, jsonify,send_file
from flask_cors import CORS
import os

user_role_service_bp = Blueprint("user_role_service", __name__)

# Mock user data (replace with a database in a real application)
users = {
    'teacher': [{'username': 'teacher1', 'password': '1234'}, {'username': 'teacher2', 'password': '1234'}],
    'facilitator': [{'username': 'facilitator1', 'password': '1234'}, {'username': 'facilitator2', 'password': '1234'}],
    'student': [{'username': 'Danny', 'password': '123'},{'username': 'Harry', 'password': '123'},{'username': 'Alice', 'password': '123'}]

}


@user_role_service_bp.route('/api/login', methods=['POST'])
def login():
    print("login...");
    data = request.get_json()
    user_type = data.get('userType')
    username = data.get('username')
    password = data.get('password')

    print("login...",username, password, user_type);
    if user_type in users:
        user_group = users[user_type]
        for user in  user_group:
            if username == user['username'] and password == user['password']:
                return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid user type'}), 401

    return jsonify({'error': 'Invalid username or password'}), 401
