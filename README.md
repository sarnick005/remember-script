`remember_script` is a personalized CLI tool for remembering docker git or linux command when you forget(basically a cheap version of man command). Why don't google it? Because ...

Goal

- A simple script that runs when invoked by `remember` command.
- Each command should have an `id`, `tag`, `command` and `description`
- List all commands:
  ```bash
  remember ls
  ```
- List all commands with specific tag:
  ```bash
  remember ls git
  ```
- Search within tag and commands or description keywords:
  ```bash
  remember git stash
  remember docker prune
  ```
- Save a new command:
  ```bash
  remember save "docker compose up" --tag docker --desc "This is the description"
  ```

Tech Stack

- Python
- Sqlite3
- Rich (for pretty CLI output with colored tables)
