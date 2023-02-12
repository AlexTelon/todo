import sqlite3

DATABASE = 'tasks.db'

def get_tasks():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('SELECT id, title, description, completed FROM tasks')
    tasks = cursor.fetchall()

    conn.close()

    return tasks

def create_task(title, description):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
    conn.commit()

    conn.close()

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

def update_task(id, title, description, completed):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?', (title, description, completed, id))

    conn.commit()
    conn.close()