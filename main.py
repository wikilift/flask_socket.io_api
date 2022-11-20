from flask import Flask
from flask_socketio import SocketIO,send

app = Flask(__name__)
app.config['SECRET_KEY']='secret!'
socketio=SocketIO(app=app)

from handlers import routes


