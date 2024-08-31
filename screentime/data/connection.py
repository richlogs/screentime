import sqlite3

PATH = "/Users/richardkyle/Library/Application Support/Knowledge"
BASE = "knowledgeC.db"
SHM = "knowledgeC.db-shm"
WAL = "knowledgeC.db-wal"

class Connection:
    """
    A context manager class for handling SQLite database connections.
    """

    def __init__(self, file_name: str = BASE):
        self.file_name = file_name
        self.conn = sqlite3.connect(f"{PATH}/{file_name}")

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"An error occurred: {exc_val}")
        self.conn.close()



if __name__ == "__main__":
    with Connection() as conn:
        cursor = conn.cursor()  
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = [name[0] for name in cursor.fetchall()]
        print(table_names)


