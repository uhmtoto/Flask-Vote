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
        return f"{self.id}|{self.name}|{self.part}|{self.phrase}|{self.image}"

db.create_all()