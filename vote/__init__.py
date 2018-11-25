from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from vote.config import *
app = Flask(__name__)

app.config['SECRET_KEY'] = SQLConf.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLConf.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLConf.TRACK_MODIFICATIONS

db = SQLAlchemy(app)
import vote.application
