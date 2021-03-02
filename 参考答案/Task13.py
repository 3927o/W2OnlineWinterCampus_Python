from flask import Flask, session


app = Flask(__name__)
app.secret_key = "secret_key"


@app.route("/login/<string:username>")
def login(username):
    session["user"] = username
    return "Login Succeed"


@app.route("/logout")
def logout():
    session.pop("user")
    return "Logout Succeed"


@app.route("/")
def index():
    username = session.get("user") or "Customer"
    return f"Hello! {username}."


app.run(debug=True)
