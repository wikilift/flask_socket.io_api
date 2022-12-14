from db.db_service import MongoManager
myClient=MongoManager.getInstance()




x=MongoManager.getInstance().get_collection('user').find_one()
# for i in x:
#     print(i)
print(x)
