from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired
 
class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    
class CadastroUserForm(FlaskForm):
    login= StringField("username", validators=[DataRequired()])
    senha = PasswordField("password", validators=[DataRequired()])
    name = StringField("name")
    email = StringField("email")

class CadastroLivroForm(FlaskForm):
    nome = StringField("name")
    autor = StringField("autor")
    categoria = StringField("categoria")
    idioma = StringField("Idioma")

class RemoverLivroForm(FlaskForm):
    id = IntegerField("id")
    
class AlterarLivroForm(FlaskForm):
    id = IntegerField("id", validators=[DataRequired()])
    nome = StringField("name")
    autor = StringField("autor")
    categoria = StringField("categoria")
    idioma = StringField("Idioma")