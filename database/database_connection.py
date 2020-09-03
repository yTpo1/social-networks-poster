import os

from database.mysql_conn import MysqlConnection
from database.sqlite_conn import SqliteConnetion
from database.database import Database

#from mysql_conn import MysqlConnection
#from sqlite_conn import SqliteConnetion
#from database import Database


class DatabaseInit(Database):

    def __init__(self, database_engine, database_name):
        if database_engine == "mysql":
            self.database = MysqlConnection(os.environ["mysql_user"],
                                            os.environ["mysql_pass"],
                                            os.environ["mysql_host"],
                                            database_name)
        elif database_engine == "sqlite":
            self.database = SqliteConnetion(database_name)
            #self.database = SqliteConnetion(os.environ["my_sqlitedb"])

    def close_connection(self):
        self.database.close_connection()
