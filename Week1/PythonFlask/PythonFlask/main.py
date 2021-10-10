from flask import Flask,render_template
app=Flask(__name__)

app.route('/')

@app.route('/<color>')
def hello_world_app(color="blue"):
    return render_template('hello.html', color=color)
