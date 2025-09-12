'''import sqlite3


conn = sqlite3.connect("student.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
grade TEXT
)
""")


cursor.executemany("INSERT INTO Students(name, age, grade) VALUES (?, ?, ?)", [
("Amit", 20, "A"),
("Priya", 21, "B"),
("Raj", 19, "A"),
("Neha", 22, "C")
])


conn.commit()
'''

#step 1 import csv
import csv
import sqlite3 as sq
conn= sq.connect("student.db")

cursor = conn.cursor()

cursor.execute("select * from Students")
rows = cursor.fetchall()
#open csv file
with open("stud.csv" , "w" , newline="") as file:
    #write in csv file 
    writer = csv.writer(file)
    writer.writerows(rows)
