from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print('dsfsdfsdfsdfffffffffffffffffffffffffffffffffffffffffffffffffff')
    emit('after connect',  {'data':'Lets dance'})

if __name__ == '__main__':
    socketio.run(app, debug=True, port=65432, host='0.0.0.0')