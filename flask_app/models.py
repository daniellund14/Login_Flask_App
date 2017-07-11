#!/usr/bin/env python3

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_app import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, email, password):
        self.email = email
        self.password = self.set_password(password)

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User:{email}'.format(email=self.email)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.email)


if __name__ == '__main__':
    user = User('daniel.lund14@gmail.com', 'password')
    print (user.password)
    print (user.check_password('password'))