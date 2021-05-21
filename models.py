from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

app.config.from_object(config.DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    login = db.Column(db.String(), primary_key=True, unique=True)
    api_key = db.Column(db.String(), unique=True)
    secret_key = db.Column(db.String(), unique=True)

    def __init__(self, login, api_key, secret_key):
        self.login = login
        self.api_key = api_key
        self.secret_key = secret_key

    def __repr__(self):
        return '<login {}>'.format(self.login)

    def serialize(self):
        return {
            'login': self.login,
            'api': self.api_key,
        }
