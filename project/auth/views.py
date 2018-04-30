from flask import render_template, redirect, request, current_app, g, flash, url_for, current_app as app
from flask_login import login_required, logout_user
from .models import User
from ..extensions import mongo
from .forms import SettingsForm

@app.route('/login')
def login():
    next_url = request.args.get('next') or request.referrer or None
    return render_template('auth/index.html', next=next_url)


@app.route('/loggedin')
def loggedin():
    return redirect(request.args.get('next') or url_for('frontend.index'))


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
    return redirect('/')
