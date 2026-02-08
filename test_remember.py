import os
import sqlite3
import unittest
from remember.db import create_db
from remember.commands import save_command

DB_FILE = "remember.db"


class TestRememberScript(unittest.TestCase):

    def setUp(self):
        """Runs before every test"""
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)

    def tearDown(self):
        """Runs after every test"""
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)

    def test_create_db(self):
        """Database should be created successfully"""
        result = create_db()
        self.assertTrue(result)
        self.assertTrue(os.path.exists(DB_FILE))

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Check table exists
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='remember'"
        )
        table = cursor.fetchone()

        conn.close()

        self.assertIsNotNone(table)

    def test_save_command(self):
        """Saving a command should insert into DB"""
        create_db()

        result = save_command(
            tag="git",
            command="git stash list",
            description="List stashes"
        )

        self.assertTrue(result)

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM remember WHERE tag = 'git'")
        rows = cursor.fetchall()

        conn.close()

        self.assertEqual(len(rows), 1)

    def test_multiple_commands(self):
        """Should store multiple commands correctly"""
        create_db()

        save_command("git", "git status", "Check repo status")
        save_command("docker", "docker ps", "List containers")

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM remember")
        count = cursor.fetchone()[0]

        conn.close()

        self.assertEqual(count, 2)


if __name__ == "__main__":
    unittest.main()
