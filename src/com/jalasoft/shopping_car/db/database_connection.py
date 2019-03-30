"""
This class makes the connection to the database.
"""
import os
import sqlite3


class DatabaseConnection:
    current_path = os.path.dirname(os.path.abspath(__file__))
    db_file_path = os.path.join(current_path, "database_connection.db")

    def __init__(self):
        self.exist = os.path.exists(self.db_file_path)

    def get_database(self):
        """
        This method obtained the connection to the database and tables are created.
        Returns db connection.

        :return:
        """
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
                cursor.execute("""CREATE TABLE IF NOT EXISTS venta (
                                                              ID INTEGER primary key AUTOINCREMENT,
                                                              DESCRIPTION TEXT
                                                        )""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS records (
                                                                              ID INTEGER primary key AUTOINCREMENT,
                                                                              NAME TEXT,
                                                                              PRICE REAL,
                                                                              QUANTITY INTEGER,
                                                                              PURCHASE_DATE DATE 
                                                                        )""")
            except sqlite3.OperationalError:
                print("the db exists")
        return connection
