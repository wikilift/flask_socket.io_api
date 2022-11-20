from main import app,socketio
from flask import  render_template
from flask_socketio import send

@app.route('/')
def index():
    return render_template('index.html')



@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast = True)