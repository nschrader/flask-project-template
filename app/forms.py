from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from dao import Departement
from bson.objectid import ObjectId

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    mdp = PasswordField('Mot de passe', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Se connecter')

class RegistrationForm(FlaskForm):
    prenom = StringField('Prénom', validators=[DataRequired()])
    nom = StringField('Nom', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    departement = SelectField('Département INSA', choices=[(d._id, d.nom) for d in Departement.get_all()], coerce=ObjectId, validators=[DataRequired()])
    niveau = SelectField('Année d\'études', choices=[('3', '3A'), ('4', '4A')], validators=[DataRequired()])
    mobilite = SelectField('J\'ai déjà effectué une mobilité internationale : ', choices=[('o', 'Oui'), ('n', 'Non')], validators=[DataRequired()])
    mdp = PasswordField('Mot de passe', validators=[DataRequired()])
    mdp2 = PasswordField('Répétez le mot de passe', validators=[DataRequired(), EqualTo('mdp')])
    submit = SubmitField('S\'inscrire')
