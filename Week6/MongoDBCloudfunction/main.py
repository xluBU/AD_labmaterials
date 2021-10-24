# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from flask import Flask, render_template, request, jsonify,redirect
import json
import requests
from google.auth.transport import requests as grequests
from google.cloud import datastore
import google.oauth2.id_token
import pymongo

firebase_request_adapter = grequests.Request()

# [START gae_python38_datastore_store_and_fetch_user_times]
# [START gae_python3_datastore_store_and_fetch_user_times]
datastore_client = datastore.Client()

# [END gae_python3_datastore_store_and_fetch_user_times]
# [END gae_python38_datastore_store_and_fetch_user_times]
app = Flask(__name__)


# [START gae_python38_datastore_store_and_fetch_user_times]
# [START gae_python3_datastore_store_and_fetch_user_times]
def store_time(email, dt):
    entity = datastore.Entity(key=datastore_client.key('User', email, 'visit'))
    entity.update({
        'timestamp': dt
    })

    datastore_client.put(entity)


def fetch_times(email, limit):
    ancestor = datastore_client.key('User', email)
    query = datastore_client.query(kind='visit', ancestor=ancestor)
    query.order = ['-timestamp']

    times = query.fetch(limit=limit)

    return times

mongoClient = pymongo.MongoClient(
   "mongodb+srv://coxl4:1234@cluster0.mans7.mongodb.net/test?retryWrites=true&w=majority")
mongoDB = mongoClient['test']


# Stores the post into Mongo collection
def store_post_mongodb(title, author, content, dateCreated, thumbnail):
    collection = mongoDB['test']
    # email will not be added, as author parameter will be used to identify individual users posts
    json_data = {"title": title, "author": author, "dateCreated": dateCreated, "thumbnail": thumbnail,
                 "content": content}
    collection.insert_one(json_data).inserted_id    


@app.route('/')
def root():
    # Verify Firebase auth.
    id_token = request.cookies.get("token")
    error_message = None
    claims = None
    times = None

    if id_token:
        try:
            # Verify the token against the Firebase Auth API. This example
            # verifies the token on each page load. For improved performance,
            # some applications may wish to cache results in an encrypted
            # session store (see for instance
            # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
            claims = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter)

            store_time(claims['email'], datetime.datetime.now())
            times = fetch_times(claims['email'], 10)

        except ValueError as exc:
            # This will be raised if the token is expired or any other
            # verification checks fail.
            error_message = str(exc)

    return render_template(
        'index.html',
        user_data=claims, error_message=error_message, times=times)

@app.route('/uploadfile')
def uploadfile():
    # Verify Firebase auth.
    id_token = request.cookies.get("token")
    error_message = None
    claims = None
    times = None

    if id_token:
        try:
            # Verify the token against the Firebase Auth API. This example
            # verifies the token on each page load. For improved performance,
            # some applications may wish to cache results in an encrypted
            # session store (see for instance
            # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
            claims = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter)

            store_time(claims['email'], datetime.datetime.now())
            times = fetch_times(claims['email'], 10)

        except ValueError as exc:
            # This will be raised if the token is expired or any other
            # verification checks fail.
            error_message = str(exc)
    else:
        return redirect("/")


    return render_template(
        'uploadfile.html',
        user_data=claims, error_message=error_message, times=times)

@app.route('/forum')
def forumDatastore():
    # Verify Firebase auth.
    id_token = request.cookies.get("token")
    error_message = None
    claims = None
    times = None

    if id_token:
        try:
            # Verify the token against the Firebase Auth API. This example
            # verifies the token on each page load. For improved performance,
            # some applications may wish to cache results in an encrypted
            # session store (see for instance
            # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
            claims = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter)

            store_time(claims['email'], datetime.datetime.now())
            times = fetch_times(claims['email'], 10)
           

        except ValueError as exc:
            # This will be raised if the token is expired or any other
            # verification checks fail.
            error_message = str(exc)
    else:
        return redirect("/")


    return render_template(
        'forumbase.html',
        user_data=claims, error_message=error_message, times=times)


@app.route('/forum-cloudfunc')
def forum_cloudfunc():
    url = "https://europe-west2-ad-labs-328821.cloudfunctions.net/mongodbdisplay"

    uResponse = requests.get(url)

    jResponse = uResponse.text
    data = json.loads(jResponse)

    return render_template('forumbase.html', data=data)  

@app.route('/createpost', methods=['POST'])
def createPost():
    title = request.form['title']
    content = request.form['content']
    dateCreated = datetime.datetime.now().year
    thumbnail = ""

    if title and content:
        store_post_mongodb(title, "Admin", content, dateCreated, thumbnail)
    return jsonify({'message': "Post submitted!"})


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
