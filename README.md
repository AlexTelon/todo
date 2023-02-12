# Todo App CLI Tool

This is a simple command-line interface for managing tasks in a todo list.

It has a `python app.py` web interface and a `python cli.py` command-line interface. This document will focus on the cli for now.

## Installation

```shell
pip install -r requirements.txt
```

## Usage

Here are the available commands for managing your todo list:

### `list`

Displays a list of all tasks in your todo list.

Example:
```shell
python cli.py list
```

### `add <title> <description>`

Adds a new task to your todo list with the given title and description.

Example:
```shell
python cli.py add "Example Task" "This is an example task."
```

### `update <id> [--title <title>] [--description <description>] [--completed <true/false>]`

Updates an existing task in your todo list with the given ID. You can update the task's title, description, or completion status using the optional `--title`, `--description`, and `--completed` arguments, respectively.

Example:

```shell
python cli.py update 1 --title "Updated Task" --completed true
```

### `delete <id>`

Deletes an existing task in your todo list with the given ID.

Example:
```shell
python cli.py delete 1
```