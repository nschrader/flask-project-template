from flask_wtf import FlaskForm
from wtforms.fields import SelectField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from dao import Departement,Universite
from bson.objectid import ObjectId

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
