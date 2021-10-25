import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
import os
import requests
import json

def get_inventory_list(request):
  client = MongoClient("mongodb+srv://xin:12345@advanceddevelopmentunit.g4vl5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

  db=client.db01

  myCursor=db.inventory.find({})

  list_cur=list(myCursor)
  print(list_cur)

  json_data=dumps(list_cur)

  return json_data
 

