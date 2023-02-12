import sqlite3

DATABASE = 'tasks.db'

class Task:
    def __init__(self, id, title, description, completed):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed


def get_tasks():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    rows = c.fetchall()
    tasks = []
    for row in rows:
        task = Task(*row)
        tasks.append(task)
    conn.close()
    return tasks


def create_task(task):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)',
                   (task.title, task.description, task.completed))
    task_id = cursor.lastrowid
    conn.commit()

    conn.close()

    return task_id


def delete_task(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()

    conn.close()


def try_setup_db():
    """Create the database and the tasks table if they don't exist."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
    if not cursor.fetchone():
        cursor.execute('''
            CREATE TABLE tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        ''')

    conn.commit()
    conn.close()


def get_task(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('SELECT id, title, description, completed FROM tasks WHERE id = ?', (id,))
    task = cursor.fetchone()

    conn.close()

    return task

def update_task(task):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('UPDATE tasks SET title=?, description=?, completed=? WHERE id=?',
                   (task.title, task.description, task.completed, task.id))
    conn.commit()

    conn.close()
