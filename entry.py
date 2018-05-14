from web import create_app
from extensions import mongo
from dao import Utilisateur

app = create_app(config='../local.cfg')

with app.app_context():
    import web.auth
    import web.frontend
    import web.mail
    import web.markdown

if __name__ == '__main__':
    try:
        Utilisateur.make_root(app.config["ROOT"], app.config["ROOT_PSWD"])
    except FileExistsError:
        pass
    
    app.run()
