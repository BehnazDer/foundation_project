import sqlite3 as sql

def insertUser(user_name, user_email, user_username,user_password, user_repeatpassword):
    con = sql.connect("mydatabase.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (name,email,username,password,repeatpassword) VALUES (?,?)", (user_name, user_email, user_username,user_password, user_repeatpassword))
    con.commit()
    con.close()

def get_db():
    con = sql.connect("mydatabase.db")
    cur = con.cursor()
    return cur, con

def insert_into_db(command):
    con = sql.connect("mydatabase.db")
    cur = con.cursor()
    cur.execute(command)
    con.commit()
    con.close()