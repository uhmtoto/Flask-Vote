from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

with open('./vote/secretkey', 'r') as file:
    app.config['SECRET_KEY'] = file.read()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
import vote.application
