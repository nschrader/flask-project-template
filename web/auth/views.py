from flask import render_template, redirect, request, g, flash, url_for, current_app as app
from flask_login import current_user, login_required, fresh_login_required, logout_user, login_user
from werkzeug.security import generate_password_hash

from dao import Utilisateur, Universite
from mail import send_to
from .forms import LoginForm, RegistrationForm, EditUserProfileForm, ChangePasswordForm, ResetPasswordForm, DeleteUserForm

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Un mail vous a été envoyé.')
        utilisateur = Utilisateur(
            nom = form.nom.data,
            prenom = form.prenom.data,
            mail = form.email.data,
            departement = form.departement.data,
            niveau = form.niveau.data,
            mobilites = [] if form.mobilite_is_non() else [form.mobilite.data] ,
            password = generate_password_hash(form.mdp.data))
        if Utilisateur.objects(mail = form.email.data).first() :
            flash("Il y a déjà un compte associé à cette adresse email", category='error')
        else :
            envoyer_mail(utilisateur)
            return redirect(url_for('login', mail = utilisateur.mail))
            #TODO: Pas logique, on contourne le sens d'un token
            '''utilisateur.make_token()
            utilisateur.save()
            debut_url = request.host_url
            debut_url = debut_url[:-1]
            send_to(utilisateur.mail, "Bli", debut_url + url_for("inscription_token", token = utilisateur.token, mail = utilisateur.mail))
            return redirect(url_for('login', mail = utilisateur.mail))'''
    return render_template('auth/inscription.html', form = form)

#TODO: On ne devrait pas avoir besoin du mail ici
@app.route('/inscription/<token>/<mail>')
def inscription_token(token, mail):
    utilisateur = Utilisateur.objects(mail = mail).first()
    if Utilisateur.verifify_token(token) == 1 :
        flash('Merci, votre inscription a été validée.')
        return redirect(url_for('login', mail = mail))
    elif Utilisateur.verifify_token(token) == 0 :
        envoyer_mail(utilisateur)
        flash("Un nouveau mail de confirmation vous a été envoyé", category='info')
        #TODO: Pas logique, on contourne le sens d'un token
        return redirect(url_for('login', mail = mail))
    else :
        #TODO: Pas logique, on n'arrive jamais ici
        utilisateur.delete()
        flash("Vous devez vous inscrire à nouveau", category='error')
        return redirect(url_for('inscription'))

#TODO: Faire marcher
'''@app.route('/reinitialiser-mdp/<mail>', methods=['GET', 'POST'])
def reinitialiser_mdp(mail):
    utilisateur = Utilisateur.objects(mail = mail).first()
    form = ResetPasswordForm(email = mail)
    if request.method == 'POST' and form.validate_on_submit() :
        envoyer_mail(utilisateur.mail)
    return render_template('auth/reinit_mdp.html', form=form)'''


#TODO: Il devrait pas y avoir besoin du mail. Ce truc ne fait aucon sens, on peut contrurner tout le systeme des tokens ?
@app.route('/login', defaults={'mail': None}, methods = ['GET', 'POST'])
@app.route('/login/<mail>', methods = ['GET', 'POST'])
def login(mail = None):
    form = LoginForm(email = mail)
    if request.method == 'POST' and form.validate_on_submit() :
        user = Utilisateur.objects(mail = form.email.data).first()
        if user :
            if user.validate_login(form.mdp.data) :
                if user.is_active :
                    if login_user(user, form.remember_me.data) :
                        flash("Vous êtes connecté", category='success')
                        return redirect(request.args.get("next") or url_for("index"))
                else :
                    flash("Votre inscription n'est pas confirmée", category='error')
                    return redirect(url_for('inscription_token', token = user.token, mail = user.mail))
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
    print(utilisateur.mobilites)
    form = EditUserProfileForm(
        prenom = utilisateur.prenom,
        nom = utilisateur.nom,
        email = utilisateur.mail,
        departement = utilisateur.departement.pk,
        niveau = str(utilisateur.niveau),
        mobilite = utilisateur.mobilites[0].pk if utilisateur.mobilites else [])
    if request.method == 'POST' and form.validate_on_submit():
        prenom = form.prenom.data
        nom = form.nom.data
        mail = form.email.data
        departement = form.departement.data
        niveau = form.niveau.data
        mobilites = [form.mobilite.data]
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
    url = debut_url + url_for("inscription_token", token = utilisateur.token, mail = utilisateur.mail)
    send_to(utilisateur.mail, "Bli", url)
