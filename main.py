from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
# from models.bands import Bands

app = Flask(__name__)
CORS(app)
socketio=SocketIO(app=app)

from handlers import routes