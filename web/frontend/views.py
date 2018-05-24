from flask import render_template, g, request, send_from_directory, redirect, current_app as app
from flask_login import login_required, current_user
from flask import render_template, flash, redirect, url_for

from web.frontend.forms import DeleteAgreementForm

from dao import *

@app.route('/')
@login_required
def index():
    return render_template('frontend/accueil.html')

@app.route('/pays/<id>')
@login_required
def pays(id):
    # TODO: What is this doing ?
    # if request.method == 'POST':
    #    pass
    return render_template('frontend/pays.html', pays=Pays.objects.id_or_404(id))

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

@app.route('/suppr-accord/<id>')
def suppr_accord(id):
    return render_template('frontend/suppr_accord.html', universite=Universite.objects.id_or_404(id))

@app.route('/voeux')
@login_required
def voeux():
    return render_template('frontend/voeux.html')

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(current_app.static_folder, request.path[1:])

@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.png')
