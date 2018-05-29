from dao import Universite, Departement, Utilisateur, Pays

class VoeuxByUniversityDTO:
    def __init__(self, universite):
        us = Utilisateur.objects(voeux_annee__exists=True)
        self.universite = universite
        self._vx_1_by_with_smstr = [(u, u.voeu_1.semestre) for u in us if self.universite == u.voeu_1.universite]
        self._vx_2_by_with_smstr = [(u, u.voeu_2.semestre) for u in us if self.universite == u.voeu_2.universite]


    def has_voeux(self):
        return self._vx_1_by_with_smstr or self._vx_2_by_with_smstr


    def get_voeux(self):
        for u, s in self._vx_1_by_with_smstr:
            yield "{} ({}) {}A{}S (1er Voeu)".format(u.get_nom(), u.departement.nom, u.voeux_annee, s)
        for u, s in self._vx_2_by_with_smstr:
            yield "{} ({}) {}A{}S (2nd Voeu)".format(u.get_nom(), u.departement.nom, u.voeux_annee, s)


    @classmethod
    def get_for_pays(cls, pays):
        return [cls(u) for u in Universite.objects(pays=pays)]


    @classmethod
    def get_for_universite(cls, id):
        uni = Universite.objects.id_or_404(id)
        return cls(uni)


    @staticmethod
    def get_for_pays_and_departement(pays, departement):
        dtos = [VoeuxByUniversityDTO(universite=u) for u in Universite.objects(pays=pays)]
        dpt = Departement.objects.with_id(departement)
        for dto in dtos:
            dto.universite.echanges = [e for e in dto.universite.echanges if dpt in e.departements]
        return [d for d in dtos if d.universite.echanges]


class UniversityByPaysDTO:
    def __init__(self, pays):
        self.pays = pays
        self.universites = VoeuxByUniversityDTO.get_for_pays(pays)


    @classmethod
    def get(cls):
        return [cls(p) for p in Pays.objects]
