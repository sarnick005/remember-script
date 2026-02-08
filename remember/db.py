import sqlite3
import uuid
import os
DB_FILE = "remember.db"


def seed_db(conn: sqlite3.Connection) -> bool:
    try:
        cursor = conn.cursor()
        id = str(uuid.uuid4())

        cursor.execute("""INSERT INTO remember (id, tag, command, description)
               VALUES (?, ?, ?, ?)""",
            (id, "ls", "remember ls", "All remember commands on this system"),
        )

        conn.commit()
        print("DB seeded")
        return True
    except Exception as e:
        print(f"Seed error: {str(e)}")
        return False


def create_db() -> bool:
    try:
        db_already_exists = os.path.exists(DB_FILE)
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS remember(id TEXT,tag TEXT,command TEXT,description TEXT)")

        conn.commit()
        if not db_already_exists:
            print("Database created successfully.")
            return seed_db(conn)
        else:
            print("Database already exists.")
            return True

    except Exception as e:
        print(f"DB creation error: {str(e)}")
        return False

    finally:
        conn.close()


if __name__ == "__main__":
    create_db()
