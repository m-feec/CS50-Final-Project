import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure SQL from cs50 library
db = SQL("sqlite:///forum.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    """Show main page"""
    if request.method == "GET":
        return render_template("index.html")

@app.route("/big6")
def big6():
    """Show coins"""
    if request.method == "GET":
        return render_template("big6.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log user in """

    # Forget user_id in session
    session.clear()

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Must provide username", 403)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("Must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Check if user exist and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to Forum page
        return redirect("/forum")

    # User get via GET method
    else:
        return render_template("/login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Register user """
    if request.method == "POST":

        name = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check if username and password is not blank
        if not name:
            return apology("must provide username", 400)

        elif not password:
            return apology("must provide password", 400)

        # Check if name exist
        rows = db.execute("SELECT * FROM users WHERE username = ?", name)

        if len(rows) != 0:
            return apology("This name is taken, pease choose another one.", 400)

        # Check if user confirm password
        if password != confirmation:
            return apology("Passwords do not match", 400)

        # create and update user database
        hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, hash)

        # Update session with new loged user
        key = db.execute("SELECT id FROM users WHERE username = ?", name)
        session["user_id"] = key[0]["id"]

        return redirect("/forum")

    else:
        return render_template("register.html")



@app.route("/logout")
def logout():

    session.clear()
    return redirect("/")



@app.route("/forum", methods=["GET", "POST"])
@login_required
def forum():
    """Chat zone"""
    if request.method == "POST":

        key = session["user_id"]
        chat = request.form.get("chat")
        now = datetime.datetime.now()

        # Check if user don't type anything
        if not request.form.get("chat"):
            return redirect("/forum")

        # Query for user name
        rows = db.execute("SELECT username FROM users WHERE id = ?", key)
        name = rows[0]["username"]

        # Insert chat to database
        db.execute("INSERT INTO conversation (user_id, chat, date) VALUES (?, ?, ?)", key, chat, now.strftime("%Y-%m-%d %H:%M:%S"))

        return redirect("/forum")

    else:

        # Get items from database for my page
        TEXT = []

        mess = db.execute("SELECT * FROM conversation ORDER BY datetime(date) DESC")

        # take one comment from SQL and add to dictionary to crate easy accesable order
        for name in mess:

            con = name["chat"]
            person = name["user_id"]
            person = db.execute("SELECT username FROM users WHERE id = ?", person)
            person = person[0]["username"]
            date = name["date"]

            MESSAGE = {
                "message": con,
                "name": person,
                "date": date
            }

            TEXT.append(MESSAGE)

        return render_template("forum.html", text=TEXT)


@app.route("/about")
def about():

    return render_template("about.html")