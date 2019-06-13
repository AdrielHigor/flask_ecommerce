from flask import render_template, request, redirect, url_for

from Ifood import app, db, ALLOWED_EXTENSIONS
from Ifood.models import User, Product
from Ifood.forms import LoginForm, ProductForm
from werkzeug import secure_filename
import os


@app.route('/')
def home():
    products = Product.query.all()
    return render_template('index.html', products = products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('Auth/form.html', form=form)

@app.route('/produto/cadastro', methods=['GET', 'POST'])
def upload_file():
   form = ProductForm()
   return render_template('Admin/Register/form.html', form=form)
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      file = request.files['file']
      filename = secure_filename(file.filename)
      print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      basedir = os.path.abspath(os.path.dirname(__file__))
      file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
      return 'file uploaded successfully'