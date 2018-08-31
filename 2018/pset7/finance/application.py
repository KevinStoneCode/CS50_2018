import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    grand = 0
    rows = db.execute("SELECT symbol, sum(shares) as shares FROM history WHERE user_id = :user_id GROUP BY symbol HAVING sum(shares) > 0",
                          user_id=session["user_id"])
    for row in rows:
        res = lookup(row["symbol"])
        row["price"] = usd(res["price"])
        row["name"] = res["name"]
        total = float(res["price"]) * int(row["shares"])
        row["total"] = usd(total)
        grand += total

    user = db.execute("SELECT cash FROM users WHERE id = :user_id",
                          user_id=session["user_id"])
    cash = user[0]["cash"]
    grand += cash

    return render_template("index.html", stocks=rows, cash=usd(cash), grand=usd(grand))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("missing symbol", 400)

        if not request.form.get("shares"):
            return apology("missing shares", 400)

        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("invalid shares", 400)

        if shares < 0:
            return apology("invalid shares", 400)

        result = lookup(request.form.get("symbol"))
        if not result:
            return apology("invalid symbol")
        else:
            # Query database for user data
            rows = db.execute("SELECT * FROM users WHERE id = :id",
                          id=session["user_id"])
            total = float(result["price"]) * int(request.form.get("shares"))
            if total > rows[0]["cash"]:
                return apology("can't afford")
            else:
                db.execute("INSERT INTO history (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                          user_id=session["user_id"],
                          symbol=result["symbol"],
                          shares=request.form.get("shares"),
                          price=result["price"])
                # update cash
                db.execute("UPDATE users SET cash = cash - :price WHERE id = :user_id",
                          price=total,
                          user_id=session["user_id"])

                # Redirect user to home page
                return redirect("/")
    else:
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute("SELECT * FROM history WHERE user_id = :user_id ORDER BY id",
                          user_id=session["user_id"])
    for row in rows:
        row["price"] = usd(row["price"])
    return render_template("history.html",stocks=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("missing symbol", 400)

        result = lookup(request.form.get("symbol"))
        if not result:
            return apology("invalid symbol")
        else:
            return render_template("quoted.html", name=result["name"], price=usd(result["price"]), symbol=result["symbol"])
    else:
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("missing username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("missing password", 400)

        # Ensure passwords match
        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("passwords don't match", 400)

        # INSERT the new user into users
        rows = db.execute("INSERT INTO users (username, hash) VALUES (:username, :password)",
                          username=request.form.get("username"),
                          password=generate_password_hash(request.form.get("password")))
        if not rows:
            return apology("username taken", 400)
        else:
            session["user_id"] = rows
            return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("missing symbol", 400)

        if not request.form.get("shares"):
            return apology("missing shares", 400)

        # Ensure shares is enough
        rows = db.execute("SELECT sum(shares) as shares FROM history WHERE user_id = :user_id and symbol = :symbol",
                          symbol=request.form.get("symbol"),
                          user_id=session["user_id"])
        if int(request.form.get("shares")) > int(rows[0]["shares"]):
            return apology("too many shares", 400)

        result = lookup(request.form.get("symbol"))
        # total value
        total = float(result["price"]) * int(request.form.get("shares"))
        db.execute("INSERT INTO history (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                  user_id=session["user_id"],
                  symbol=result["symbol"],
                  shares=(int(request.form.get("shares")) * -1),
                  price=result["price"])
        # update cash
        db.execute("UPDATE users SET cash = cash + :price WHERE id = :user_id",
                  price=total,
                  user_id=session["user_id"])

        # Redirect user to home page
        return redirect("/")
    else:
        # get user's stock
        rows = db.execute("SELECT symbol, sum(shares) as shares FROM history WHERE user_id = :user_id GROUP BY symbol HAVING sum(shares) > 0",
                          user_id=session["user_id"])

        return render_template("sell.html", stocks=rows)


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
