# Hello world python program
import sqlite3

class recoder:
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname)
        cursor = self.con.cursor()
        cursor.execute("select * from sqlite_master where tables")