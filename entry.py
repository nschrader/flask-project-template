from web import create_app
from extensions import mongo
from dao import Utilisateur, set_std_user

app = create_app(config='../local.cfg')

with app.app_context():
    import web.auth
    import web.frontend
    import web.mail
    import web.markdown

if __name__ == '__main__':
    try:
        root = Utilisateur.make_root(app.config["ROOT"], app.config["ROOT_PSWD"])
        set_std_user(root)
    except FileExistsError:
        root = Utilisateur.get_mail(app.config["ROOT"])
    finally:
        set_std_user(root)

    app.run()
