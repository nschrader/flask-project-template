from flask import render_template, g, request, send_from_directory, redirect, current_app as app
from flask_login import login_required, current_user
from flask import render_template, flash, redirect, url_for
from web.auth.forms import LoginForm, RegistrationForm
from dao import *

@app.route('/')
def index():
    return render_template('frontend/accueil.html')

@app.route('/showLogin')
def show_login():
    return render_template('frontend/login_examples.html')

@app.route('/pays')
def pays():
    return render_template('frontend/pays.html')

@app.route('/universite')
def universite():
    return render_template('frontend/universite.html')

@app.route('/voeux')
def voeux():
    return render_template('frontend/voeux.html')

@app.route('/robots.txt')
def static_from_root():
    # Static items
    return send_from_directory(current_app.static_folder, request.path[1:])


@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.png')

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = RegistrationForm()
    if form.validate_on_submit() :
        flash('Merci, votre inscription a été validée.')
        utilisateur = Utilisateur(
            nom = form.nom.data,
            prenom = form.prenom.data,
            mail = form.email.data,
            departement = form.departement.data,
            niveau = form.niveau.data,
            mobilite = True if form.mobilite.data == 'o' else False,
            password = form.mdp.data)
        utilisateur.insert()
        return redirect(url_for('connexion'))
    return render_template('frontend/inscription.html', title='S\'inscrire', form=form)
