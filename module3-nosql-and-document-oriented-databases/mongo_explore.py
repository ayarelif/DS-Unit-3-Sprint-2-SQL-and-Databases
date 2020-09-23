from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pandas


load_dotenv()

DB_USER = os.getenv("MONGO_USER_2", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD_2", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME_2", default="OOPS")

uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", uri)

client =MongoClient(uri)
print("URI:", uri)


# set the DB to Analytics
analytics_db = client.sample_analytics

# Acces a specific collection

transaction=analytics_db.transactions
print(transaction.count_documents({}))

# get all the customers into dataframe

customers=analytics_db.customers
all_customers=customers.find()

import pandas as pd 

df=pd.DataFrame(all_customers)

### write JSON DATA from RPG DB to Mongo
import json
# read json file 
with open ('test_data_json.txt') as json_file:
     rpg_data=json.load(json_file)

#create an rpg_data database
my_db=client.rpg_data

#create a characters collection in the rpg_data DB
character_table=my_db.characters

#insert the JSON data into characters collection

character_table.insert_many(rpg_data)
print(character_table.count_documents({}))


