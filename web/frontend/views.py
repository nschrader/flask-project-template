from flask import render_template, g, request, send_from_directory, redirect, current_app as app
from flask_login import login_required, current_user
from flask import render_template, flash, redirect, url_for

@app.route('/')
def index():
    return render_template('frontend/accueil.html')

@app.route('/showLogin')
def show_login():
    return render_template('frontend/login_examples.html')

@app.route('/pays')
def pays():
    if request.method == 'POST':
        pass
    return render_template('frontend/pays.html')

@app.route('/editer')
def editer():
    return render_template('frontend/edit.html')
    
@app.route('/projet')
def projet():
    return render_template('frontend/projet.html')

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
