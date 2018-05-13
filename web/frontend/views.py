from flask import render_template, g, request, send_from_directory, redirect, current_app as app

from flask_login import login_required, current_user

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
