
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from flask import redirect
from flask import session
from datetime import datetime
from model import getShelter
from model import womenShelter
from model import menShelter
from model import youthShelter
from model import lgbtqShelter
from model import formResult

# import requests
import os
from model import womenShelter


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
    # users = mongo.db.users

    shelter_info = getShelter()
    print(shelter_info)



@app.route('/women', methods=['GET', 'POST'])
def women():
    users = mongo.db.users
    womenShelter_info = womenShelter(users)
    print(womenShelter_info)
    return render_template('women18+.html', time=datetime.now(), womenShelter_info = womenShelter_info)


@app.route('/men', methods=['GET', 'POST'])
def men():
    users = mongo.db.users
    menShelter_info = menShelter(users)
    print(menShelter_info)
    return render_template('men18+.html', time=datetime.now(), menShelter_info = menShelter_info)

@app.route('/youth', methods=['GET', 'POST'])
def youth():
    users = mongo.db.users
    youthShelter_info = youthShelter(users)
    print(youthShelter_info)
    return render_template('youth.html', time=datetime.now(), youthShelter_info = youthShelter_info)

@app.route('/lgbtq', methods=['GET', 'POST'])
def lgbtq():
    users = mongo.db.users
    lgbtqShelter_info = lgbtqShelter(users)
    print(lgbtqShelter_info)
    return render_template('lgbtq.html', time=datetime.now(), lgbtqShelter_info = lgbtqShelter_info)

# def womenShelter():
#     shelter_request_link = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Service_WebMercator/MapServer/25/query?where=1%3D1&outFields=*&outSR=4326&f=json"
#     women = requests.get(shelter_request_link).json()
#     if users.find({"gender": "Women"}) :
#         return women['features'][0]['attributes']['ADDRESS']
#         return women['features'][7]['attributes']['ADDRESS']
#         return women['features'][9]['attributes']['ADDRESS']
#         return women['features'][12]['attributes']['ADDDRESS']
#         return women['features'][14]['attributes']['ADDRESS']

    # connect to the database
    # events = mongo.db.events

    # insert new data
   # events.insert({"event": "First Day of Classes",
    # "date": "2021-09-13"})

    # events.insert({"event": "birthday",
    # "date": "2003-04-24"})

    # return a message to the user
    return render_template("shelter.html", time=datetime.now()) #shelter_info = shelter_info)


@app.route('/resource', methods=['GET', 'POST'])
def resource():
    users = mongo.db.users
   # form_info = formResult(users)
   # print(form_info)
    if users.find({"reside": "NO"}):
        return render_template("resource.html", time=datetime.now())
    else:
        return redirect('/yourShelter')
        # return render_template("resource.html", time=datetime.now())
# login page
# @app.route('/form', methods = ['GET', 'POST'])
# def form():
#     if request.method == "GET":
#         return render_template("form.html")
#     else:
#         form = mongo.db.forms


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

        # this stores form data into a user's dictionary
    else:
        users = mongo.db.users
        user = {
            "username": request.form["username"],
            "password": request.form["password"],
            "reside": request.form["reside"],
            "age": request.form["age"],
            "gender": request.form["gender"],
            # "type_assistance": request.form["type_assistance"]
        }

        # checks if user already exists in the database
        existing_user = users.find_one({'username': user['username']})

        # make condition to check if user already exists in mongo
        if existing_user is None:
            users.insert(user)  # add our user data into mongo

       # tell the browser session who the user is
            session["username"] = request.form["username"]

            return "Congratulations, you made an account: @" + request.form["username"]
            # return render_template('/')
        else:
            return "Unfortunately, this username is taken. Please try again." + render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    users = mongo.db.users
    if request.method == "GET":
        return render_template("login.html")
    else:
        # this creates a user's database in mongo db if it doesn't already exist

       

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
                error = "Incorrect password. Please try again. If you haven't registered, please make an account."
                return render_template('login.html', error=error)

        else:
            return redirect('/signup')


@app.route('/logout')
def logout():
    # removes session
    session.clear()
    return redirect('/')
