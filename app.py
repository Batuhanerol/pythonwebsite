from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import date



app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.errorhandler(404)
def erorr(e):
    return render_template('404.html')



if __name__ == "__main__":
    

    app.debug = True
    app.run()
