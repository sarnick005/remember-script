from .db import create_db
from .commands import save_command, fetch_commands
import shlex


def parse_input_command(command: str) -> bool:
    parts = shlex.split(command)
    print(parts)
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

    # remember save "docker compose up" --tag docker --desc "This is the description"
    if len(parts) >= 2 and parts[1] == "save":
        try:
            command_str = parts[2]
            tag = None
            desc = ""
            i = 3
            while i < len(parts):
                if parts[i] == "--tag" and i + 1 < len(parts):
                    tag = parts[i + 1]
                    i += 2
                elif parts[i] == "--desc" and i + 1 < len(parts):
                    desc = parts[i + 1]
                    i += 2
                else:
                    i += 1
            if not tag:
                print("Error: --tag is required")
                return False
            save_command(tag, command_str, desc)
            print("Command saved.")
            return True
        except Exception as e:
            print("Error saving command:", e)
            return False

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
