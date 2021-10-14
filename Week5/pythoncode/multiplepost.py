import pymongo
from pymongo import MongoClient

cluster=MongoClient( "mongodb+srv://xin:1234@advanceddevelopmentunit.g4vl5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["Pythontest"]
collection=db["Students"]

post1={"_id":1, "name": "Lucas","score":5}
post2={"_id":2, "name": "Daniel","score":5}
collection.insert_many([post1,post2])