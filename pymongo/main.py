from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017")
    print("Connecting")
    print("Info: ", client.server_info())
except:
    print("Could not connect")

db = client.test_db

print("Databases: ", client.list_database_names())

collection = db.test_collection

# To delete a collection
# collection.drop()

print("Collections: ", db.list_collection_names())

data = {
    "name": "test",
    "title": "test",
    "age": 24
}

insert_res = collection.insert_one(data)

print("Data inserted", insert_res)

find_res = collection.find()

for res in find_res:
    print(res)
