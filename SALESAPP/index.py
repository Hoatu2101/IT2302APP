import math
from tkinter.font import names

from flask import Flask, render_template, request
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from flask_login import  login_user,current_user
import dao
from SALESAPP import app,login


@app.route("/")

def index():
    q = request.args.get("q")
    cate_id=request.args.get("cate_id")
    page=request.args.get("page")
    cates = dao.load_categories()
    pages = math.ceil(dao.count_product() / app.config["PAGE_SIZE"])
    prods = dao.load_products(q=q,cate_id=cate_id,page=page)
    return render_template("index.html", prods=prods,pages=pages)


@app.route("/products/<int:id>")
def details(id):
    return render_template("products_details.html", prod=dao.get_product_by_id(id))


@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }
@app.route("/login", methods=['get', 'post'])

def login_my_user():
    err_msg=None
    if request.method.__eq__('POST'):
     username = request.form.get("username")
     password= request.form.get("password")
     if username=="user" and password =="123":
         return  redirect('/')
     else:
         err_msg="Tên đăng nhập hoặc mật khẩu không đúng"

    return render_template("login.html",err_msg=err_msg)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
