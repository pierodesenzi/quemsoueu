from quemsoueu import db
from quemsoueu.models import User

print('dropping...')
db.drop_all()
db.engine.execute('DROP TABLE flag')
print('recreating...')
db.create_all()
db.engine.execute("""CREATE TABLE flag (
	status BOOLEAN NOT NULL
)""")
print('adding flag...')
db.engine.execute("INSERT INTO flag VALUES (False)")
#db.session.add(StartFlag(ready=False))
print('committing...')
db.session.commit()
print('Done.')
