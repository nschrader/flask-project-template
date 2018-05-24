import re
from flask_wtf import FlaskForm

from wtforms.fields import TextField, SelectField, StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField
from wtforms.fields.html5 import URLField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import ValidationError, url, length, regexp, optional, DataRequired, Email, EqualTo
from dao import Departement, Utilisateur, Universite
from bson.objectid import ObjectId

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

#TODO: Make this usable
class SettingsForm(FlaskForm):
    """docstring for SettingsForm"""

    ui_lang = SelectField(
        label="Primary site language",
        description="Site will try to show UI labels using this " +
            "language. User data will be shown in original languages.",
    )
    url = URLField(
        label="Personal site URL",
        description="If you have personal site and want to share " +
            "with other people, please fill this field",
        validators=[optional(), url(message="Invalid URL.")])
    username = TextField(
        label="Public profile address",
        description="Will be part of your public profile URL. Can " +
            "be from 2 up to 40 characters length, can start start from [a-z] " +
            "and contains only latin [0-9a-zA-Z] chars.",
        validators=[
            length(2, 40, message="Field must be between 2 and 40" +
            " characters long."),
            regexp(r"[a-zA-Z]{1}[0-9a-zA-Z]*",
                re.IGNORECASE,
                message="Username should start from [a-z] and " +
                    "contains only latin [0-9a-zA-Z] chars")
        ]
    )

class RegistrationForm(FlaskForm):
    prenom = StringField('Prénom', validators=[DataRequired()])
    nom = StringField('Nom', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    departement = SelectField('Département INSA', choices=[(d.pk, d.nom) for d in Departement.objects.all()], coerce=ObjectId, validators=[DataRequired()])
    niveau = SelectField('Année d\'études', choices=[('3', '3A'), ('4', '4A')], validators=[DataRequired()])
    mobilite = SelectField('J\'ai déjà effectué une mobilité internationale : ', choices=[(univ.pk, univ.nom) for univ in Universite.objects.all()], coerce=ObjectId, validators=None)
    mdp = PasswordField('Mot de passe', validators=[DataRequired()])
    mdp2 = PasswordField('Répétez le mot de passe', validators=[DataRequired(), EqualTo('mdp')])
    submit = SubmitField('S\'inscrire')


class LoginForm(FlaskForm):
    """Login form to access writing and settings pages"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    mdp = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi')

class EditUserProfileForm(FlaskForm):
    prenom = StringField('Prénom')
    nom = StringField('Nom')
    email = StringField('Email')
    departement = SelectField('Département INSA', choices=[(d.pk, d.nom) for d in Departement.objects.all()], coerce=ObjectId)
    niveau = SelectField('Année d\'études', choices=[('3', '3A'), ('4', '4A')])
    mobilite = SelectField('J\'ai déjà effectué une mobilité internationale : ', choices=[(univ.pk, univ.nom) for univ in Universite.objects.all()], coerce=ObjectId, validators=None)
    submit = SubmitField('Valider les changements')

class ChangePasswordForm(FlaskForm):
    mdp = PasswordField('Mot de passe actuel', validators=[DataRequired()])
    nouveau_mdp = PasswordField('Nouveau mot de passe', validators=[DataRequired()])
    nouveau_mdp2 = PasswordField('Répétez le nouveau mot de passe', validators=[EqualTo('nouveau_mdp')])
    submit = SubmitField('Valider le changement de mot de passe')

class DeleteUserForm(FlaskForm):
    mdp = PasswordField('Mot de passe requis', validators=[DataRequired()])
    submit = SubmitField('Supprimer mon compte (cette opération est irréversible)')
