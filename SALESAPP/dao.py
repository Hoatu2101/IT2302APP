import json
from Scripts.unicodedata import category


def load_categories():
    with open("data/category.json",encoding="utf-8") as f:
        return json.load(f)
def load_products():
    with open("data/product.json",encoding="utf-8") as f:
        return json.load(f)


if __name__=="__main__":
    print(load_categories())
    print(load_products())