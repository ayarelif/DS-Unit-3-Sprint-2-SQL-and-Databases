

# BG_URI="mongodb+srv://elifayar:<password>@clusters.lcjcx.mongodb.net/<dbname>?retryWrites=true&w=majority")
# client = pymongo.MongoClient(DB_URI)
# db = client.test

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)



client =MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
print("DATABASES", client.list_database_names())

db = client.my_test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)
print("DOCUMENTS COUNT:", collection.count_documents({}))

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
    "parents": ['Pikachu',"Raichu"],
    "other_attr": {
        "a":1,
        "b":2,
        "c":3
    }
})
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))

#from pprint import pprint
#breakpoint()
#dir(collection)