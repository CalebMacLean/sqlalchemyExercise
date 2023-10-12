# Seed File to make sample data for users
# Imports
from models import User, db
from app import app

# Create Tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add Users
cabletooth = User(first_name='Cable', last_name='Tooth')
caleb_maclean = User(first_name='Caleb', last_name='MacLean')
sarah_fakename = User(first_name='Sarah', last_name='Fakename')

# Add new user objects to session
db.session.add(cabletooth)
db.session.add(caleb_maclean)
db.session.add(sarah_fakename)

# Commit
db.session.commit()
