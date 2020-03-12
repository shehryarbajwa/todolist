from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from .database.models import setup_db, Todo, db_drop_and_create_all
import os
import json
from sqlalchemy import asc

template_dir = os.path.abspath('../../frontend/templates')
styles_dir = os.path.abspath('../../frontend/static')

app = Flask(__name__, template_folder=template_dir, static_folder=styles_dir)
app.secret_key = 'todoapp'
setup_db(app)

#Run this at setup
db_drop_and_create_all()

@app.route('/todos', methods=['GET'])
def view_todo():
    todos = list(map(Todo.format, Todo.query.all()))
    return jsonify({
        'success': True,
        'todos': todos
    })


@app.route('/todos/create', methods=['POST'])
def create_todo():
    if request.data:
        data = json.loads(request.data)
        title = data.get('title', None)
        description = data.get('description', None)
        due_date = data.get('date', None)
        due_date_to_str = str(due_date)
        todo = Todo(title=title, description=description, completed=False, date=due_date_to_str)

        Todo.insert(todo)
        return jsonify({
            'success': True
        })
    else:
        abort(422)


@app.route('/todos/<int:todo_id>', methods=['PATCH'])
def update_todo(todo_id):
    if request.data:
        data = json.loads(request.data)
        title = data.get('title', None)
        description = data.get('description', None)
        due_date = data.get('date', None)
        todo = Todo.query.filter_by(id=todo_id).one_or_none()
        
        if todo is None:
            abort(404)
        if title is None:
            abort(400)
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
        if due_date is not None:
            todo.date = due_date
        
        todo.update()

        return jsonify({
            'success': True
        })
    else:
        abort(422)

@app.route('/todos/<int:todo_id>/completed', methods=['POST'])
def task_completed(todo_id):
    if request.data:
        completed = json.loads(request.data)['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        todo.update()
        return redirect(url_for('index'))
    
    else:
        abort(422)


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo_list_query = Todo.query.get(todo_id)
    if todo_list_query:
        todo_list_query.delete()
        return jsonify({
            'success': True
        })
    else:
        abort(404)

@app.route('/refresh')
def refresh_todo():
    return redirect(url_for('index'))


@app.route('/')
def index():
    todos = Todo.query.all()
    completed_todos = Todo.query.filter_by(completed=True).all()
    upcoming_tasks = Todo.query.order_by(Todo.date.asc()).limit(10).all()
    
    return render_template('/index.html', todos=todos, completed_todos=completed_todos, upcoming_tasks=upcoming_tasks)

#Error Handling

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "Unprocessable"
                    }), 422

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource not found"
    
    }), 404

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        'success': False,
        'error': 401,
        'message': 'Unauthorized'
    } , 401)

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'Method not allowed'
    }, 405)

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'Internal Server Error'
    }, 500)

if __name__ == '__main__':
    app.run()