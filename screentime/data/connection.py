import sqlite3

PATH = "/Users/richardkyle/Library/Application Support/Knowledge"
BASE = "knowledgeC.db"
SHM = "knowledgeC.db-shm"
WAL = "knowledgeC.db-wal"


def connect(file_name: str = BASE) -> sqlite3.Connection:
    """
    Connects to the database and returns a connection object
    """
    conn = sqlite3.connect(f"{PATH}/{file_name}")
    return conn

