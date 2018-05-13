from flask import render_template, g, request, send_from_directory, redirect, current_app as app
from flask_login import login_required, current_user
from flask import render_template, flash, redirect, url_for
from web.auth.forms import LoginForm, RegistrationForm
from dao import *

@app.route('/')
def index():
    return render_template('frontend/voeux.html')

@app.route('/showLogin')
def show_login():
    return render_template('frontend/login_examples.html')

@app.route('/pays')
def pays():
    return render_template('frontend/pays.html')

@app.route('/robots.txt')
def static_from_root():
    # Static items
    return send_from_directory(current_app.static_folder, request.path[1:])


@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.png')

@app.route('/voeux.html')
def voeux():
        return render_template('frontend/voeux.html')

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    #'''if current_user.is_authenticated:
    #    return redirect(url_for('index'))'''
    form = RegistrationForm()
#    '''if form.validate_on_submit():
    #    user = User(username=form.username.data, email=form.email.data)
    #    user.set_password(form.password.data)
        #db.session.add(user)
    #    db.session.commit()
        #"flash('Congratulations, you are now a registered user!')
    #    #return redirect(url_for('login'))'''
    #if form.validate_on_submit() :
        #flash('Merci, votre inscription a été validée.')
        #utilisateur = Utilisateur(nom = form.nom.data,
        #    prenom = form.prenom.data,
        #    mail = form.email.data,
    #    departement = Departement(nom = form.departement.data),
        #    niveau = form.niveau.data,
            #mobilite = lambda n : True if form.mobilite.data == 'o' else False,
            #password = form.mdp.data)
        #utilisateur.insert()
        #return redirect(url_for('connexion'))
    return render_template('frontend/inscription.html', title="S'inscrire", form=form)
