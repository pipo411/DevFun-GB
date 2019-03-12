import os
import sqlite3


class DatabaseConnection:
    current_path = os.path.dirname(os.path.abspath(__file__))
    db_file_path = os.path.join(current_path, "database_connection.db")

    def __init__(self):
        self.exist = os.path.exists(self.db_file_path)

    def get_database(self):
        connection = sqlite3.connect(self.db_file_path)
        if not self.exist:
            print("A DB was successfully")
            try:
                cursor = connection.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS items (
                                              ID INTEGER primary key AUTOINCREMENT,
                                              NAME TEXT,
                                              PRICE REAL,
                                              QUANTITY INTEGER
                                        )""")
            except sqlite3.OperationalError:
                print("the db exists")
        return connection