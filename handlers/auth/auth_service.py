from flask import make_response
from db.db_service import MongoManager
from cerberus import Validator
from models.user import User
import json
db=MongoManager.getInstance().get_collection('user')
def signUp(request):
    schema = {'email': {'type': 'string', 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', 'required': True,'minlength':3},'password': {'type': 'string', 'required': True},'name': {'type': 'string', 'required': True}}
    v = Validator(schema)
    v.validate(request.args)
    if(len(v.errors)>0):
        return make_response(json.dumps({"created":False,"errors":v.errors},indent=2), 400) 
    try:
        u=User(**request.args)
        if db.count_documents(filter={'email':u.email},limit=1)==0:
            #TODO: encrypt password
            import bcrypt
         
            u.password=(bcrypt.hashpw(u.password.encode('utf8'),bcrypt.gensalt())).decode('utf8')
            u.save()
            
            return make_response(json.dumps({"created":True,"msg":"user created"},indent=4), 200)
        return  make_response(json.dumps({"created":False,"msg":"wrong credentials"},indent=4), 400)
    except Exception as e:
        print(e)
        return  make_response(json.dumps({"created":False,"msg":"fatal error"},indent=4), 500)
     
   