import json

from SALESAPP import db, app
from sqlalchemy import Column, Float


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Product', backref="category", lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(Float, default=0.0)
    image = db.Column(db.String(150),
                      default="https://cdn.tgdd.vn/Products/Images/522/221775/ipad-pro-12-9-inch-wifi-128gb-2020-xam-400x460-1-400x460.png")
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
       # db.drop_all()  # nếu muốn reset database

        #  Thêm category
        # c1 = Category(name="Laptop")
        # c2 = Category(name="Mobile")
        # c3 = Category(name="Tablet")
        # db.session.add_all([c1, c2, c3])
        #Thêm product
        with open("data/product.json", encoding="utf-8") as f:
            products = json.load(f)
            for p in products:
             db.session.add(Product(**p))

        db.session.commit() #commit tất cả product 1 lần
