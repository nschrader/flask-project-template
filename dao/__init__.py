from .pays import Pays
from .universite import Universite
from .utilisateur import Utilisateur
from .departement import Departement
from .continent import Continent
from .accord import Accord
from .article import Article

def set_std_user(user):
    for entity in [Departement, Universite, Pays, Continent, Accord, Article]:
        entity.std_user = user
