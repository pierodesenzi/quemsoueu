from flask import render_template, url_for, flash, redirect, request, make_response
from quemsoueu import app, db
from quemsoueu.forms import RegistrationForm
from quemsoueu.models import User, StartFlag
import random

@app.route("/", methods=['GET', 'POST'])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        #flash('Your account has been created! You are now able to log in', 'success')
        res = make_response(redirect(url_for('wait')))
        res.set_cookie('myname', form.username.data, max_age=60*60*24)
        return res
    return render_template('home.html', form=form)


@app.route("/wait")
def wait():
    return render_template('wait.html', name=request.cookies.get('myname'))


@app.route("/set_characters")
def set_characters():
    ready = True#StartFlag.query.first()[1]
    if ready:
        players = []
        users = User.query.all()
        for u in users:
            players.append(u.username)
        print(players)
        random.shuffle(players)
        for p in range(0,len(players)):
            result = db.engine.execute("UPDATE user SET target='{}' WHERE username='{}'".format(players[p-1], players[p]))
        mytarget = list(db.engine.execute("SELECT target FROM user WHERE username='{}'".format(request.cookies.get('myname'))))[0][0]#[2]
    return render_template('set_characters.html', name=request.cookies.get('myname'),
        target = mytarget)

@app.route("/game")
def game():
    User.query.all
    return render_template('wait.html', name=request.cookies.get('myname'))
