`remember_script` is a personalized CLI tool for remembering docker git or linux command when you forget(basically a cheap version of man command). Why don't google it? Because ...

Goal

- A simple script that runs when invoked by `remember` command.
- Basic usage like `remember git stash`, `remember docker prune` etc command easily by efficient searching based on tags like `git` or `docker`, commands like `stash` or `prune` or simple search any word if it's in database it will show.
- Each command should have an `id`, `tag`, `command` and `description`
- `remember ls` command will print all commands in the database.
- `remember ls git` command will print all git commands in the database.
- `remember save "docker compose up" --tag docker` to add a new command
-

Tech Stack

- Python
- Sqlite3
