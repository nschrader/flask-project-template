from flask import render_template, redirect, request, g, flash, url_for, current_app as app
from flask_login import current_user, login_required, fresh_login_required, logout_user, login_user
from werkzeug.security import generate_password_hash
from dao import Utilisateur, Universite
from mail import send_to
from web.mail import sendMail
from .forms import LoginForm, RegistrationForm, EditUserProfileForm, ChangePasswordForm, ResetPasswordForm, DeleteUserForm

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Un mail vous a été envoyé.')
        utilisateur = Utilisateur (
            nom = form.nom.data,
            prenom = form.prenom.data,
            mail = form.email.data,
            departement = form.departement.data,
            niveau = form.niveau.data,
            mobilites = [] if form.mobilite_is_non() else [form.mobilite.data],
            password = generate_password_hash(form.mdp.data)
        )
        if Utilisateur.objects(mail = form.email.data).first() :
            flash("Il y a déjà un compte associé à cette adresse email", category='error')
        else :
            envoyer_mail(utilisateur)
            return redirect(url_for('login', token = utilisateur.token))
    return render_template('auth/inscription.html', form = form)


@app.route('/inscription/<token>')
def inscription_token(token):
    utilisateur = Utilisateur.objects(token = token).first()
    if Utilisateur.verifify_token(token) == 1 :
        flash('Merci, votre inscription a été validée.')
        return redirect(url_for('login', token = token))
    elif Utilisateur.verifify_token(token) == 0 :
        envoyer_mail(utilisateur)
        flash("Un nouveau mail de confirmation vous a été envoyé", category='info')
        return redirect(url_for('login', token = token))
    else :
        utilisateur.delete()
        flash("Vous devez vous inscrire à nouveau", category='error')
        return redirect(url_for('inscription'))

#TODO: Faire marcher
@app.route('/reinitialiser-mdp/<token>', methods=['GET', 'POST'])
def reinitialiser_mdp(token):
    utilisateur = Utilisateur.objects(token = token).first()
    form = ResetPasswordForm(email = utilisateur.mail)
    if request.method == 'POST' and form.validate_on_submit() :
        envoyer_mail(utilisateur.mail)
    return render_template('auth/reinit_mdp.html', form=form)


@app.route('/login', defaults={'token': None}, methods = ['GET', 'POST'])
@app.route('/login/<token>', methods = ['GET', 'POST'])
def login(token = None):
    utilisateur = Utilisateur.objects(token = token).first() if token else None
    form = LoginForm(email = utilisateur.mail if utilisateur else "")
    if request.method == 'POST' and form.validate_on_submit() :
        utilisateur = Utilisateur.objects(mail = form.email.data).first()
        if utilisateur :
            if utilisateur.validate_login(form.mdp.data) :
                if utilisateur.is_active :
                    if login_user(utilisateur, form.remember_me.data) :
                        flash("Vous êtes connecté", category='success')
                        return redirect(request.args.get("next") or url_for("index"))
                else :
                    flash("Votre inscription n'est pas confirmée", category='error')
                    return redirect(url_for('inscription_token', token = utilisateur.token))
            else :
                flash("Email ou mot de passe erroné", category='error')
        else :
            flash("Pas de compte associé à cette adresse email", category='error')
    return render_template('auth/login.html', form=form)


@app.route('/profil')
@login_required
def profil() :
    return render_template('auth/profil.html')


@app.route('/modif-profil', methods=['GET', 'POST'])
@fresh_login_required
def modif_profil() :
    utilisateur = current_user
    form = EditUserProfileForm (
        prenom = utilisateur.prenom,
        nom = utilisateur.nom,
        email = utilisateur.mail,
        departement = utilisateur.departement.pk,
        niveau = str(utilisateur.niveau),
        mobilite = utilisateur.mobilites[0].pk if utilisateur.mobilites else []
    )
    if request.method == 'POST' and form.validate_on_submit():
        prenom = form.prenom.data
        nom = form.nom.data
        mail = form.email.data
        departement = form.departement.data
        niveau = form.niveau.data
        mobilites = [] if form.mobilite_is_non() else [form.mobilite.data]
        utilisateur.update(prenom=prenom, nom=nom, mail=mail, departement=departement, niveau=niveau, mobilites=mobilites)
        utilisateur.save()
        flash("Vos modifications ont été enregistrées", category='success')
        return redirect(url_for('profil'))
    return render_template('auth/modif_profil.html', form=form)


@app.route('/modif-mdp', methods=['GET', 'POST'])
@fresh_login_required
def modif_mdp() :
    utilisateur = current_user
    form = ChangePasswordForm()
    if request.method == 'POST' and form.validate_on_submit():
        if not utilisateur.validate_login(form.mdp.data) :
            flash("Mot de passe erroné", category='error')
            return render_template('auth/modif_mdp.html', form=form)
        utilisateur.password = generate_password_hash(form.nouveau_mdp.data)
        utilisateur.save()
        flash("Vos modifications ont été enregistrées", category='success')
        return render_template('auth/profil.html')
    return render_template('auth/modif_mdp.html', form=form)


@app.route('/suppr-compte', methods=['GET', 'POST'])
@fresh_login_required
def suppr_profil() :
    utilisateur = current_user
    form = DeleteUserForm()
    if request.method == 'POST' and form.validate_on_submit():
        if not utilisateur.validate_login(form.mdp.data) :
            flash("Mot de passe erroné", category='error')
            return render_template('auth/suppr_profil.html', form=form)
        utilisateur.delete()
        logout_user()
        flash("Votre compte a bien été supprimé", category='success')
        return render_template('frontend/accueil.html')
    return render_template('auth/suppr_profil.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


def envoyer_mail(utilisateur) :
    utilisateur.make_token()
    utilisateur.save()
    debut_url = request.host_url
    debut_url = debut_url[:-1]
    url = debut_url + url_for("inscription_token", token = utilisateur.token)
    print(utilisateur.mail)
    #send_to(utilisateur.mail, "Bli", url)
    sendMail(utilisateur.mail,url)
    return redirect(url_for('login', token = utilisateur.token))
