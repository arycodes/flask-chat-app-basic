# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Dictionary to store user credentials (username: password)
user_credentials = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('credentials')
def handle_credentials(credentials):
    username = credentials['username']
    password = credentials['password']

    # Check if the provided username exists and the password is correct
    if username in user_credentials and user_credentials[username] == password:
        emit('authentication_status', {'status': 'success'})
        print(f'User {username} authenticated successfully!')
    else:
        emit('authentication_status', {'status': 'failure'})
        print(f'Authentication failure for user {username}.')

@socketio.on('message')
def handle_message(data):
    username = data['username']
    message = data['message']
    print(f'Received message from {username}: {message}')
    emit('message', {'username': username, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
