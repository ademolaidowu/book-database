import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, isbn integer, year integer)")
    conn.commit()
    conn.close

def insert(title, author, isbn, year):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author, isbn, year))
    conn.commit()
    conn.close()

def viewall():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book ")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", isbn="", year=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR isbn=? OR year=?",(title, author, isbn, year))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, isbn, year):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, isbn=?, year=? WHERE id=?", (title, author, isbn, year, id))
    conn.commit()
    conn.close()



connect()

