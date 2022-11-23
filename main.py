from flask import Flask
from flask_socketio import SocketIO
# from models.bands import Bands

app = Flask(__name__)
app.config['SECRET_KEY']='secret!'
socketio=SocketIO(app=app)

from handlers import routes