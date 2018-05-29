from flask import render_template, g, request, send_from_directory, redirect, current_app as app
from flask_login import login_required, current_user
from flask import render_template, flash, redirect, url_for

from dao import *
from .forms import FilterForm, WikiForm, DeleteAgreementForm, VoeuxForm, DeleteVoeuxForm, AjoutEchngForm
from .dtos import VoeuxByUniversityDTO, UniversityByPaysDTO

@app.route('/')
@login_required
def index():
    return render_template('frontend/accueil.html')

@app.route('/pays/<id>', methods=['GET', 'POST'])
@login_required
def pays(id):
    pays = Pays.objects.id_or_404(id)
    dtos = VoeuxByUniversityDTO.get_for_pays(pays)

    filter_form = FilterForm()
    vie_pratique = WikiForm (texte = Article.get_markup_for(pays.vie_pratique))
    tourisme = WikiForm (texte = Article.get_markup_for(pays.tourisme))
    culture = WikiForm (texte = Article.get_markup_for(pays.culture))
    climat = WikiForm (texte = Article.get_markup_for(pays.climat))

    if request.method == 'POST' and filter_form.validate_on_submit() :
        if filter_form.is_tous_departements() :
            dtos = VoeuxByUniversityDTO.get_for_pays(pays)
        else:
            dtos = VoeuxByUniversityDTO.get_for_pays_and_departement(pays, filter_form.departement.data)
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
    vie_pratique = WikiForm (texte = Article.get_markup_for(pays.vie_pratique))
    if request.method == 'POST' and vie_pratique.validate_on_submit() :
        pays.vie_pratique = Article(text=vie_pratique.texte.data)
        pays.save()
        flash("Vos modifications ont été enregistrées", category='success')
    return redirect(url_for('pays', id=id))


@app.route('/pays/<id>/tourisme', methods=['POST'])
@login_required
def wiki_tourisme(id) :
    pays = Pays.objects.id_or_404(id)
    tourisme = WikiForm (texte = Article.get_markup_for(pays.tourisme))
    if request.method == 'POST' and tourisme.validate_on_submit() :
        pays.tourisme = Article(text=tourisme.texte.data)
        pays.save()
        flash("Vos modifications ont été enregistrées", category='success')
    return redirect(url_for('pays', id=id))


@app.route('/pays/<id>/culture', methods=['POST'])
@login_required
def wiki_culture(id) :
    pays = Pays.objects.id_or_404(id)
    culture = WikiForm (texte = Article.get_markup_for(pays.culture))
    if request.method == 'POST' and culture.validate_on_submit() :
        pays.culture = Article(text=culture.texte.data)
        pays.save()
        flash("Vos modifications ont été enregistrées", category='success')
    return redirect(url_for('pays', id=id))


@app.route('/pays/<id>/climat', methods=['POST'])
@login_required
def wiki_climat(id) :
    pays = Pays.objects.id_or_404(id)
    climat = WikiForm (texte = Article.get_markup_for(pays.climat))
    if request.method == 'POST' and climat.validate_on_submit() :
        pays.climat = Article(text=climat.texte.data)
        pays.save()
        flash("Vos modifications ont été enregistrées", category='success')
    return redirect(url_for('pays', id=id))


@app.route('/projet')
def projet():
    return render_template('projet.html')

@app.route('/universite/<id>')
@login_required
def universite(id):
    # TODO : faire marcher la suppression
    deleteForm = DeleteAgreementForm()
    if deleteForm.validate_on_submit():
        return redirect(url_for('suppr_accord', id = id))

    univ = Universite.objects.id_or_404(id)
    dto = VoeuxByUniversityDTO.get_for_universite(id)

    cours = WikiForm (texte = Article.get_markup_for(univ.cours))
    accessibilite = WikiForm (texte = Article.get_markup_for(univ.accessibilite))
    logement = WikiForm (texte = Article.get_markup_for(univ.logement))
    ambiance = WikiForm (texte = Article.get_markup_for(univ.ambiance))

    return render_template('frontend/universite.html',
        universite=univ,
        deleteForm=deleteForm,
        cours=cours,
        accessibilite=accessibilite,
        logement=logement,
        ambiance=ambiance,
        dto=dto
    )


@app.route('/universite/<id>/cours', methods=['POST'])
@login_required
def wiki_cours(id) :
    univ = Universite.objects.id_or_404(id)
    cours = WikiForm (texte = Article.get_markup_for(univ.cours))
    if request.method == 'POST' and cours.validate_on_submit() :
        univ.cours = Article(text=cours.texte.data)
        univ.save()
        flash("Vos modifications ont été enregistrées", category='success')
    return redirect(url_for('univ', id=id))


@app.route('/universite/<id>/accessibilite', methods=['POST'])
@login_required
def wiki_accessibilite(id) :
    univ = Universite.objects.id_or_404(id)
    accessibilite = WikiForm (texte = Article.get_markup_for(univ.accessibilite))
    if request.method == 'POST' and accessibilite.validate_on_submit() :
        univ.accessibilite = Article(text=accessibilite.texte.data)
        univ.save()
        flash("Vos modifications ont été enregistrées", category='success')
    return redirect(url_for('univ', id=id))


@app.route('/universite/<id>/logement', methods=['POST'])
@login_required
def wiki_logement(id) :
    univ = Universite.objects.id_or_404(id)
    logement = WikiForm (texte = Article.get_markup_for(univ.logement))
    if request.method == 'POST' and logement.validate_on_submit() :
        univ.logement = Article(text=logement.texte.data)
        univ.save()
        flash("Vos modifications ont été enregistrées", category='success')
    return redirect(url_for('univ', id=id))


@app.route('/universite/<id>/ambiance', methods=['POST'])
@login_required
def wiki_ambiance(id) :
    univ = Universite.objects.id_or_404(id)
    ambiance = WikiForm (texte = Article.get_markup_for(univ.ambiance))
    if request.method == 'POST' and ambiance.validate_on_submit() :
        univ.ambiance = Article(text=ambiance.texte.data)
        univ.save()
        flash("Vos modifications ont été enregistrées", category='success')
    return redirect(url_for('univ', id=id))


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
            flash("Vos voeux ont bien été enregistrés", category="success")
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

    dtos = UniversityByPaysDTO.get()
    return render_template('frontend/voeux.html', form=form, del_form=DeleteVoeuxForm(), enregistre=enregistre, pays_dtos=dtos)

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
