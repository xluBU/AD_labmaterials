from pymongo import MongoClient
from bson.json_util import dumps
from flask import Blueprint, request, jsonify
import os
import requests
import json
# end imports

# Cloud function to get a forum posts from mongo
def get_mongodb_items(request):

    client = MongoClient("mongodb+srv://xin:12345@advanceddevelopmentunit.g4vl5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    # connect to the db
    db = client.test
    myCursor = None

    # create queries

    title_query = {"title": {"$eq": "Man walks on the moon"}}

    author_query = {"author": {"$eq": "Faker"}}

    dateCreated_query = {"dateCreated": {"$eq": 2019}}

    myCursor = db.test.find({"$and": [title_query, author_query, dateCreated_query]})



    list_cur = list(myCursor)
    print(list_cur)

    json_data = dumps(list_cur)



    return json_data
