from flask import (render_template, g, request, url_for,
    current_app, send_from_directory, json, redirect, make_response, abort, current_app as app)

from flask_login import login_required, current_user

from ..extensions import pages

@app.route('/')
def index():
    return render_template('frontend/index.html', user = current_user)


@app.route('/docs/', defaults={'path': 'index'})
@app.route('/docs/<path:path>/', endpoint='page')
def page(path):
    # Documentation views
    _page = pages.get_or_404(path)
    return render_template('page.html', page=_page)


@app.route('/robots.txt')
def static_from_root():
    # Static items
    return send_from_directory(current_app.static_folder, request.path[1:])


@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.png')
