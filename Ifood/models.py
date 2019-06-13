from Ifood import db
from sqlalchemy import Column, ForeignKey, Integer, Unicode, String, Float
from flask_appbuilder.models.mixins import ImageColumn
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(64), index=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Product(db.Model):
    id = Column(Integer, primary_key=True, unique=True)
    product_name = Column(String(120), index=True)
    product_img = Column(ImageColumn(
        size=(300, 300, True), thumbnail_size=(30, 30, True)))
    product_desc = Column(String(120), index=True)
    price = Column(Float, index=True)
