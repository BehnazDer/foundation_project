import sqlite3 as sql

def insertUser(username,password):
    con = sql.connect("mydatabase.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def get_db():
    con = sql.connect("mydatabase.db")
    cur = con.cursor()
    return cur