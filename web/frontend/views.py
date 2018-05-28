from flask import render_template, g, request, send_from_directory, redirect, current_app as app
from flask_login import login_required, current_user
from flask import render_template, flash, redirect, url_for

from dao import *
from .forms import FilterForm, WikiForm, DeleteAgreementForm, VoeuxForm, DeleteVoeuxForm, AjoutEchngForm
from .dtos import UniversiteForPaysDTO

@app.route('/')
@login_required
def index():
    return render_template('frontend/accueil.html')

@app.route('/pays/<id>', methods=['GET', 'POST'])
@login_required
def pays(id):
    pays = Pays.objects.id_or_404(id)
    dtos = UniversiteForPaysDTO.get_for_pays(pays)

    filter_form = FilterForm()
    vie_pratique = WikiForm (texte = pays.vie_pratique.text)
    tourisme = WikiForm (texte = pays.tourisme.text)
    culture = WikiForm (texte = pays.culture.text)
    climat = WikiForm (texte = pays.climat.text)

    if request.method == 'POST' :
        if filter_form.validate_on_submit() :
            if filter_form.is_tous_departements() :
                dtos = UniversiteForPaysDTO.get_for_pays(pays)
            else:
                dtos = UniversiteForPaysDTO.get_for_pays_and_departement(pays, filter_form.departement.data)
            for dto in dtos:
                if filter_form.doublediplome.data and not filter_form.F_echange.data :
                    dto.universite.echanges=[e for e in dto.universite.echanges if e.accord.nom == "Double Diplôme"]
                elif not filter_form.doublediplome.data and filter_form.F_echange.data :
                    dto.universite.echanges=[e for e in dto.universite.echanges if e.accord.nom != "Double Diplôme"]

    return render_template('frontend/pays.html',
        pays = pays,
        dtos = dtos,
        filter_form = filter_form,
        vie_pratique = vie_pratique,
        tourisme = tourisme,
        culture = culture,
        climat = climat
    )


@app.route('/pays/<id>/vie-pratique', methods=['POST'])
@login_required
def wiki_vie_pratique(id) :
    pays = Pays.objects.id_or_404(id)
    vie_pratique = WikiForm (texte = pays.vie_pratique.text)
    if request.method == 'POST' and vie_pratique.validate_on_submit() :
        pays.vie_pratique = Article(text=vie_pratique.texte.data)
        pays.save()
        flash("Vos modifications ont été enregistrées", category='success')
    return redirect(url_for('pays', id=id))

@app.route('/projet')
def projet():
    return render_template('frontend/projet.html')

@app.route('/universite/<id>')
@login_required
def universite(id):
    # TODO : faire marcher la suppression
    deleteForm = DeleteAgreementForm()
    if deleteForm.validate_on_submit():
        return redirect(url_for('suppr_accord', id = id))
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
        if form.universite_1.data == form.universite_2.data:
            flash("Il faut que les deux universités soient distinctes", category="error")
        else:
            flash("Vos voeux étaient bien enregistrés", category="success")
            current_user.voeu_1 = Voeu(
                universite=form.universite_1.data,
                semestre=form.semestre_1.data,
            )
            current_user.voeu_2 = Voeu(
                universite=form.universite_2.data,
                semestre=form.semestre_2.data,
            )
            current_user.voeux_annee = form.annee.data
            current_user.save()
            enregistre = True

    elif current_user.voeu_1 and current_user.voeu_2:
        form = VoeuxForm(
            universite_1 = current_user.voeu_1.universite.pk,
            universite_2 = current_user.voeu_2.universite.pk,
            semestre_1 = current_user.voeu_1.semestre,
            semestre_2 = current_user.voeu_2.semestre,
            annee = current_user.voeux_annee
        )
        enregistre = True

    return render_template('frontend/voeux.html', form=form, del_form=DeleteVoeuxForm(), enregistre=enregistre)

@app.route('/voeux/delete', methods=['POST'])
def delete_voeux():
    del_form=DeleteVoeuxForm()
    if del_form.validate_on_submit():
        current_user.voeu_1 = None
        current_user.voeu_2 = None
        current_user.voeux_annee = None
        current_user.save()
    return redirect(url_for("voeux"))

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(current_app.static_folder, request.path[1:])

@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.png')
