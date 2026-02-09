import sqlite3
import uuid

from remember.rich_cli import display_output
from .db import DB_FILE


def save_command(tag: str, command: str, description: str) -> bool:
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        id = str(uuid.uuid4())

        cursor.execute(
            """INSERT INTO remember (id, tag, command, description)
               VALUES (?, ?, ?, ?)""",
            (id, tag, command, description),
        )

        conn.commit()
        return True

    except Exception as e:
        print(f"Save error: {str(e)}")
        return False

    finally:
        conn.close()


def fetch_commands(tag: str, command: str = None):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        if command:
           res = cursor.execute("SELECT * FROM remember WHERE tag = ? COLLATE NOCASE AND (command LIKE ? OR description LIKE ? COLLATE NOCASE)",
                                (tag, f"%{command}%", f"%{command}%"))
        else:
            res = cursor.execute("SELECT * FROM remember WHERE tag = ?",(tag,))
        rows = res.fetchall()
        display_output(f"Displaying {tag} commands", rows)
    except Exception as e:
        print(f"Fetch error: {str(e)}")
    finally:
        conn.close()

def fetch_all_commands():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        res = cursor.execute("SELECT * FROM remember ORDER BY tag ASC")
        rows = res.fetchall()
        display_output("Displaying all commands", rows)
    except Exception as e:
        print(f"Fetch error: {str(e)}")
    finally:
        conn.close()
