from flask import Flask, render_template, redirect, request, url_for
from database import get_db
import sqlite3
app = Flask(__name__) #creating the application object
app.secret_key = 41003
DATABASE='mydatabase.db'


@app.route('/')
def landing():
    return render_template('auth/landing.html')
@app.route('/home') # @ is a decorator and links the function to the url
def home():
    return render_template('auth/home.html')

@app.route('/login', methods=('GET', 'POST')) # by default flask assumes that all methods are GET
def login():  
    if  request.method == 'POST':
        user_username = request.form['username']
        user_password = request.form['password']
        print(user_username, user_password)
        if not user_username or not user_password:
            return render_template('auth/login.html')
        #to get data from database
        cursor, connection = get_db()
        cursor.execute("SELECT username, password  FROM users WHERE username= '{}' and password='{}'".format(user_username,user_password))
        user_info = cursor.fetchall()
        if user_info:
            return redirect('/home')
        else:
            return render_template('auth/login.html', error= "This information is required")
           
    else:
        return render_template('auth/login.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']
        user_username = request.form['username']
        user_password = request.form['password']
        user_repeatpassword = request.form['repeatpassword']
        cursor, connection = get_db()
        error = None
        if not user_name or not user_email or not user_username or not user_password or not user_repeatpassword:
            return render_template('auth/register.html', error= "This information is required")
        elif user_password != user_repeatpassword:
            return render_template('auth/register.html', error= "Invalid Password")
            
        elif cursor.execute('SELECT id FROM users WHERE email = ? ', (user_email,)).fetchone() is not None:
            error = 'User {} is already registered.'.format(user_email)
        if error is None:   
            cursor.execute("INSERT INTO users (name, email, username, password, repeatpassword) values(?, ?, ?, ?, ?)",(user_name, user_email, 
                            user_username, user_password, user_repeatpassword))

            # insert_into_db("INSERT ...")
            # insertUser(user_username, user_password)
            connection.commit()
            return redirect('/home')
    else:
        return render_template('auth/register.html')



if __name__ =="__main__" :
    app.run(debug=True) #start the server with the run() method