from flask import Flask, make_response


app = Flask(__name__)


@app.route('/learn_response')
def response():
    resp = make_response('Response OK', 200)
    resp.headers['Some data'] = 'data'
    return resp


if __name__ == '__main__':
    app.run()