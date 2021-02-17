from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
def first():
    return "Hello Flask"


@app.route("/index")
def index():
    return "Index Page"


@app.route("/hello/<string:username>")
def hello(username):
    return f"Hello, {username}"


@app.route("/hello/<float:value>")
def calculate(value):
    return str(39*value)


@app.route("/get_welcome_url/<string:username>")
def welcome_url(username):
    return url_for("hello", username=username)


@app.route("/delete", methods=["POST"])
def delete():
    return "POST SUCCEED"


app.run(debug=True)
