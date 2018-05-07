from project import create_app, mongo
from werkzeug.security import generate_password_hash

app = create_app(config='../local.cfg')

#TODO: this shit shouldn't be here
with app.app_context():
    import project.frontend
    import project.mail

def makeRoot():
    root = app.config["ROOT"];
    root_pswd = app.config["ROOT_PSWD"]
    if not mongo.users.find_one({"_id": root}):
        hash = generate_password_hash(root_pswd, method='pbkdf2:sha256')
        mongo.users.insert({"_id": root, "password": hash})

if __name__ == '__main__':
    makeRoot()
    app.run()
