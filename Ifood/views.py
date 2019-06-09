from flask import render_template, request, redirect, url_for

from Ifood import app, db
from Ifood.models import User, Product
from Ifood.forms import LoginForm

# ...

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('index.html', title='Sign In', form=form)


@app.route('/')
def home():
    products = Product.query.all()
    return render_template('index.html', products = products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('Auth/index.html', form=form)
