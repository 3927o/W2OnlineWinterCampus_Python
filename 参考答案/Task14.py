import time

from flask import Flask, request


app = Flask(__name__)
tasks = list()


class Task:
    max_id = 0

    def __init__(self, content):
        self.id = Task.max_id + 1
        self.content = content
        self.status = False
        self.start_time = time.time()
        self.end_time = None
        Task.max_id += 1

    def to_json(self):
        return {
            "id": self.id,
            "content": self.content,
            "status": int(self.status),
            "start_time": self.start_time,
            "end_time": self.end_time
        }

    @classmethod
    def list_to_json(cls, tasks):
        return [task.to_json() for task in tasks]


def make_resp(data, status=200, message="success"):
    return {
        "status": status,
        "message": message,
        "data": data
    }


@app.route("/tasks", methods=["GET", "POST"])
def task_list():
    if request.method == "GET":
        data = Task.list_to_json(tasks)
        resp = make_resp(data)
        return resp
    if request.method == "POST":
        content = request.form['content']
        new_task = Task(content)
        tasks.append(new_task)

        data = new_task.to_json()
        resp = make_resp(data)
        return resp


@app.route("/task/<int:id>", methods=["GET", "PUT", "DELETE"])
def task(id):
    if request.method == "GET":
        return make_resp(tasks[id].to_json())
    if request.method == "PUT":
        tasks[id].status = not tasks[id].status
        return make_resp(tasks[id].to_json())
    if request.method == "DELETE":
        tasks.remove(tasks[id])
        return make_resp({})


app.run(debug=True)
