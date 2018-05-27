from flask import render_template, g, request, send_from_directory, redirect, current_app as app
from flask_login import login_required, current_user
from flask import render_template, flash, redirect, url_for

from dao import *
from .forms import FilterForm, DeleteAgreementForm, VoeuxForm, DeleteVoeuxForm,AjoutEchngForm

@app.route('/')
@login_required
def index():
    return render_template('frontend/accueil.html')

@app.route('/pays/<id>', methods=['GET', 'POST'])
@login_required
def pays(id):
    form=FilterForm()
    pays=Pays.objects.id_or_404(id)

    if request.method == 'POST' and form.validate_on_submit():
        if form.is_tous_departements():
            univ_echng=Universite.get_with_echanges_for_pays(pays)
        else:
            univ_echng=Universite.get_with_echanges_for_pays_and_departement(pays, form.departement.data)
        if form.doublediplome.data and not form.F_echange.data :
            univ_echng=filter(lambda x: x[1].accord.nom == "Double Diplôme", univ_echng)
        elif not form.doublediplome.data and form.F_echange.data :
            univ_echng=filter(lambda x: x[1].accord.nom != "Double Diplôme", univ_echng)
    else:
        univ_echng=Universite.get_with_echanges_for_pays(pays)
    return render_template('frontend/pays.html', pays=pays, univ_echng=univ_echng, form=form)

@app.route('/editer')
@login_required
def editer():
    return render_template('frontend/edit.html')

@app.route('/projet')
def projet():
    return render_template('frontend/projet.html')

@app.route('/universite/<id>')
@login_required
def universite(id):
    # TODO : faire marcher la suppression
    deleteForm = DeleteAgreementForm()
    if deleteForm.validate_on_submit():
        return redirect(url_for('suppr-accord'))
    return render_template('frontend/universite.html', universite=Universite.objects.id_or_404(id), form=deleteForm)


@app.route('/ajout')
@login_required
def ajout():
    form=AjoutEchngForm()
    return render_template('frontend/ajout_echng.html',form=form)


@app.route('/suppr-accord/<id>')
def suppr_accord(id):
    return render_template('frontend/suppr_accord.html', universite=Universite.objects.id_or_404(id))

@app.route('/voeux', methods=['GET', 'POST'])
@login_required
def voeux():
    form = VoeuxForm()
    enregistre = False
    if request.method == 'POST' and form.validate_on_submit():
        invalid = False
        if form.universite_1.data == form.universite_2.data:
            invalid = True
            flash("Il faut que les deux universités soient distinctes", category="error")
        if form.annee_1.data != form.annee_2.data:
            invalid = True
            flash("Il faut que vous fassiez deux voeux pour la même année", category="error")
        if not invalid:
            flash("Vos voeux étaient bien enregistrés", category="success")
            current_user.voeu_1 = Voeu(
                universite=form.universite_1.data,
                annee=form.annee_1.data,
                semestre=form.semestre_1.data,
            )
            current_user.voeu_2 = Voeu(
                universite=form.universite_2.data,
                annee=form.annee_2.data,
                semestre=form.semestre_2.data,
            )
            current_user.save()
            enregistre = True

    elif current_user.voeu_1 and current_user.voeu_2:
        form = VoeuxForm(
            universite_1 = current_user.voeu_1.universite.pk,
            universite_2 = current_user.voeu_2.universite.pk,
            semestre_1 = current_user.voeu_1.semestre,
            semestre_2 = current_user.voeu_2.semestre,
            annee_1 = current_user.voeu_1.annee,
            annee_2 = current_user.voeu_2.annee
        )
        enregistre = True

    return render_template('frontend/voeux.html', form=form, del_form=DeleteVoeuxForm(), enregistre=enregistre)

@app.route('/voeux/delete', methods=['POST'])
def delete_voeux():
    del_form=DeleteVoeuxForm()
    if del_form.validate_on_submit():
        current_user.voeu_1 = None
        current_user.voeu_2 = None
        current_user.save()
    return redirect(url_for("voeux"))

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(current_app.static_folder, request.path[1:])

@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.png')
