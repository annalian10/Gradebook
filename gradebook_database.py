import sqlite3
from sqlite3 import Error

## Create the database
#need to create a db file of the gradebooks
def creat_connection(db_file):
    """ Create a database connection to a SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version, 'database created')
    except Error as e:
        print(e)
    finally:
        conn.close()
        print('connection closed')
    

## Create the tables

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS students;')