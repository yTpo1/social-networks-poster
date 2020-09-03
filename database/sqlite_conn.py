import sqlite3
from database.database import Database


class SqliteConnetion(Database):
    def __init__(self, db_location):
        self.conn = sqlite3.connect(db_location)
        self.cursor = self.conn.cursor()  # cursor

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
