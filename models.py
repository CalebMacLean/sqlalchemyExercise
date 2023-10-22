"""SQLAlchemy models for blogly."""

import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

# User Model
class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"
    
    posts = db.relationship("Post", backref='user', cascade="all, delete-orphan")

# Post Model 
class Post(db.Model):
    """User post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(75), nullable=False)
    created_at = db.Column(db.DateTime, 
                           nullable = False,
                           default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Tag Model
class Tag(db.Model):
    """Tags for Posts"""
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text, nullable=False)

    posts = db.relationship('Post',
                            secondary='posts_tags',
                            cascade="all,delete",
                            backref='tags')

# M2M Through Model connecting posts and tags
class PostTag(db.Model):
    """M2M table for posts & tags tables"""
    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)