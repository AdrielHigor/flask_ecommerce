from flask_wtf import FlaskForm
from wtforms import StringField, MultipleFileField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message=('Este campo é obrigatório'))
        ])
    password = PasswordField('Password', validators=[
        DataRequired()
        ])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ProductForm(FlaskForm):
    name = StringField('Nome do Produto', validators=[
        DataRequired()
        ])
    description = TextAreaField('Descrição')
    images = MultipleFileField('Imagens do Produto')
    price = StringField("Preço", validators=[
        DataRequired(message="Este campo é obrigatório")
    ])
    submit = SubmitField('Cadastrar')