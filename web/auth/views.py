from flask import render_template, redirect, request, g, flash, url_for, current_app as app
from flask_login import current_user, login_required, logout_user, login_user

from dao import Utilisateur

from web.auth.forms import LoginForm, RegistrationForm, EditUserProfileForm, ChangePasswordForm, DeleteUserForm, SettingsForm
from werkzeug.security import generate_password_hash

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
            mobilites = [form.mobilite.data] if form.mobilite.data == 'o' else [],
            password = generate_password_hash(form.mdp.data))
        utilisateur.save()
        return redirect(url_for('login'))
    return render_template('auth/inscription.html', title = 'S\'inscrire', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Utilisateur.objects.get(mail = form.email.data)
        if user and user.validate_login(form.mdp.data):
            if form.remember_me.data:
                login_user(user, "rememberMe" in request.args)
            else :
                login_user(user)
            flash("Vous êtes connecté", category='success')
            return redirect(request.args.get("next") or url_for("index"))
        flash("Email ou mot de passe erroné", category='error')
    return render_template('auth/login.html', title='Se connecter', form=form)

@app.route('/profil', methods=['GET', 'POST'])
@login_required
def profil() :
    return render_template('auth/profil.html', title='Mon profil')

@app.route('/modif-profil', methods=['GET', 'POST'])
@login_required
def modif_profil() :
    utilisateur = current_user
    form = EditUserProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        prenom = form.prenom.data
        nom = form.nom.data
        mail = form.email.data
        departement = form.departement.data if form.departement.data else utilisateur.departement
        niveau = form.niveau.data if form.niveau.data else utilisateur.niveau
        mobilites = [form.mobilite.data] if form.mobilite.data == 'o' else utilisateur.mobilites # à modifier
        utilisateur.update(prenom=prenom, nom=nom, mail=mail, departement=departement, niveau=niveau, mobilites=mobilites)
        utilisateur.save()
        flash(current_user.prenom, category='success')
        flash("Vos modifications ont été enregistrées", category='success')
        return redirect(url_for('profil'))
    return render_template('auth/modif_profil.html', title='Modifier mes informations', form=form)

@app.route('/modif-mdp', methods=['GET', 'POST'])
@login_required
def modif_mdp() :
    utilisateur = current_user
    form = ChangePasswordForm()
    if request.method == 'POST' and form.validate_on_submit():
        if not utilisateur.validate_login(form.mdp.data) :
            flash("Mot de passe erroné", category='error')
            return render_template('auth/modif_mdp.html', title='Modifier mon mot de passe', form=form)
        utilisateur.password = generate_password_hash(form.nouveau_mdp.data)
        utilisateur.save()
        flash("Vos modifications ont été enregistrées", category='success')
        return render_template('auth/profil.html', title='Mon profil')
    return render_template('auth/modif_mdp.html', title='Modifier mon mot de passe', form=form)

@app.route('/suppr-compte', methods=['GET', 'POST'])
@login_required
def suppr_profil() :
    utilisateur = current_user
    form = DeleteUserForm()
    if request.method == 'POST' and form.validate_on_submit():
        if not utilisateur.validate_login(form.mdp.data) :
            flash("Mot de passe erroné", category='error')
            return render_template('auth/suppr_profil.html', title='Supprimer mon compte', form=form)
        utilisateur.remove()
        logout_user()
        flash("Votre compte a bien été supprimé", category='success')
        return render_template('frontend/accueil.html')
    return render_template('auth/suppr_profil.html', title='Supprimer mon compte', form=form)

#TODO: Make this work
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
    return redirect(url_for('index'))
