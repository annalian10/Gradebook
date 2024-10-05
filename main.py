""" Create and work with the student class"""
import sqlite3
import pandas as pd
import numpy as np
#db_path
tables = ['students', 'courses', 'assignments', 'enrollments']

#Create the student class
class student:
    #db_path =
    def __init__(self, st):
        self.st_name = st['last name'] + '_' + st['first_name']
        self.uid - st['uid']
        self.first_name = st['first_name']
        self.last_name = st['last_name']
        self.email = st['email'] 
        self.accomadations = st['accomadations']
        self.notes = st['notes']
        self.courses = []
        self.assignments = []
        self.submitted = []
        self.graded = []
        
def read_db_header(db_path, table):
    conn = sqlite3.connect(db_path)
    curr = conn.cursor()
    cur.execute(f'SELECT * FROM {table}')
    cols = [description[0] for description in cur.description]
    conn.close()
    return cols

def create_name_list(db_path):
    st_name_list = []
    table = 'students'
    query = f'SELECT last_name, first_name FROM {table}'
    
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    cols = [description[0] for description in cur.description]
    rows = cur.fetchall
    
    for row in rows:
        st = dict(zip(cols, row))
        st_name = st['last_name']+ '_' + st['first_name']
        st_name_list.append(st_name)
    conn.close()
    st_name_list.sort()
    return st_name_list