import sqlite3

PATH = "/Users/richardkyle/Library/Application Support/Knowledge"
BASE = "knowledgeC.db"
SHM = "knowledgeC.db-shm"
WAL = "knowledgeC.db-wal"


def connect(file_name: str) -> sqlite3.Connection:
    """
    Connects to the database and returns a connection object
    """
    conn = sqlite3.connect(f"{PATH}/{file_name}")
    return conn


def get_table_names(conn: sqlite3.Connection) -> list:
    """"
    Returns a list of table names in the database
    """
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_names = [name[0] for name in cursor.fetchall()]
    return table_names



if __name__ == "__main__":
    with connect(BASE) as conn:
        print(get_table_names(conn))