import re
from flask_wtf import FlaskForm

from wtforms.fields import TextField, SelectField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import ValidationError, url, length, regexp, optional, DataRequired, Email, EqualTo
from dao import Departement, Utilisateur
from bson.objectid import ObjectId

# TODO : faire marcher EditAgreementForm et DeleteAgreementForm

class EditAgreementForm(FlaskForm):
    type = SelectField('Type d\'accord')
    departements = SelectField('Département INSA', choices=[(d.pk, d.nom) for d in Departement.objects.all()], coerce=ObjectId, validators=[DataRequired()])
    submit = SubmitField('S\'inscrire')

class DeleteAgreementForm(FlaskForm):
    submit = SubmitField('Supprimer l\'accord')
