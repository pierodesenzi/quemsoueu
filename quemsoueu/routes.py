from flask import render_template, url_for, flash, redirect, request, make_response
from quemsoueu import app, db
from quemsoueu.forms import RegistrationForm, CharacterForm
from quemsoueu.models import User, StartFlag
import random

@app.route("/", methods=['GET', 'POST'])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        res = make_response(redirect(url_for('wait')))
        res.set_cookie('myname', form.username.data, max_age=60*60*24)
        return res
    return render_template('home.html', form=form)


@app.route("/wait")
def wait():
    return render_template('wait.html', name=request.cookies.get('myname'))


@app.route("/set_characters", methods=['GET', 'POST'])
def set_characters():
    ready = list(db.engine.execute('SELECT COUNT(*) FROM User WHERE target IS NOT NULL'))
    #shuffler
    if len(ready) == 0:
        print('B')
        players = []
        users = User.query.all()
        for u in users:
            players.append(u.username)
        random.shuffle(players)
        for p in range(0,len(players)):
            result = db.engine.execute("UPDATE user SET target='{}' WHERE username='{}'".format(players[p-1], players[p]))
    mytarget = list(db.engine.execute("SELECT target FROM user WHERE username='{}'".format(request.cookies.get('myname'))))[0][0]
    db.session.commit()
    form = CharacterForm()
    if form.validate_on_submit():
        result = db.engine.execute("UPDATE user SET character='{}' WHERE username='{}'".format(form.character.data, request.cookies.get('myname')))
        db.session.commit()
        return redirect(url_for('game'))
    return render_template('set_characters.html', name=request.cookies.get('myname'),
        target = mytarget, form=form)

@app.route("/game")
def game():
    tuples = db.engine.execute("SELECT target, CASE WHEN target != '{}' THEN character ELSE '???' END as character FROM user".format(request.cookies.get('myname')))
    lst = list(tuples)
    return render_template('game.html', name=request.cookies.get('myname'), players = lst)


@app.route("/reset")
def reset():
    tuples = db.engine.execute("DELETE FROM user")
    db.session.commit()
    return render_template('reset.html')
