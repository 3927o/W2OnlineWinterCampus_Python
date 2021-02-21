from flask import Flask, request


app = Flask(__name__)


@app.route("/get_form_data", methods=["POST"])
def get_form():
    return str(request.form.to_dict())


@app.route("/get_args")
def get_args():
    return str(request.args.to_dict())


@app.route("/get_request_info")
def get_info():
    return f"""
    request path: {request.path},
    request method: {request.method}
    """


@app.route("/upload_file", methods=["POST"])
def get_file():
    f = request.files["file"]
    f.save(f.filename)
    return "Upload Succeed!"


@app.route("/get_cookies")
def get_cookies():
    resp = ""
    for i in request.cookies.items():
        resp += f"{i} \n"
    return resp


app.run(debug=True)
