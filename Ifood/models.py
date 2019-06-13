from Ifood import db
from sqlalchemy import Column, ForeignKey, Integer, Unicode, String, Float
from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy.orm import relationship
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
    product_imgs = image_attachment('ProductImage', uselist=True)
    product_desc = Column(String(120), index=True)
    price = Column(Float, index=True)

class ProductImage(db.Model, Image):
    product_id = Column(Integer, ForeignKey(Product.id), primary_key=True)
    product = relationship(Product)
    order_index = Column(Integer, primary_key=True)


