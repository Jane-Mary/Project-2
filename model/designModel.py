from sqlalchemy.sql import func
from config import db


class Designs(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name =  db.Column(db.String(50), nullable=False)
     price = db.Column(db.Integer, nullable=False)
     location =  db.Column(db.String(200), nullable=False)
     image = db.Column(db.String(200),nullable=False)
     description =  db.Column(db.String(200), nullable=False)
     