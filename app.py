"""Blogly application."""
# Flask, models.py Import and Configuration
from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# Flask-DebugToolBar Import and Configuration
from flask_debugtoolbar import DebugToolbarExtension

app.debug = True
app.config['SECRET_KEY'] = 'A11S3cr3tsAr3Saf3'

toolbar = DebugToolbarExtension(app)

# Routes

# Home Page
@app.route("/")
def get_users_list():
    """Redirect to a list of Users"""

    redirect('/users')

# Users Page
@app.route("/users")
def show_users():
    """Show a list of Users"""

    users = User.query.all()
    return render_template('users.html',
                           users = users)


# New User Form
app.route("/users/new", methods=["GET"])
def show_new_user_form():
    """Shows a form to create a new User"""

    return render_template('new_user_form.html')

app.route("/user/new", methods=["POST"])
def add_user():
    """Adds User and Redirects to User"""

    return redirect("/users")


# User Detail Page
app.route("/users/<int:user_id>", methods=["GET"])
def show_user(user_id):
    """Shows details about a User"""

    user = User.query.get_or_404(user_id)
    return render_template('user.html',
                           user = user)

# Edit User Form Page
app.route("/users/<int:user_id>/edit", methods=["GET"])
def show_edit_user_form(user_id):
    """Shows form to update User information"""
    user = User.query.get_or_404(user_id)
    return render_template('edit_user_form.html',
                           user = user)

app.route("/users/<int:user_id>/edit", methods=["POST"])
def update_user(user_id):
    """Update User information"""

    return redirect("/users")

# Delete User Page
app.route("users/<int:user-id>/delete", methods=["POST"])
def delete_user(user_id):
    """Delete a User from the database"""

    return redirect("/users")
