# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from flask import redirect
from flask import session
import os

# -- Initialization section --
app = Flask(__name__)

# events = [
#         {"event":"First Day of Classes", "date":"2019-08-21"},
#         {"event":"Winter Break", "date":"2019-12-20"},
#         {"event":"Finals Begin", "date":"2019-12-01"}
#     ]

# name of database
# app.config['MONGO_DBNAME'] = 'database-name'
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:Dw84pzbMkdHNBoJs@cluster0.lndrp.mongodb.net/database?retryWrites=true&w=majority'

mongo = PyMongo(app)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
# URI of database
#app.config['MONGO_URI'] = 'mongo-uri'

#mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html',time = datetime.now())


# CONNECT TO DB, ADD DATA

@app.route('/yourShelter',methods = ['GET', 'POST'])

def yourShelter():
    shelter_info = getShelter()
    print(shelter_info)
    
    # connect to the database
    events = mongo.db.events

    # insert new data
   # events.insert({"event": "First Day of Classes",
                  # "date": "2021-09-13"})

    #events.insert({"event": "birthday",
                   # "date": "2003-04-24"})

    # return a message to the user
    return ""

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("account.html")
    else:
        # this creates a user's database in mongo db if it doesn't already exist

        users = mongo.db.users

        # this stores form data into a user's dictionary
        user = {
            "username": request.form["username"],
            "password": request.form["password"]
        }
        users.insert(user)  # add our user data into mongo
       # tell the browser session who the user is
        session["username"] = request.form["username"]
        return "Congratulations, you made an account: @ " + request.form["username"]
       


