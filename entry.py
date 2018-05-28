from web import create_app
from dao import Utilisateur, StdUserProxy

app = create_app(config='../local.cfg')
StdUserProxy.set(Utilisateur.get_root())

with app.app_context():
    import web.auth
    import web.frontend

if __name__ == '__main__':
    app.run()
