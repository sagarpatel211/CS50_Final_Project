# Modules
import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
# ----------------------------------- #
# Configure application
app = Flask(__name__)
# ----------------------------------- #
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
# ----------------------------------- #
# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
# ----------------------------------- #
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///words_storage.db")
# ----------------------------------- #
@app.route("/")
@login_required
def index():
    rows = db.execute("SELECT symbol,quantity FROM words WHERE u_id=:u_id", u_id=session['user_id'])
    return render_template("index.html", rows=rows)
# ----------------------------------- #
@app.route("/new", methods=["GET", "POST"])
@login_required
def new():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quantity = request.form.get("quantity")
        if not symbol:
            return apology("enter a some text")
        db.execute("INSERT INTO words (symbol, quantity, u_id) VALUES (:symbol, :quantity, :u_id);",
        symbol=symbol, quantity=quantity, u_id=session["user_id"])
        return redirect("/")
    else:
        return render_template("index.html")
# ----------------------------------- #
@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")
# ----------------------------------- #
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
# ----------------------------------- #
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password don't match", 403)
        password = request.form.get("password")
        hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        insert = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get("username"), hash=hash)
        if not insert:
            return apology("pick different username")
        user_id = db.execute("SELECT id FROM users WHERE username IS :username", username=request.form.get("username"))
        session['user_id'] = user_id[0]['id']
        return redirect("/")
    else:
        return render_template("register.html")
# ----------------------------------- #
def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)
# ----------------------------------- #
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)