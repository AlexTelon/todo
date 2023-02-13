# Todo App CLI Tool

This is a simple command-line interface for managing tasks in a todo list.

It has a `python app.py` web interface and a `todo` command-line interface. This document will focus on the cli for now.

## Installation

```shell
pip install .
# pip install -e . # if you want to make changes to the code.
```

## Usage

Here are the available commands for managing your todo list:

### `list`

Displays a list of all tasks in your todo list.

Example:
```shell
todo list
```

### `add <title> <description>`

Adds a new task to your todo list with the given title and description.

Example:
```shell
todo add "Example Task" "This is an example task."
```

### `update <id> [--title <title>] [--description <description>] [--completed <true/false>]`

Updates an existing task in your todo list with the given ID. You can update the task's title, description, or completion status using the optional `--title`, `--description`, and `--completed` arguments, respectively.

Example:

```shell
todo update 1 --title "Updated Task" --completed true
```

### `delete <id>`

Deletes an existing task in your todo list with the given ID.

Example:
```shell
todo delete 1
```