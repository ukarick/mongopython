import mongo
import datetime
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection
print("###########Test write documentation########")
post = {"author": "Ukrit", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
print("###########Test get single documentation#######")
print(posts.find_one({"_id": post_id}))