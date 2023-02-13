import click
import database
from database import Task

@click.group()
def todo():
    pass

@todo.command()
def list():
    tasks = database.get_tasks()
    for task in tasks:
        click.echo(f'{task.id}: {task.title} {task.description} {task.completed}')

@todo.command()
@click.argument('id')
@click.option('--title', prompt=True, help='Title of the task')
@click.option('--description', prompt=True, help='Description of the task')
@click.option('--completed', default=False, is_flag=True, help='Mark the task as completed')
def update(id, title, description, completed):
    database.update_task(id, title, description, completed)
    click.echo(f'Task {id} updated!')

@todo.command()
@click.argument('title')
@click.argument('description')
def add(title, description):
    task = Task(
        id=None,
        title=title,
        description=description,
        completed=False
    )
    database.create_task(task)
    click.echo('Task added successfully.')

@todo.command()
@click.argument('id')
def delete(id):
    database.delete_task(id)
    click.echo(f'Task {id} deleted!')

if __name__ == '__main__':
    database.try_setup_db()