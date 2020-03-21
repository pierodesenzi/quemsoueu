from flask import render_template, url_for, flash, redirect
from quemsoueu import app
from quemsoueu.forms import RegistrationForm


@app.route("/")
def home():
    form = RegistrationForm()

    return render_template('home.html', form=form)
