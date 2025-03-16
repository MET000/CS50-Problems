from cs50 import SQL
from email_validator import validate_email, EmailNotValidError
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///coffeeshops.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        subscriber = request.form.get("subscriber").lower()

        # Validate the subscriber's email
        try:
            validate_email(subscriber)
        except EmailNotValidError as e:
            # Pass the error message to the template
            return render_template(
                "index.html",
                error_message_subscribers=f"Please provide a valid email address: {str(e)}",
            )

        # Check if the email is already subscribed
        if db.execute("SELECT 1 FROM subscribers WHERE email= ?", subscriber):
            return render_template(
                "index.html", error_message_subscribers="You are already subscribed"
            )

        # Add the new subscriber to the database
        try:
            db.execute("INSERT INTO subscribers (email) VALUES (?)", subscriber)
        except ValueError:
            return render_template(
                "index.html",
                error_message_subscribers="An error occurred, ensure that your email is valid",
            )

        # Redirect to the homepage after successful subscription
        return redirect("/")

    # Render the index page for GET requests
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        email = request.form.get("email").lower()
        password = request.form.get("password")
        confirmed_password = request.form.get("confirmation")
        address = request.form.get("address").title()
        phone_number = request.form.get("phone_number")

        # Ensure email was submitted
        if not email:
            return render_template(
                "register.html",
                error_message_register="Please provide a valid email address!",
            )

        # Check if the email is already registered
        if db.execute("SELECT 1 FROM users WHERE user_email= ?", email):
            return render_template(
                "register.html", error_message_register="You are already registered!"
            )

        # Validate the email format
        try:
            validate_email(email)
        except EmailNotValidError as e:
            return render_template(
                "register.html",
                error_message_register=f"Please provide a valid email address: {str(e)}",
            )

        # Ensure CoffeeShop name was submitted
        if not request.form.get("name"):
            return render_template(
                "register.html",
                error_message_register="Please provide a CoffeeShop name!",
            )

        # Ensure password was submitted
        elif not password:
            return render_template(
                "register.html", error_message_register="Please provide a password!"
            )

        # Ensure the passwords match and confirmation provided
        elif not confirmed_password or password != confirmed_password:
            return render_template(
                "register.html",
                error_message_register="Confirmation not provided or passwords do not match!",
            )

        # Ensure address was submitted
        elif not address:
            return render_template(
                "register.html", error_message_register="Please provide an address!"
            )

        # Ensure phone number was submitted and valid
        elif not phone_number:
            return render_template(
                "register.html",
                error_message_register="Please provide a valid phone number!",
            )
        try:
            phonenumbers.is_valid_number(phonenumbers.parse(phone_number, None))
        except NumberParseException as e:
            return render_template(
                "register.html",
                error_message_register=f"Please provide a valid phone number: {str(e)}",
            )

        if not phonenumbers.is_valid_number(phonenumbers.parse(phone_number, None)):
            return render_template(
                "register.html",
                error_message_register="Please provide a valid phone number!",
            )

        # Add the new user to the database
        try:
            db.execute(
                "INSERT INTO users (user_email, coffee_shop, hash, address, phone_number) VALUES (?, ?, ?, ?, ?)",
                email,
                request.form.get("name"),
                generate_password_hash(password),
                address,
                phone_number,
            )
        except ValueError:
            return render_template(
                "register.html", error_message_register="CoffeeShop already exists"
            )

        # Redirect user to login page after successful registration
        return redirect("/login")

    else:
        # Render the registration page for GET requests
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (by submitting a form via POST)
    if request.method == "POST":
        # Ensure email was submitted
        if not request.form.get("email"):
            return render_template(
                "login.html", error_message_login="Please provide an email"
            )

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template(
                "login.html", error_message_login="Please provide a password"
            )

        # Query database for email
        rows = db.execute(
            "SELECT * FROM users WHERE user_email = ?", request.form.get("email")
        )

        # Ensure email exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return render_template(
                "login.html",
                error_message_login="Invalid email address and/or password",
            )

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (by clicking a link or via redirect)
    else:
        # Render the login page
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to home page
    return redirect("/")


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Add a new menu item"""
    categories = [
        "Hot Drinks",
        "Cold Drinks",
        "Food & Snacks",
        "Espresso Bar",
        "Tea Selection",
        "Non-Coffee Beverages",
        "Breakfast & Bakery",
        "Lunch & Savory Items",
        "Desserts",
    ]
    if request.method == "POST":

        category = request.form.get("category")
        item = request.form.get("item")
        price = request.form.get("price")

        # Validate the form inputs
        if not category or category not in categories:
            return render_template(
                "add.html",
                error_message_add="Please provide a valid category",
                categories=categories,
            )
        elif not item:
            return render_template(
                "add.html",
                error_message_add="Please provide the name of your item",
                categories=categories,
            )
        elif not price:
            return render_template(
                "add.html",
                error_message_add="Please provide the price of your item",
                categories=categories,
            )

        # Add the new menu item to the database
        db.execute(
            "INSERT INTO menu (user_id, category, item, price) VALUES (?, ?, ?, ?)",
            session["user_id"],
            category,
            item,
            price,
        )

    # Render the add item page
    return render_template("add.html", categories=categories)


@app.route("/remove", methods=["GET", "POST"])
@login_required
def remove():
    """Remove a menu item"""
    data = db.execute("SELECT item FROM menu WHERE user_id = ?", session["user_id"])
    if request.method == "POST":
        item = request.form.get("item")

        # Ensure an item was selected
        if not item:
            return render_template(
                "remove.html", error_message_remove="Please select an item", data=data
            )

        # Remove the item from the database
        try:
            db.execute(
                "DELETE FROM menu WHERE item = ? AND user_id = ?",
                item,
                session["user_id"],
            )
        except ValueError:
            return render_template(
                "remove.html",
                error_message_remove="Please select a valid item",
                data=data,
            )

        # Redirect to home page after successful removal
        return redirect("/")

    # Render the remove item page
    return render_template("remove.html", data=data)


@app.route("/menu", methods=["GET", "POST"])
@login_required
def menu():
    """Display the menu with selected style"""
    if request.method == "POST":
        style = request.form.get("style")

        # Validate the selected style
        if not style or style not in ["Colorful", "Illustrational", "Minimalistic"]:
            return render_template(
                "menu.html", error_message_style="Please provide a valid style"
            )

        # Fetch menu items for the user
        data1 = db.execute(
            "SELECT category, item, price FROM menu WHERE user_id= ?",
            session["user_id"],
        )

        # Fetch user information
        data2 = db.execute(
            "SELECT coffee_shop, address, phone_number FROM users WHERE id= ?",
            session["user_id"],
        )

        categories = []

        for c in data1:
            if c["category"] not in categories:
                categories.append(c["category"])

        # Set style-specific attributes
        if style == "Colorful":
            color1 = "#D2042D"
            color2 = "#00D621"
            color3 = "#92ACAC"
            font1 = "libre-caslon-display-regular"
            font2 = "baskervville"
            font3 = "caudex-regular"
            img = "/static/img_1.jpg"
        elif style == "Illustrational":
            color1 = "#EBDDC3"
            color2 = "#D67BA8"
            color3 = "#005f69"
            font1 = "shrikhand-regular"
            font2 = "titan-one-regular"
            font3 = "sour-gummy"
            img = "/static/img_2.jpg"
        elif style == "Minimalistic":
            color1 = "#FFDE21"
            color2 = "#FFEA99"
            color3 = "#3b3b3b"
            font1 = "libre-caslon-display-regular"
            font2 = "monserrat"
            font3 = "bungee-hairline-regular"
            img = "/static/img_3.jpg"

        # Render the menu with the selected style
        return render_template(
            "display_menu.html",
            color1=color1,
            color2=color2,
            color3=color3,
            font1=font1,
            font2=font2,
            font3=font3,
            img=img,
            data1=data1,
            name=data2[0]["coffee_shop"],
            phone_number=data2[0]["phone_number"],
            address=data2[0]["address"],
            categories=categories,
        )

    # Render the style selection page
    return render_template("menu.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        email = request.form.get("email").lower()
        message = request.form.get("message")

        # Check if both email and message are provided
        if not email or not message:
            return render_template(
                "contact.html",
                error_message_contact="Message and/or email not provided!",
            )

        # Validate email format
        try:
            validate_email(email)
        except EmailNotValidError as e:
            # Pass the error message to the template
            return render_template(
                "contact.html",
                error_message_contact=f"Please provide a valid email address: {str(e)}",
            )

        # Insert the contact message into the database
        db.execute("INSERT INTO contact (email, message) VALUES (?, ?)", email, message)

        # Redirect to homepage
        return redirect("/")

    # Render the contact form for GET requests
    return render_template("contact.html")
