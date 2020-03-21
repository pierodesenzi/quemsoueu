from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
db = SQLAlchemy(app)


from quemsoueu import routes
