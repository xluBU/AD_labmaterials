import flask
import requests
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)

@app.route("/mongo", methods=["GET"])
def mesh_mongo():
    url= "https://europe-west2-ad-labs-328821.cloudfunctions.net/Service_Mesh_Layer_Function"
    req = requests.post(url, json={
        "source": "mongo",

    }, headers={"Content-type": "application/json", "Accept": "text/plain"})
    return(req.content)

@app.route("/google", methods=["GET"])
def mesh_google():
    url= "https://europe-west2-ad-labs-328821.cloudfunctions.net/Service_Mesh_Layer_Function"
    req = requests.post(url, json={
        "source": "google",

    }, headers={"Content-type": "application/json", "Accept": "text/plain"})
    return(req.content)


if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
