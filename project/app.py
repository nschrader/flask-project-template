import os
from flask import Flask, request, render_template, g

from .extensions import (mongo, login_manager)


def create_app(config=None, app_name='project', blueprints=None):
    app = Flask(app_name,
        static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'),
        template_folder="templates"
    )

    app.config.from_object('project.config')
    app.config.from_pyfile('../local.cfg', silent=True)
    if config:
        app.config.from_pyfile(config)

    configure_logging(app)
    error_pages(app)
    gvars(app)

    return app


def extensions_fabrics(app):
    db.init_app(app)
    mail.init_app(app)
    babel.init_app(app)
    pages.init_app(app)
    init_social(app, db)
    login_manager.init_app(app)
    manager.init_app(app, flask_sqlalchemy_db=db)
    migrate.init_app(app, db)
    csrf.init_app(app)
    cache.init_app(app)
    celery.config_from_object(app.config)


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

    app.context_processor(backends)

    from .models import User

    @login_manager.user_loader
    def load_user(userid):
        try:
            return User.query.get(int(userid))
        except (TypeError, ValueError):
            pass

    @app.before_request
    def guser():
        g.user = current_user

    @app.context_processor
    def inject_user():
        try:
            return {'user': g.user}
        except AttributeError:
            return {'user': None}
