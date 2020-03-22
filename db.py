from quemsoueu import db
from quemsoueu.models import User, StartFlag

db.drop_all()
db.create_all()