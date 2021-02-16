from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/index")
def index():
    return "Index Page"


app.run()
