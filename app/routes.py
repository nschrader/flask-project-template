from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RegistrationForm
from dao import *

@app.route('/')

@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    form = LoginForm()
    if form.validate_on_submit() :
        flash('L\'utilisateur {} demande à se connecter, remember_me={}'.format(form.email.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('connexion.html', title='Connexion', form=form)

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    '''if current_user.is_authenticated:
        return redirect(url_for('index'))'''
    form = RegistrationForm()
    '''if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))'''
    if form.validate_on_submit() :
        flash('Merci, votre inscription a été validée.')
        utilisateur = Utilisateur(nom = form.nom.data,
            prenom = form.prenom.data,
            mail = form.email.data,
            departement = Departement(nom = str(form.departement.data)),
            niveau = form.niveau.data,
            mobilite = lambda n : True if form.mobilite.data == 'o' else False,
            password = form.mdp.data)
        utilisateur.insert()
        return redirect(url_for('connexion'))
    return render_template('inscription.html', title='S\'inscrire', form=form)
