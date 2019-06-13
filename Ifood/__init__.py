from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


UPLOAD_FOLDER = 'Ifood/static/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = 'you-will-never-guess'

from Ifood import views, models