from flask import render_template, request, redirect, url_for

from Ifood import app, db, ALLOWED_EXTENSIONS
from Ifood.models import User, Product
from Ifood.forms import LoginForm
from werkzeug.utils import secure_filename
import os
...

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/teste', methods=['GET', 'POST'])
# def teste():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <p><input type=file name=file>
#          <input type=submit value=Upload>
#     </form>
#     '''


@app.route('/')
def home():
    products = Product.query.all()
    return render_template('index.html', products = products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('Auth/index.html', form=form)
