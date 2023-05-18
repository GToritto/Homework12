# Giuseppe Toritto
# 05/17/2023

import sqlite3

# Connecting to database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# a
cursor.execute("SELECT last FROM authors ORDER BY last DESC")

last_names = cursor.fetchall()

print(last_names)

# b
cursor.execute("SELECT title FROM titles ORDER BY title ASC")

book_titles = cursor.fetchall()

print(book_titles)

# c
author_name = "John Doe" 
cursor.execute("""
    SELECT titles.title, titles.copyright, author_ISBN.isbn
    FROM titles
    INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn
    INNER JOIN authors ON author_ISBN.id = authors.id
    WHERE authors.last = ?
    ORDER BY titles.title ASC
""", (author_name,))
books_by_author = cursor.fetchall()

print(books_by_author)


new_author = ("Jane", "Smith")  
cursor.execute("INSERT INTO authors (first, last) VALUES (?, ?)", new_author)

conn.commit()


new_title = ("420", "SpiderWoman", 1, "2023")  
cursor.execute("INSERT INTO titles (isbn, title, edition, copyright) VALUES (?, ?, ?, ?)", new_title)

new_title_id = cursor.lastrowid

author_id = 1  
cursor.execute("INSERT INTO author_ISBN (id, isbn) VALUES (?, ?)", (author_id, new_title[0]))
conn.commit()

cursor.close()
conn.close()
