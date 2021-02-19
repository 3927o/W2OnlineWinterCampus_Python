from flask import Flask, url_for, redirect, request


app = Flask(__name__)


@app.route("/get_file_url/<string:filename>")
def get_file_url(filename):
    return url_for("static", filename=filename)


@app.route("/get_file/<string:filename>")
def get_file(filename):
    return redirect(url_for("static", filename=filename))


@app.route("/get_url/<value>")
def test(value):
    "%s%s"%request.host%url_for()
    return request.host + url_for("test", value=value)


app.run(debug=True)
