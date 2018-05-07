from flask import render_template, redirect, request, current_app, g, flash, url_for, current_app as app
from flask_login import login_required, logout_user, login_user
from .models import User
from ..extensions import mongo
from .forms import SettingsForm, LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = mongo.users.find_one({"_id": form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            flash("Logged in successfully", category='success')
            return redirect(request.args.get("next") or url_for("index"))
        flash("Wrong username or password", category='error')
    return render_template('auth/login.html', title='login', form=form)


@app.route('/loggedin')
def loggedin():
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html')


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingsForm(request.form, g.user)
    form.ui_lang.choices = current_app.config['LANGUAGES'].items()

    if form.validate_on_submit():
        form.populate_obj(g.user)
        #TODO: Needs to be ported to mongo db
        #db.session.add(g.user)
        #db.session.commit()
        flash("Settings saved")

    return render_template('auth/settings.html', languages=current_app.config['LANGUAGES'], form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
