from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RegistrationForm
from dao import *
from dao.set_db import dict_departements

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
    form = RegistrationForm()
    if form.validate_on_submit() :
        flash('Merci, votre inscription a été validée.')
        utilisateur = Utilisateur(nom = form.nom.data,
            prenom = form.prenom.data,
            mail = form.email.data,
            departement = form.departement.data,
            niveau = form.niveau.data,
            mobilite = True if form.mobilite.data == 'o' else False,
            password = form.mdp.data)
        utilisateur.insert()
        return redirect(url_for('connexion'))
    return render_template('inscription.html', title='S\'inscrire', form=form)
