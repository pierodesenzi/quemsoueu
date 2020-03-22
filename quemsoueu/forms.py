from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
#from quemsoueu import models


class RegistrationForm(FlaskForm):
    username = StringField('nome')
    submit = SubmitField('Confirmar')
#    user = models.User(username = username)

class CharacterForm(FlaskForm):
    character = StringField('personagem')
    submit = SubmitField('Confirmar')
