from quemsoueu import db
from quemsoueu.models import User

print('dropping...')
db.drop_all()
try:
    db.engine.execute('DROP TABLE flag')
except:
    pass
print('recreating...')
db.create_all()
db.engine.execute("""CREATE TABLE flag (
	status BOOLEAN NOT NULL
)""")
print('adding flag...')
db.engine.execute("INSERT INTO flag VALUES (False)")
print('committing...')
db.session.commit()
print('Done.')
