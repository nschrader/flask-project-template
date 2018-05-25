from flask_wtf import FlaskForm
from wtforms.fields import SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from dao import Departement
from bson.objectid import ObjectId

class FilterForm(FlaskForm):
    tous=ObjectId('666f6f2d6261722d71757578')
    choices_depart=[(d.pk, d.nom) for d in Departement.objects.all()]
    choices_depart.append((tous,'Tous'))
    choices_depart.reverse()
    departement = SelectField('Département INSA:',choices=choices_depart , coerce=ObjectId, validators=[DataRequired()])
    submit = SubmitField('Filtrer')
    doublediplome = BooleanField('Double Diplôme:')
    F_echange = BooleanField('\tEchange:')


    def is_tous_departements(self):
        return self.departement.data == self.__class__.tous
