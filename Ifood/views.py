from flask import render_template, request, redirect, url_for
from Ifood import app, db, ALLOWED_EXTENSIONS
from Ifood.models import User, Product, ProductImage
from Ifood.forms import LoginForm, ProductForm
from werkzeug import secure_filename
from datetime import datetime
import random
import PIL
import os


@app.route('/')
def home():
    carousel_products = carousel_list()
    new_products = new_products_list()
    sale_products = sale_products_list()
    popular_products = popular_products_list()
    products_imgs = ProductImage.query.all()
    now = datetime.now()
    return render_template('index.html', carousel_products=carousel_products ,new_products=new_products,sale_products=sale_products,popular_products=popular_products ,products_imgs=products_imgs, now=now)

def carousel_list():
    products = Product.query.all()
    carousel_products = []
    if (len(products) > 5):
        for i in range(0,5):
            numero = (random.randrange(0, (len(products))))
            if products[numero] not in carousel_products:
                carousel_products.append(products[numero])
    else:
        carousel_products = Product.query.all()
    return carousel_products

def sale_products_list():
    products = Product.query.all()
    sale_products = []
    if (len(products) > 8):
        for i in range(0, 8):
            max_sale = 0
            best_sale = ""

            for product in products:
                if (product.discount >= max_sale):
                    max_sale =  product.discount
                    best_sale = product

            products.remove(best_sale)
            sale_products.append(best_sale)
    else:
        sale_products = Product.query.all()
    return sale_products

def new_products_list():
    products = Product.query.all()
    new_products = []
    if (len(products) > 8):
        for i in range(0, 8):
            max_newer = 0
            newer_product = ""

            for product in products:
                if (datetime.now().day - product.created_at.day <=2):
                    max_newer =  product.discount
                    newer_product = product

            products.remove(newer_product)
            new_products.append(newer_product)
    else:
        new_products = Product.query.all()
    return new_products

def popular_products_list():
    products = Product.query.all()
    popular_products = []
    if (len(products) > 8):
        for i in range(0, 8):
            max_sold = 0
            most_sold = ""

            for product in products:
                if (product.sold >= max_sold):
                    max_sold = product.sold
                    most_sold = product


            products.remove(most_sold)
            popular_products.append(most_sold)
    else:
        popular_products = Product.query.all()
    return popular_products

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
        file_path = os.path.join('/static/uploads/', filename)
        product = Product(name=form.name.data, thumbnail=file_path,
                          desc=form.description.data, price=form.price.data, discount=form.discount.data,
                          tag=form.tag.data, created_at=datetime.now(), sold=0)
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

    return render_template('product/register/form.html', form=form)


@app.route('/produto/listar', methods=['GET', 'POST'])
def product_update():
    products = Product.query.all()
    return render_template('product/list/index.html', products=products)
