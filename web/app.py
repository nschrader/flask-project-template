from os import path
from flask import Flask, request, render_template, g
from flask_login import current_user
from extensions import mongo, login_manager, mail


def create_app(config=None, app_name='Project Whiskey'):
    app = Flask(app_name,
        static_folder=path.join(path.dirname(__file__), '..', 'static'),
        template_folder="static/templates"
    )

    app.config.from_object('config')
    if config:
        app.config.from_pyfile(config, silent=True)

    extensions_fabrics(app)
    error_pages(app)
    gvars(app)

    return app


def extensions_fabrics(app):
    mail.init_app(app)
    login_manager.init_app(app)


def error_pages(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("misc/403.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("misc/404.html"), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return render_template("misc/405.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("misc/500.html"), 500


def gvars(app):
    @app.before_request
    def gdebug():
        if app.debug:
            g.debug = True
        else:
            g.debug = False

    with app.app_context():
        from .models import User

    @login_manager.user_loader
    def load_user(username):
        u = mongo.users.find_one({"_id": username})
        if not u:
            return None
        return User(u['_id'])

    @app.before_request
    def guser():
        g.user = current_user

    @app.context_processor
    def inject_user():
        try:
            return {'user': g.user}
        except AttributeError:
            return {'user': None}