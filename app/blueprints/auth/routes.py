from flask import render_template, request, flash, redirect, url_for
from .import bp as auth
from .forms import LoginForm
from app.models import User
from flask_login import login_user


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        username = request.form.get("username").lower()
        password = request.form.get("password")
        u = User.query.filter_by(username=username).first()

        if u and u.checked_hashed_password(password):
            login_user(u)
            flash('You have logged in', 'success')
            return redirect(url_for("main.index"))
        error_string = "Invalid email and/or password."
        return render_template('login.html.j2', error = error_string, form=form)
    return render_template('login.html.j2', form=form)

# @auth.route('/register', methods = ['GET', 'POST'])
# def register():
