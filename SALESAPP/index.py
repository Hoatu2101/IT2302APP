from tkinter.font import names

from flask import Flask, render_template

import dao

app = Flask(__name__)

@app.route("/")
def index():
    cates = dao.load_categories()
    prods=dao.load_products()
    return render_template("index.html",cates=cates,prods=prods)

if __name__ =="__main__":
    with app.app_context():
        app.run(debug=True)

