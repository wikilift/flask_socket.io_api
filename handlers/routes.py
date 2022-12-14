from main import app,socketio
from flask import  render_template,request
from flask_socketio import send,emit
import json
from cerberus import Validator

# from models.bands import Bands
# from models.band_model import Band


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login',methods=['GET','POST'])
def login():
    
    from .auth.auth_service import signUp
    return signUp(request=request)
    

    

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast = True)




# @socketio.on('join')
# def handleMessage(msg):
#     try:
#         print('Client joined: ' + str(msg))
#         send({'Welcome':msg})
#         emit('active-bands',[json.dumps(x.__dict__) for x in CONST_BANDS.getBands()],broadcast=True)
#     except Exception as e:
#         print(e)

# @socketio.on('delete-band')
# def deleteBand(payload):
#     try:
        
#         obj=json.loads(payload)
#         CONST_BANDS.deleteBand(obj['id'])
#         emit('active-bands',[json.dumps(x.__dict__) for x in CONST_BANDS.getBands()],broadcast=True)
#     except Exception as e:
#         print(e)

# @socketio.on('add-band')
# def addBand(payload):
#     try:
        
#         obj=Band.fromMap(payload)
#         CONST_BANDS.addBand(obj)
#         emit('active-bands',[json.dumps(x.__dict__) for x in CONST_BANDS.getBands()],broadcast=True)
#     except Exception as e:
#         print(e)

# @socketio.on('vote-band')
# def voteBand(payload):
#     try:
        
#         obj=json.loads(payload)
#         CONST_BANDS.voteBand(obj['id'])
#         emit('active-bands',[json.dumps(x.__dict__) for x in CONST_BANDS.getBands()],broadcast=True)
#     except Exception as e:
#         print(e)
   

@socketio.on('message')
def handleMessage(jsonStr):
    try:
        
        data=json.loads(jsonStr)
       
        print('Json: ' + data['message'])
        send(data)
    except Exception as e:
        print(e)
        print('Message: ' + jsonStr)
        send({'message':jsonStr})