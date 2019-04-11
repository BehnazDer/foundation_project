from flask import Flask, render_template, redirect, request, url_for, Blueprint
from database import get_db
import sqlite3
app = Flask(__name__) #creating the application object
DATABASE='mydatabase.db'

@app.route('/') # @ is a decorator and links the function to the url
def home():
    return "Welcome to the PawClubs!"
bp = Blueprint('auth', __name__, url_prefix='/auth')
 #Flask associates view functions wih bluprints when dispatching requests & generating URLs from one endpoint to another
@app.route('/login', methods=('GET', 'POST')) # by default flask assumes that all methods are GET
def login():  
    if request.method == 'POST':
        user_username = request.form['username']
        user_password = request.form['password']
        print(user_username, user_password)
        if not user_username or not user_password:
            return render_template('auth/login.html')
        #to get data from database
        cursor = get_db()
        cursor.execute("SELECT username, password  FROM users WHERE username= '{}' and password='{}'" .format(user_username,user_password))
        user_info = cursor.fetchall()
        print(user_info)
        return redirect("/")
    else:
        return render_template('auth/login.html')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    # if request.method == 'POST':
    #     user_username = request.form['username']
    #     user_password = request.form['password']
    # else:
    #     return redirect(url_for('home'))
    return render_template('auth/register.html')



if __name__ =="__main__" :
    app.run(debug=True) #start the server with the run() method