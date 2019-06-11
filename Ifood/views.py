from flask import render_template, request, redirect, url_for

from Ifood import app, db
from Ifood.models import User, Product
from Ifood.forms import LoginForm
from werkzeug import secure_filename
import os

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

@app.route('/upload')
def upload_file():
   return render_template('uploads/upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      print(os.path.join(app.config['UPLOAD_FOLDER']))
      #f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return 'file uploaded successfully'