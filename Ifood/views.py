from flask import render_template, request, redirect, url_for
from Ifood import app, db, ALLOWED_EXTENSIONS
from Ifood.models import User, Product, ProductImage
from Ifood.forms import LoginForm, ProductForm
from werkzeug import secure_filename
import PIL
import os


@app.route('/')
def home():
    products = Product.query.all()
    products_imgs = ProductImage.query.all()
    return render_template('index.html', products = products, products_imgs = products_imgs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('Auth/form.html', form=form)

@app.route('/produto/cadastro', methods=['GET', 'POST'])
def product_register():
   form = ProductForm()
   if request.method == 'POST':
      file = (request.files['file'])
      filename = secure_filename(file.filename)
      basedir = os.path.abspath(os.path.dirname(__file__))
      file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
      file_path = os.path.join('static/uploads/', filename)
      product = Product(name = form.name.data, thumbnail=file_path ,desc = form.description.data, price = form.price.data)
      db.session.add(product)
      db.session.commit()

      # files = request.files.getlist('images')
      # for file in files:
      #    filename = secure_filename(file.filename)
      #    basedir = os.path.abspath(os.path.dirname(__file__))
      #    print(basedir)
      #    file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
      #    teste = ('static/uploads/',filename)
      #    productimage = ProductImage(product_id = '3', image = teste)
      #    db.session.add(productimage)
      #    db.session.commit()

      return "sucesso"

   return render_template('admin/register/form.html', form=form)

@app.route('/produto/editar', methods=['GET','POST'])
def product_update():
   products = Product.query.all()
   return render_template('admin/upgrade/index.html', products = products)