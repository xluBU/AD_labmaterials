import pymongo
from pymongo import MongoClient

cluster=MongoClient( "mongodb+srv://xin:1234@advanceddevelopmentunit.g4vl5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["Pythontest"]
collection=db["Students"]

results=collection.find({"name":"Lucas"})
for result in results:
    print(result)

oneresult= collection.find_one({"_id":0})
print(oneresult)

delete_results=collection.delete_one({"_id":0})

all_result=collection.find({})
for x in all_result:
    print(x)

update_result=collection.update_one({"_id":2},{"$set":{"name":"Wang"}})

oneresult= collection.find_one({"_id":2})
print(oneresult)