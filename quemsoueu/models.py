from datetime import datetime
from quemsoueu import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    target = db.Column(db.String(20))
    character = db.Column(db.String(30))

#class StartFlag(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    ready = db.Column(db.String(5))
