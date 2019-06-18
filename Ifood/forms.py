from flask_wtf import FlaskForm
from wtforms import StringField, MultipleFileField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message=('Este campo é obrigatório'))
        ])
    password = PasswordField('Password', validators=[
        DataRequired(message=('Este campo é obrigatorio'))
        ])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    name = StringField('Nome', validators=[
        DataRequired(message=('Este campo é obrigatório'))
        ])
    last_name = StringField('Sobrenome', validators=[
        DataRequired(message=('Este campo é obrigatório'))
        ])
    endereco = StringField('Endereço', validators=[
        DataRequired(message=('Este campo é obrigatório'))
        ])
    email = StringField('E-mail', validators=[
        DataRequired(message=('Este campo é obrigatório'))
        ])
    cpf = StringField('CPF', validators=[
        DataRequired(message=('Este campo é obrigatório'))
        ])
    born_at = StringField('Username', validators=[
        DataRequired(message=('Este campo é obrigatório'))
        ])

class ProductForm(FlaskForm):
    name = StringField('Nome do Produto', validators=[
        DataRequired()
        ])
    description = TextAreaField('Descrição')
    images = MultipleFileField('Imagens do Produto')
    file = FileField('Thumbnail do Produto')
    price = StringField("Preço R$:", validators=[
        DataRequired(message="Este campo é obrigatório")
    ])
    discount = StringField("Desconto:")
    tag = StringField("Tag do produto")
    submit = SubmitField('Cadastrar')