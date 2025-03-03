# app/auth/routes.py
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.models import User
from app.auth.forms import LoginForm, RegistrationForm
from app.auth import bp


@bp.route("/login", methods=["GET", "POST"])
def login():
    # this property should return True if the user is authenticated
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", category="error")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("main.index"))
    return render_template("auth/login.html", title="Sign In", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            firstName=form.firstName.data,
            lastName=form.lastName.data,
            username=form.username.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!", category="success")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", title="Register", form=form)
