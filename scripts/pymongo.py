import os
import pymongo
from pymongo import MongoClient
from bson import objectid
from bson.objectid import ObjectId
from datetime import datetime
import pprint
#######################

key_3 =  str(os.environ.get('MONGODB_SRV'))

client = MongoClient(key_3)
db = client.galeria
collection = db.videos

pprint.pprint(collection.find_one({"current_user_id": "2"})) # get the last video of one user by its id

