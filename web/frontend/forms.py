from flask_wtf import FlaskForm
from wtforms.fields import SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from dao import Departement, Universite, Utilisateur, Voeu
from bson.objectid import ObjectId

class FilterForm(FlaskForm):
    tous=ObjectId('666f6f2d6261722d71757578')
    choices_depart=Departement.get_choices()
    choices_depart.append((tous,'Tous'))
    choices_depart.reverse()

    departement = SelectField('Département INSA:',choices=choices_depart, coerce=ObjectId, validators=[DataRequired()])
    submit = SubmitField('Filtrer')
    doublediplome = BooleanField('Double Diplôme:')
    F_echange = BooleanField('\tEchange:')


    def is_tous_departements(self):
        return self.departement.data == self.__class__.tous


class VoeuxForm(FlaskForm):
    universite_1 = SelectField("Université:", choices=Universite.get_choices(), coerce=ObjectId, validators=[DataRequired()])
    universite_2 = SelectField("Université:", choices=Universite.get_choices(), coerce=ObjectId, validators=[DataRequired()])
    annee_1 = SelectField("Année:", choices=Utilisateur.get_annee_choices(), validators=[DataRequired()])
    annee_2 = SelectField("Année:", choices=Utilisateur.get_annee_choices(), validators=[DataRequired()])
    semestre_1 = SelectField("Semestre:", choices=Voeu.get_semestre_choices(), validators=[DataRequired()])
    semestre_2 = SelectField("Semestre:", choices=Voeu.get_semestre_choices(), validators=[DataRequired()])
    submit = SubmitField("Soumettre")


class DeleteVoeuxForm(FlaskForm):
    submit = SubmitField("Supprimer mes voeux")


# TODO : faire marcher EditAgreementForm et DeleteAgreementForm
class EditAgreementForm(FlaskForm):
    type = SelectField('Type d\'accord')
    departements = SelectField('Département INSA', choices=Departement.get_choices(), coerce=ObjectId, validators=[DataRequired()])
    submit = SubmitField('S\'inscrire')


class DeleteAgreementForm(FlaskForm):
    submit = SubmitField('Supprimer l\'accord')
