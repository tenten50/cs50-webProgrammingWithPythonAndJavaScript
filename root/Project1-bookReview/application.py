import os
import requests

from flask import Flask, session, render_template, url_for, request, flash, redirect, abort
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
Session(app)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

#Goodreads API
res=requests.get("https://www.goodreads.com/book/review_counts.json", params={"key":"w8sUE1HnjwhfcuBPENrEyg", "isbns":"9781632168146"})
print(res.json())

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/search/', methods=['GET', 'POST'])
def search():
    books=[]
    if request.method == "POST":
        searchType = request.form.get('searchType')
        searchContent = request.form.get('searchContent')
        books=db.execute("SELECT * FROM books WHERE {searchType} LIKE '%{searchContent}%'".format(searchType=searchType, searchContent=searchContent)).fetchall()

    return render_template("search.html", books=books)

@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        log_username = request.form.get('username')
        log_password = request.form.get('password') 
        query = db.execute("SELECT * FROM users WHERE username=:username", {"username": log_username}).fetchone()
        if query is None:
            flash("Please register first")
            return redirect(url_for('register'))
        elif query is not None and query["password"] == log_password:
            flash("Login successfully!")
            session['username'] = log_username
            return redirect(url_for('index'))
        elif query is not None and query["password"] != log_password:
            flash("wrong password.")
            return redirect(url_for('login'))
    return render_template('login.html')



@app.route("/register/", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        reg_username = request.form.get('username')
        reg_password = request.form.get('password')

        query = db.execute("SELECT * FROM users WHERE username=:username", {"username": reg_username}).fetchone()
        if query is None:
            db.execute("INSERT INTO users (username, password) VALUES (:username, :password)", {"username": reg_username, "password":reg_password})
            db.commit()
            flash('successfully registered, please login')
            return redirect(url_for('login'))
        else:
            flash('username already exists')
            return render_template("register.html")
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug = True)
