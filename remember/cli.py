from .db import create_db
from .commands import save_command, fetch_commands

def parse_input_command(command: str) -> bool:
    parts = command.split()

    if not parts:
        return False

    if parts[0] != "remember":
        print("Unknown command")
        return False

    # remember ls
    if len(parts) == 2 and parts[1] == "ls":
        fetch_commands("ls")
        return True

    # remember ls git
    if len(parts) == 3 and parts[1] == "ls":
        fetch_commands(parts[2])
        return True

    # # remember save <tag> <command...>
    # if len(parts) >= 4 and parts[1] == "save":
    #     tag = parts[2]
    #     command_str = " ".join(parts[3:])
    #     save_command(tag, command_str, "User saved command")
    #     return True

    # remember git
    if len(parts) == 2:
        fetch_commands(parts[1])
        return True

    # remember git stash
    if len(parts) >= 3:
        tag = parts[1]
        search_term = " ".join(parts[2:])
        fetch_commands(tag, search_term)
        return True

    print("Invalid remember command")
    return False
