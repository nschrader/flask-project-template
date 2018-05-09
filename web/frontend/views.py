from flask import (render_template, g, request, url_for,
    current_app, send_from_directory, json, redirect, make_response, abort, current_app as app)

from flask_login import login_required, current_user

@app.route('/')
def index():
    return render_template('frontend/base_layout.html', user = current_user)
    
@app.route('/pays')
def pays():
    return render_template('frontend/pays.html', user = current_user)


@app.route('/robots.txt')
def static_from_root():
    # Static items
    return send_from_directory(current_app.static_folder, request.path[1:])


@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.png')
