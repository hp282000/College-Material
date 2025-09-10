
#step 1 import library
import sqlite3
'''
#step 2 connection and create db
con = sqlite3.connect('test.db')

#step 3 connection with cursor
cursor = con.cursor()

#----------------------Create Table------------------------------

student = """Create table Student
(id INTEGER PRIMARY KEY ,
StudentName TEXT NOT NULL,
Class Text)"""

cursor.execute(student)
con.commit()
con.close()

'''
#----------------------Insert Data------------------------------

con = sqlite3.connect('test.db')
cursor = con.cursor()

#insertdata = """insert into Student values(2,'Harsh','20')"""
#cursor.execute(insertdata)

#con.commit()

#----------------------select Data------------------------------
selectquery = """select * from Student"""
a = cursor.execute(selectquery)
b = a.fetchall()
print(b)
con.close()
