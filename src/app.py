from flask import Flask, request
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/guido/Desktop/python-flask-api-tutorial-master/src/database/test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    

@app.route('/', methods=['GET'])
def home():
    all_todos = Todo.query.all()
    todos_list = []
    for todo in all_todos: todos_list.append([{"id": todo.id, "task": todo.task}])
    return jsonify({"todos": todos_list})
from flask import request

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    new_todo = Todo(task=request_body)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify(todos)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return 'Invalid position', 400
    del todos[position]
    return jsonify(todos)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=3245, debug=True)