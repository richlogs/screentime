import sqlite3
from screentime.data.connection import connect


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