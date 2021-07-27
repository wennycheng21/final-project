
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from flask import redirect
from flask import session
from datetime import datetime
from model import getShelter
import os
from model import getShelter
from datetime import datetime


# -- Initialization section --
app = Flask(__name__)

# name of database
app.secret_key = os.getenv("SECRET_KEY")
uri_password = os.getenv("PASSWORD")
# app.config['MONGO_DBNAME'] = 'database-name'
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:' + uri_password + \
    '@cluster0.lndrp.mongodb.net/database?retryWrites=true&w=majority'

mongo = PyMongo(app)


# URI of database
# app.config['MONGO_URI'] = 'mongo-uri'

# mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=datetime.now())


# CONNECT TO DB, ADD DATA

@app.route('/yourShelter', methods=['GET', 'POST'])
def yourShelter():
    shelter_info = getShelter()
    print(shelter_info)

    # connect to the database
    # events = mongo.db.events

    # insert new data
   # events.insert({"event": "First Day of Classes",
    # "date": "2021-09-13"})

    # events.insert({"event": "birthday",
    # "date": "2003-04-24"})

    # return a message to the user
    return render_template("shelter.html", time=datetime.now(), shelter_info=shelter_info)

# login page


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        # this creates a user's database in mongo db if it doesn't already exist

        users = mongo.db.users

        # this stores form data into a user's dictionary
        user = {
            "username": request.form["username"],
            "password": request.form["password"]
        }

        # checks if user already exists in the database
        existing_user = users.find_one({'username': user['username']})

        # make condition to check if user already exists in mongo
        if existing_user is None:
            users.insert(user)  # add our user data into mongo

       # tell the browser session who the user is
            session["username"] = request.form["username"]

            # return "Congratulations, you made an account: @ " + request.form["username"]
            return render_template("index.html")
        else:
            return "Unfortunately, the username is taken."

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == "GET":
       return render_template("login.html")
   else:
       # this creates a user's database in mongo db if it doesn't already exist
 
        users = mongo.db.users
 
         # this stores form data into a user's dictionary
        user = {
            "username": request.form["username"],
            "password": request.form["password"]
       }
 
        # checks if user already exists in the database
        existing_user = users.find_one({'username': user['username']})
        # make condition to check if user already exists in mongo
        if existing_user:
            # if it does exists, we are checking if the password matches
            if user['password'] == existing_user['password']:
                session['username'] = user['username']
                return redirect('/')
            else:
                error = "Incorrect password. Plesse try again."
                return render_template('login.html', error=error)
        else: 
            return redirect('/signup.')

 
 


@app.route('/logout')
def logout():
    # removes session
    session.clear()
    return redirect('/')
