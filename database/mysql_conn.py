import mysql.connector
from database.database import Database


class MysqlConnection(Database):
    def __init__(self, user, passw, host, database):
        config = {
            'user': user,
            'password': passw,
            'host': host,
            'database': database,
            'raise_on_warnings': True
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

