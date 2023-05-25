
class MongoManager:
     __instance = None
     DATABASE=None
     @staticmethod 
     def getInstance():
         if MongoManager.__instance == None:
             MongoManager()           
         return MongoManager.DATABASE
     def __init__(self):
        if MongoManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            import pymongo
            from dotenv import load_dotenv
            from mongoengine import connect
            import os
            env_path=os.path.join('/flask','credentials.env')
            load_dotenv(env_path)
            SECRET_PHRASE=os.getenv('STRING_URL')
            from mongoengine import connect
            connect('testDb', username='mongoadmin', password='mongoadmin',host='192.168.1.18', authentication_source='admin',port=27017)
            MongoManager.__instance = pymongo.MongoClient(SECRET_PHRASE)
            MongoManager.DATABASE=MongoManager.__instance['testDb']
    
