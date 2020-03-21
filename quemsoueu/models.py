from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)

def write_to_db(object):
    db.session.add(object)
    db.session.commit()
