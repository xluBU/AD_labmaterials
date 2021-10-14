import flask
import json

from flask import request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

app = flask.Flask(__name__)

cluster = MongoClient(
    "mongodb+srv://xin:1234@advanceddevelopmentunit.g4vl5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Pythontest"]
collection = db["Students"]

def get_mongodb_items():
    # Search data from Mongodb

    myCursor = None
    # create queries
    title_query = {"Unit title": {"$eq": "IoT Unit"}}
    author_query = {"Unit leader": {"$eq": "Xin"}}
    dateCreated_query = {"dateCreated": {"$eq": 2021}}

    myCursor = collection.find({"$and": [title_query, author_query, dateCreated_query]})
    list_cur = list(myCursor)
    print(list_cur)
    json_data = dumps(list_cur)
    return json_data

def store_mongodb(Unittitle, Unitleader, content, dateCreated, thumbnail):
  # Write to MongoDB
  json_data = {"Unit title": Unittitle, "Unit leader": Unitleader, "dateCreated": dateCreated, "thumbnail": thumbnail, "content": content}
  collection.insert_one(json_data)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Unit information</h1>
              <p>Please select the Unit</p>'''

@app.route('/unit')
def Post_Mongo():
    store_mongodb('IoT Unit', 'Xin', 'Welcome to IoT Unit', 2021, ',')
    return "done"


@app.route('/display', methods=['GET'])
def display():
    jResponse=get_mongodb_items()
    data=json.loads(jResponse)
    return jsonify(data)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)