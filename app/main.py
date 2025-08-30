from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)
users = {}

@app.route('/')
def home():
    return "🚀 Welcome to DevSecOps API!"

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({'error': 'Missing fields'}), 400

    users[username] = {'email': email}
    return jsonify({'message': f'User {username} created'}), 201

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'username': username, 'email': user['email']}), 200

@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'}), 200

@app.route('/run', methods=['POST'])
def run_command():
    data = request.json
    cmd = data.get('cmd')
    output = subprocess.check_output(cmd, shell=True)
    return jsonify({'output': output.decode('utf-8')}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
