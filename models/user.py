from mongoengine import Document,ListField,StringField,URLField,EmailField,connect,DateTimeField,ObjectIdField,BooleanField
import datetime
from bson.objectid import ObjectId
import json
class User(Document):
      
      email=StringField(min_length=6,regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', required=True,unique=True)
      password=StringField(min_length=6, required=True)
      name=StringField(min_length=3, required=True)
      date_modified = DateTimeField(default=datetime.datetime.utcnow)
      online=BooleanField(default=False)
      _id = ObjectIdField(default=ObjectId)
      def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
      
      
      # def __init__(self, name,email,password,online=False):
        
      #   self.email=email
      #   self.password=password
      #   self.name = name
      #   self.online=online
      
    #   def fromMap(map):
    #       import json
    #       data=json.loads(map)
    #       return Band(name=data['name'],votes=data['votes'],id=data['id'])
          