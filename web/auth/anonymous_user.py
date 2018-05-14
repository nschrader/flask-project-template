from flask_login import AnonymousUserMixin

class AnonymousUser(AnonymousUserMixin) :

        def get_nom(self):
            return "Anonyme"
