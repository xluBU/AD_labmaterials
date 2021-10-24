import flask
import requests
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    url= "https://europe-west2-ad-labs-328821.cloudfunctions.net/helloworld"
    response=requests.get(url)
    return(response.content)

if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)