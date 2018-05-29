from flask_wtf import FlaskForm
from wtforms.fields import SelectField, BooleanField, SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired
from dao import Departement, Universite, Utilisateur, Voeu, Accord
from bson.objectid import ObjectId

class FilterForm(FlaskForm):
    tous=ObjectId('666f6f2d6261722d71757578')
    choices_depart=Departement.get_choices()
    choices_depart.append((tous,'Tous'))
    choices_depart.reverse()

    departement = SelectField('Département INSA:', choices=choices_depart, coerce=ObjectId, validators=[DataRequired()])
    submit = SubmitField('Filtrer')
    doublediplome = BooleanField('Doubles diplômes:')
    F_echange = BooleanField('\tEchanges:')


    def is_tous_departements(self):
        return self.departement.data == self.__class__.tous


class WikiForm(FlaskForm):
    texte = TextAreaField()
    enregistrer = SubmitField('Enregistrer')


class VoeuxForm(FlaskForm):
    universite_1 = SelectField("Université:", choices=Universite.get_choices(), coerce=ObjectId, validators=[DataRequired()])
    universite_2 = SelectField("Université:", choices=Universite.get_choices(), coerce=ObjectId, validators=[DataRequired()])
    semestre_1 = SelectField("Semestre:", choices=Voeu.get_semestre_choices(), validators=[DataRequired()])
    semestre_2 = SelectField("Semestre:", choices=Voeu.get_semestre_choices(), validators=[DataRequired()])
    annee = SelectField("Année:", choices=Utilisateur.get_annee_choices(), validators=[DataRequired()])
    submit = SubmitField("Soumettre")


class DeleteVoeuxForm(FlaskForm):
    submit = SubmitField("Supprimer mes voeux")


# TODO : faire marcher EditAgreementForm et DeleteAgreementForm
class AgreementForm(FlaskForm):
    type = SelectField('Type d\'accord', choices=Accord.get_choices(), validators=[DataRequired()])
    #departements = SelectField('Département INSA', choices=Departement.get_choices(), coerce=ObjectId, validators=[DataRequired()])
    nb_places_TC = SelectField('Nombre de places', choices=[(i, i) for i in range(0,16)], validators=[DataRequired()])
    nb_mois_TC = SelectField('Nombre de mois', choices=[(5, '5'), (10, '10')], validators=[DataRequired()])

class CreateAgreementForm(AgreementForm):
    submit = SubmitField('Ajouter l\'accord')

class EditAgreementForm(AgreementForm):
    submit = SubmitField('Valider les changements')

class DeleteAgreementForm(FlaskForm):
    submit = SubmitField('Supprimer l\'accord')

class AjoutEchngForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    type = SelectField('Type d\'accord')
    #TODO faire marcher pour durée du séjour
    departements = SelectField('Département INSA', choices=[(d.pk, d.nom) for d in Departement.objects.all()], coerce=ObjectId, validators=[DataRequired()])
    submit = SubmitField("Créer l'accord")
