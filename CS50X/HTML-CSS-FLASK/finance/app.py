import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks = db.execute(
        "SELECT symbol, shares, action FROM transactions WHERE user_id= ?", session["user_id"]
    )

    cash = db.execute(
        "SELECT cash FROM users WHERE id = ?", session["user_id"]
    )[0]['cash']

    # Create an empty dictionary to contain data about actual shares owned
    data = {}

    for stock in stocks:
        if stock["symbol"] in data:
            if stock["action"] == "bought":
                data[stock["symbol"]] += stock["shares"]

            elif stock["action"] == "sold":
                data[stock["symbol"]] -= stock["shares"]

        # Create a key having the name of the stock and iniatialize its value to stock["shares"]
        # The first time a stock appears in a person’s history (data stores in transactions table), it must be a purchase, as they cannot sell a stock they haven’t bought
        else:
            data[stock["symbol"]] = stock["shares"]

    # Initialize an empty list to store stock prices
    prices = []

    for stock in data:
        prices.append({stock: lookup(stock)["price"], "shares": data[stock]})

    # Initialize a variable to count the total value of a person’s stocks + their cash
    total = cash

    for price in prices:
        for i in price:
            if i != "shares":
                total += price[i] * price["shares"]

    return render_template("index.html", data=data, prices=prices, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        data = lookup(request.form.get("symbol"))
        if not data:
            return apology("stock symbol does not exist or was not provided")

        stock_price = data["price"]
        user_cash = int(db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"]
        )[0]["cash"])

        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("number of shares must be a positive integer", 400)

        if shares < 1:
            return apology("number of shares must be a positive integer", 400)

        if user_cash - (stock_price * shares) < 0:
            return apology("you don't have enough cash")

        # Store the data about the purchase
        db.execute("INSERT INTO transactions (user_id, symbol, price, shares, action) VALUES (?, ?, ?, ?, ?)", session["user_id"], request.form.get(
            "symbol").upper(), stock_price * int(request.form.get("shares")), request.form.get("shares"), "bought")

        # Update the cash
        db.execute("UPDATE users SET cash = (SELECT cash FROM users WHERE id = ?) - ? WHERE id = ?",
                   session["user_id"], stock_price * int(request.form.get("shares")), session["user_id"])
        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    data = db.execute(
        "SELECT symbol, price, shares, date, action FROM transactions WHERE user_id = ?", session[
            "user_id"]
    )

    return render_template("history.html", data=data)


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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
        symbol = request.form.get("symbol")
        data = lookup(symbol)
        if not data:
            return apology("an error occured")

        return render_template("quoted.html", name=data['name'], price=data['price'], symbol=data['symbol'])

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure the passwords match and confirmation provided
        elif not request.form.get("confirmation") or (request.form.get("password") != request.form.get("confirmation")):
            return apology("confirmation not provided or passwords do not match", 400)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get(
                "username"), generate_password_hash(request.form.get("password")))
        except ValueError:
            return apology("username already exists", 400)

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("please provide a symbol")
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("number of shares must be a positive integer")

        if shares < 1:
            return apology("number of shares must be a positive integer")

        owned_shares = db.execute(
            "SELECT symbol, SUM(shares) AS shares FROM transactions WHERE user_id = ? GROUP BY symbol", session[
                "user_id"]
        )

        symbol = request.form.get("symbol")

        marker = 0

        for owned in owned_shares:
            if symbol == owned["symbol"] and owned["shares"] >= shares:
                marker += 1

        if marker == 0:
            return apology("not enough shares to sell of that stock")

        stock_price = lookup(symbol)["price"]

        # Store data about the sale
        db.execute("INSERT INTO transactions (user_id, symbol, price, shares, action) VALUES (?, ?, ?, ?, ?)", session["user_id"], request.form.get(
            "symbol").upper(), stock_price * int(request.form.get("shares")), request.form.get("shares"), "sold")

        # Update the cash
        db.execute("UPDATE users SET cash = (SELECT cash FROM users WHERE id = ?) + ? WHERE id = ?",
                   session["user_id"], stock_price * shares, session["user_id"])

        return redirect("/")

    symbols = db.execute(
        "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol", session["user_id"]
    )
    return render_template("sell.html", symbols=symbols)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():

    if request.method == "POST":

        try:
            cash = int(request.form.get("cash"))
        except ValueError:
            return apology("please enter a valid amount")

        if cash < 500:
            return apology("please enter a valid amount ($500 or more)")

        # Update the cash
        db.execute("UPDATE users SET cash = (SELECT cash FROM users WHERE id = ?) + ? WHERE id = ?",
                   session["user_id"], cash, session["user_id"])

        return redirect("/")

    return render_template("add_cash.html")
