import pymongo

#!StringURL
myclient= pymongo.MongoClient('mongodb://admin:asdasd@192.168.1.18:27017/?authMechanism=DEFAULT')

#!SelectDatabase
myDb=myclient['testDb']

#!print database names
print(myclient.list_database_names())

#!pointer to collection ref
mycol = myDb["testCol"]

#!dictionari to insert
mydict = { "name": "John", "address": "Highway 37" }

#!print collection names
print(myDb.list_collection_names())

"""
#!Single insert
x = mycol.insert_one(mydict)
#return id
print(x.inserted_id)
"""


"""
#!Insert multiple 
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#?print list of the _id values of the inserted documents:
print(x.inserted_ids)
"""

"""
#!Insert Multiple Documents, with Specified IDs
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#?print list of the _id values of the inserted documents:
print(x.inserted_ids)
"""

"""
#!Find One
#?To select data from a collection in MongoDB, we can use the find_one() method.
x = mycol.find_one()

print(x)
"""

"""
#!Find All
#?To select data from a table in MongoDB, we can also use the find() method.
for x in mycol.find():
  print(x)
"""

"""
#!Return Only Some Fields
#?The second parameter of the find() method is an object describing which fields to include in the result.
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)
 """ 
 
"""
#*You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):
#!This example will exclude "address" from the result:
for x in mycol.find({},{ "address": 0 }):
  print(x)
"""

"""
#!When finding documents in a collection, you can filter the result by using a query object.
#?The first argument of the find() method is a query object, and is used to limit the search.
myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
"""

"""
#!To make advanced queries you can use modifiers as values in the query object.
#?to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}
myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
"""  

"""
#!Filter With Regular Expressions
#?To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}
myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
"""

"""
#!Use the sort() method to sort the result in ascending or descending order.
#?The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).
mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)

#?Use the value -1 as the second parameter to sort descending.
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)
"""

"""
#!Delete Document
#?To delete one document, we use the delete_one() method.

#?The first parameter of the delete_one() method is a query object defining which document to delete.
myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)
"""

"""
#!Delete Many Documents
#?To delete more than one document, use the delete_many() method.
#?The first parameter of the delete_many() method is a query object defining which documents to delete.
myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")
"""

"""
#!Delete All Documents in a Collection
#?To delete all documents in a collection, pass an empty query object to the delete_many() method:
x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")
"""

"""
#!Delete Collection
#?You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
mycol.drop()
"""

"""
#!Update Collection
#?You can update a record, or document as it is called in MongoDB, by using the update_one() method.
#?The first parameter of the update_one() method is a query object defining which document to update.
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#*print "customers" after the update:
for x in mycol.find():
  print(x)
"""

"""
#!Update Many
#?To update all documents that meets the criteria of the query, use the update_many() method.
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")
"""

"""
#!Limit the Result
#?To limit the result in MongoDB, we use the limit() method.
#?The limit() method takes one parameter, a number defining how many documents to return.
myresult = mycol.find().limit(5)

#*print the result:
for x in myresult:
  print(x)
"""
