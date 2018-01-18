from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask.ext.heroku import Heroku

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:start@localhost/temp2'
heroku = Heroku(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    complete = db.Column(db.Boolean, default=False)

    def __init__(self, title):
        self.title = title


class TodoSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'title', 'complete')


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


# endpoint to create new task
@app.route("/todo", methods=["POST"])
def add_todo():
    title = request.json['title']
    # email = request.json['email']
    new_todo = Todo(title)

    db.session.add(new_todo)
    db.session.commit()

    return todo_schema.jsonify(new_todo)


# endpoint to show all tasks
@app.route("/todo", methods=["GET"])
def get_todo():
    all_todos = Todo.query.all()
    result = todos_schema.dump(all_todos)
    return jsonify(result.data)


# endpoint to get task detail by id
@app.route("/todo/<id>", methods=["GET"])
def todo_detail(id):
    todo = Todo.query.get(id)
    return todo_schema.jsonify(todo)


# endpoint to update a task
@app.route("/todo/<id>", methods=["PUT"])
def todo_update(id):
    todo = Todo.query.get(id)
    title = request.json['title']
    complete = request.json['complete']

    todo.title = title
    todo.complete = complete

    db.session.commit()
    return todo_schema.jsonify(todo)


# endpoint to delete a task
@app.route("/todo/<id>", methods=["DELETE"])
def todo_delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()

    return todo_schema.jsonify(todo)


if __name__ == '__main__':
    app.run(debug=True)