from flask import render_template, url_for, flash, redirect
from quemsoueu import app


@app.route("/")
def home():
    return render_template('home.html')
