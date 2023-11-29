from flask import Flask
from flask import jsonify, request
import json
from task import Task

app = Flask(__name__)
database = {}


# 1
@app.route('/', methods=['GET'])
def sanity():
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response


# 2
@app.route('/add', methods=['POST'])
def addTask():
    # Read the json from the request
    j = json.loads(request.get_json())
    # Create Task instance
    task = Task(**j)
    # We are casting task into a dictionary.
    # We are doing this because we want to store
    # the database into a json later.
    database[task.id] = task.__dict__
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response


# 3
@app.route('/print', methods=['GET'])
def showTasks():
    # TO DO return database in json format
    return json.dumps(database)


# 3.1
@app.route('/print/<name>', methods=['GET'])
def showEmployeeTasks(name):
    # TO DO search for tasks that have the employyes name
    # return them in json format
    answer = {}
    for task in database.values():
        if name == task['name']:
            answer[task['name']] = task
    return json.dumps(answer)


# 3.2
@app.route('/print/pending', methods=['GET'])
def showPendingTasks():
    # TO DO search for tasks that have status not done
    # return them in json format
    answer = {}
    for task in database.values():
        if task['status'] == "completed":
            answer[task['id']] = task
    return json.dumps(answer)


# 3.3
@app.route('/print/completed', methods=['GET'])
def showCompletedTasks():
    # TO DO search for tasks that have status completed
    # return them in json format
    answer = {}
    for task in database.values():
        if task['status'] == "completed":
            answer[task['id']] = task
    return json.dumps(answer)


# 4
@app.route('/delete/<id>', methods=['DELETE'])
def deleteTask(id):
    # TO DO delete the task that has the id id from the database
    if id in database:
        database.pop(id)
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response


# 4.1
@app.route('/delete/all', methods=['DELETE'])
def deleteAllTasks():
    # TO DO clear database
    database.clear()
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response


# 5
@app.route('/update/<id>', methods=['POST'])
def updateTaskStatus(id):
    # TO DO change task status to completed
    if id in database:
        database[id]['status'] = "completed"
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response


# 5.1
@app.route('/update/<id>/<name>', methods=['POST'])
def updateTaskAssignee(id, name):
    # TO DO change task asignee
    if id in database:
        database[id]['name'] = name
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response


# 6
@app.route('/save', methods=['POST'])
def saveTasks():
    # TO DO store database to a json file
    j = json.dumps(database)
    json_file = open("database.json", "w")
    json_file.write(j)
    json_file.close
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response


# 7
@app.route('/load', methods=['POST'])
def loadTasks():
    # TO DO load database from json file
    json_file = open("database.json", "r")
    global database
    database = json.load(json_file)
    json_file.close
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

