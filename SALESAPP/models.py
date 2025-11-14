import json
from base64 import encode
from datetime import datetime
from tkinter.font import names
from xmlrpc.client import boolean

from SALESAPP import db, app
from sqlalchemy import Column, Float, String, Boolean,DateTime
from sqlalchemy import Column, Float, String, Boolean, DateTime, Enum
from enum import Enum as RoleEnum
from flask_login import UserMixin

class UserRole(RoleEnum):
    USER=1
    ADMIN=2

class Base(db.Model):
    __abstract__= True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    active= Column(Boolean,default=True)
    created_date= Column(DateTime,default=datetime.now())

class Category(Base):
    products = db.relationship('Product', backref="category", lazy=True)

class User(Base,UserMixin):
    username=Column(String(150),unique= True, nullable=False)
    password=Column(String(150),nullable=False)
    avatar = Column(String(300),default="https://cdn-icons-png.freepik.com/512/3607/3607444.png")
    role=Column(Enum(UserRole),default=UserRole.USER)

class Product(Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(Float, default=0.0)
    image = db.Column(db.String(150),
                      default="https://cdn.tgdd.vn/Products/Images/522/221775/ipad-pro-12-9-inch-wifi-128gb-2020-xam-400x460-1-400x460.png")
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)

def auth_user (username,password):
    return User.query.

if __name__ == "__main__":
    with app.app_context():
       #  db.create_all()
       # # # db.drop_all()  # nếu muốn reset database
       # #
       # #   #Thêm category
       #  c1 = Category(name="Laptop")
       #  c2 = Category(name="Mobile")
       #  c3 = Category(name="Tablet")
       #  db.session.add_all([c1, c2, c3])
       # #  #Thêm product
       #  with open("data/product.json", encoding="utf-8") as f:
       #      products = json.load(f)
       #      for p in products:
       #       db.session.add(Product(**p))
       # #
       #  db.session.commit() #commit tất cả product 1 lần
        import  hashlib
        password = hashlib.md5("123".encode("utf-8")).hexdigest()
        #u1=User(name="User",username="user",password=password)
        u2 = User(name="User2", username="user2", password=password)

        db.session.add(u2)

        db.session.commit()