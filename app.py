from flask import Flask, redirect, request, render_template, url_for

import database as db

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        db.create_task(title, description)
        return redirect(url_for('tasks'))

    tasks = db.get_tasks()

    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    # Retrieve a single task by its ID and render it in a template
    task = db.get_task(id)
    return render_template('task.html', task=task)

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    # Update a task by its ID in the database and redirect to the task details page
    title = request.form.get('title')
    description = request.form.get('description')
    completed = 'completed' in request.form
    db.update_task(id, title, description, completed)
    return redirect(url_for('get_task', id=id))

@app.route('/tasks/<int:id>', methods=['POST'])
def update_task_with_method(id):
    # Handle a PUT request sent as a POST request with a _method parameter
    if request.form.get('_method') == 'put':
        return update_task(id)
    else:
        return redirect(url_for('get_task', id=id))


@app.route('/tasks/<int:id>', methods=['POST'])
def delete_task_with_method(id):
    # Handle a DELETE request sent as a POST request with a _method parameter
    if request.form.get('_method') == 'delete':
        return delete_task(id)
    else:
        return redirect(url_for('get_task', id=id))

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    db.delete_task(id)
    return redirect(url_for('tasks'))


if __name__ == '__main__':
    db.try_setup_db()
    app.run(debug=True)
