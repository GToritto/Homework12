# Giuseppe Toritto
# 05/17/2023


import sqlite3

# opens books database

conn = sqlite3.connect('books.db')

# creates cursor

cursor = conn.cursor()

cursor.execute("SELECT * FROM titles")

# metadata from description

description = cursor.description

data = cursor.fetchall()

# Results

for row in data:
    
    print("%-20s%-20s%-20s" % (row[0], row[1], row[2]))
