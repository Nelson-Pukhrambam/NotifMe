from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'distant_touch_secret_key_123' 

# Allow cross-origin requests so the cloud server can communicate with the phones
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print(f"Device connected: {request.sid}")
    emit('connection_success', {'status': 'Connected to Digital Living Room!'})

@socketio.on('disconnect')
def handle_disconnect():
    print(f"Device disconnected: {request.sid}")

@socketio.on('send_touch')
def handle_touch(data):
    print(f"Heartbeat received from: {request.sid}")
    # Broadcast the touch to EVERYONE else connected
    emit('receive_touch', {'message': 'Partner sent love!'}, broadcast=True, include_self=False)

if __name__ == '__main__':
    # Cloud providers use the 'PORT' environment variable. 
    # If it doesn't exist (like on your local PC), it defaults to 5000.
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Distant Touch server on port {port}...")
    socketio.run(app, host='0.0.0.0', port=port, allow_unsafe_werkzeug=True)