from flask_wtf import FlaskForm
from wtforms.fields import SelectField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from dao import Departement, Universite, Utilisateur
from bson.objectid import ObjectId

class ProfileForm(FlaskForm):
    non = ObjectId('666f6f2d6261722d71757578')
    prenom = StringField('Prénom', validators=[DataRequired()])
    nom = StringField('Nom', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    departement = SelectField('Département INSA', choices=Departement.get_choices(), coerce=ObjectId, validators=[DataRequired()])
    niveau = SelectField('Année d\'études', choices=Utilisateur.get_annee_choices(), validators=[DataRequired()])
    choix_mobilite = Universite.get_choices()
    choix_mobilite.append((non, 'Non'))
    choix_mobilite.reverse()
    mobilite = SelectField('J\'ai déjà effectué une mobilité internationale : ', choices=choix_mobilite, coerce=ObjectId, validators=[DataRequired()])

    def mobilite_is_non(self):
        return self.mobilite.data == self.__class__.non

class RegistrationForm(ProfileForm):
    mdp = PasswordField('Mot de passe', validators=[DataRequired()])
    mdp2 = PasswordField('Répétez le mot de passe', validators=[DataRequired(), EqualTo('mdp')])
    submit = SubmitField('S\'inscrire')

class EditUserProfileForm(ProfileForm):
    submit = SubmitField('Valider les changements')

class LoginForm(FlaskForm):
    """Login form to access writing and settings pages"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    mdp = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi')

class ChangePasswordForm(FlaskForm):
    mdp = PasswordField('Mot de passe actuel', validators=[DataRequired()])
    nouveau_mdp = PasswordField('Nouveau mot de passe', validators=[DataRequired()])
    nouveau_mdp2 = PasswordField('Répétez le nouveau mot de passe', validators=[EqualTo('nouveau_mdp')])
    submit = SubmitField('Valider le changement de mot de passe')

class ResetPasswordForm(ChangePasswordForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

class DeleteUserForm(FlaskForm):
    mdp = PasswordField('Mot de passe requis', validators=[DataRequired()])
    submit = SubmitField('Supprimer mon compte (cette opération est irréversible)')
