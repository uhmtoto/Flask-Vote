from flask_sqlalchemy import SQLAlchemy
from vote import db

class Candidate(db.Model):
    __table_name__ = 'Candidate'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    part = db.Column(db.String(50), nullable=False)
    phrase = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100), nullable=False)

    def __repr__ (self):
        return f"[{self.id},'{self.name}','{self.part}','{self.phrase}','{self.image}']"

class Voter(db.Model):
    __table_name__ = 'Voter'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(7), nullable=False)

    def __repr__ (self):
        return f"{self.id}|{self.key}"

class Log(db.Model):
    __table_name__ = 'Log'
    id = db.Column(db.Integer, primary_key=True)
    user_key = db.Column(db.String(7), nullable=False)
    part = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Integer, nullable=False)

    def __repr__ (self):
        return f"{self.id}|{self.user_key}|{self.part}|{self.value}"

db.create_all()