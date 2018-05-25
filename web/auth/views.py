from flask import render_template, redirect, request, g, flash, url_for, current_app as app
from flask_login import current_user, login_required, fresh_login_required, logout_user, login_user
from werkzeug.security import generate_password_hash

from dao import Utilisateur
from mail import send_to
from .forms import LoginForm, RegistrationForm, EditUserProfileForm, ChangePasswordForm, DeleteUserForm

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = RegistrationForm(mobilite='n')
    if form.validate_on_submit():
        flash('Un mail vous a été envoyé.')
        utilisateur = Utilisateur(
            nom = form.nom.data,
            prenom = form.prenom.data,
            mail = form.email.data,
            departement = form.departement.data,
            niveau = form.niveau.data,
            mobilites = [form.mobilite.data],
            password = generate_password_hash(form.mdp.data))
        if Utilisateur.objects(mail = form.email.data).first() :
            flash("Il y a déjà un compte associé à cette adresse email", category='error')
        else :
            utilisateur.make_token()
            utilisateur.save()
            print("USEEEEEEEER : " + str(utilisateur.token))
            debut_url = request.host_url
            debut_url = debut_url[:-1]
            send_to(utilisateur.mail, "Bli", debut_url + url_for("inscription_token", token=utilisateur.token))
            return redirect(url_for('login'))
    return render_template('auth/inscription.html', form = form)


@app.route('/inscription/<token>')
def inscription_token(token):
    if Utilisateur.verifify_token(token):
        flash('Merci, votre inscription a été validée.')
        return redirect(url_for('login'))
    else:
        flash("Votre token n'est pas bon, faites vous en renvoyer un.")
        return redirect(url_for("reset"))


@app.route("/reset")
def reset():
    return "Do stuff..."


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
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
                    return redirect(url_for("reset"))
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
    form = EditUserProfileForm(
        prenom = utilisateur.prenom,
        nom = utilisateur.nom,
        mail = utilisateur.mail,
        departement = utilisateur.departement.pk,
        niveau = str(utilisateur.niveau),
        mobilite = utilisateur.mobilites[0].pk if utilisateur.mobilites != [''] else '')
    if request.method == 'POST' and form.validate_on_submit():
        prenom = form.prenom.data
        nom = form.nom.data
        mail = form.email.data
        departement = form.departement.data
        niveau = form.niveau.data
        mobilites = [form.mobilite.data]
        utilisateur.update(prenom=prenom, nom=nom, mail=mail, departement=departement, niveau=niveau, mobilites=mobilites)
        utilisateur.save()
        flash(current_user.prenom, category='success')
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
        return render_template('auth/profil.html', title='Mon profil')
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
        utilisateur.remove()
        logout_user()
        flash("Votre compte a bien été supprimé", category='success')
        return render_template('frontend/accueil.html')
    return render_template('auth/suppr_profil.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
