from SALESAPP import app
from models import Category, Product


def load_categories():
    # with open("data/category.json",encoding="utf-8") as f:
    #     return json.load(f)
    return Category.query.all()


def load_products(q=None, cate_id=None, page=None):
    # with open("data/product.json",encoding="utf-8") as f:
    #     products = json.load(f)
    #     if q:
    #         products =[p for p in products if p["name"].find(q)>=0]
    #     if cate_id:
    #         products = [p for p in products if p["category_id"] == int(cate_id)]
    #     return products
    query = Product.query
    if q:
              query = query.filter(Product.name.contains(q))
    if cate_id:
            query = query.filter(Product.category_id==int(cate_id))
    if page:
            size = app.config["PAGE_SIZE"]
            start = (int(page) - 1) * size
            query = query.slice(start, start + size)
    return query.all()


def get_product_by_id(id):
    # # """
    # #
    # # :param id:
    # # :return:
    # # """
    # # with open("data/product.json",encoding="utf-8") as f:
    # #     products = json.load(f)
    # #     for p in products:
    # #         if p["id"].__eq__(id):
    #             return p
    # return None
    return Product.query.get(id)

def count_product():
    return Product.query.count()
if __name__ == "__main__":
    print(load_categories())
    print(load_products())
    print(get_product_by_id(2))
