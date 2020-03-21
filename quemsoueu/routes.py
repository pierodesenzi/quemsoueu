from flask import render_template, url_for, flash, redirect, request, make_response
from quemsoueu import app, db
from quemsoueu.forms import RegistrationForm
from quemsoueu.models import User, StartFlag


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
        print(form.username.data)
        print(request.cookies.get('myname'))
        return res
    return render_template('home.html', form=form)


@app.route("/wait")
def wait():
    return render_template('wait.html', name=request.cookies.get('myname'))
    
