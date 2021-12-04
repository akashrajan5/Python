import json
from woocommerce import API
import requests


def woo_details():
    wcapi = API(
                url="store-url",
                consumer_key="consumer key from store",
                consumer_secret="consumer secret key from store",
                wp_api=True,
                version="wc/v3",
                timeout=180,
                query_string_auth=True
            )
    return wcapi

def all_products_json():
    all_products = woo_details().get("products").json()
    print(all_products)

def list_products_names():
    all_products = woo_details().get("products").json()
    for prod_name in all_products:
        print(prod_name['name'])

def product_details(prod_id):
    if prod_id:
        product = woo_details().get("products/%d" % (prod_id)).json()
        print(product)
    else:
        print("Please provide a product id.")

def create_product(data):
    if data is None:
        print("Products data is empty.")
    else :
        pdata = {}
        pdata["name"] = data["name"]

        cat_id_1 = get_category_id(pdata["Category1"])

        res = woo_details().post("products", data).json()
        if 'code' in res:
            print("Error, Details : ", res)
        else:
            print("Product successfully created")

def update_product(prod_id, data):
    if isinstance(prod_id, int):
        woo_details().put("products/%d" % (prod_id), data).json()
    else:
        return "Please provide a proper id value"
    
def remove_product(prod_id):
    if prod_id is None:
        print("Error : Please provide an id value.")
    elif not isinstance(prod_id, int):
        print("Error : Please provide an id number")
    else:
        res = woo_details().delete("products/%d" % (prod_id), params={"force": True}).json()
        if 'code' in res:
            print("Error : Id not found. Please provide a valid id value")
        else:
            print("Successfully Removed")

def get_all_categories_data():
    all_category = []
    page = 1
    while True:
        all_cat = woo_details().get(f"products/categories?per_page=50&page={page}").json()
        if len(all_cat) == 0:
            break
        for cat in all_cat:
            all_category.append(cat)
        page = page + 1
    return all_category

def get_all_categories_name():
    all_category = []
    page = 1
    while True:
        all_cat = woo_details().get(f"products/categories?per_page=50&page={page}").json()
        if len(all_cat) == 0:
            break
        for cat in all_cat:
            all_category.append(cat['name'].lower())
        page = page + 1
    for x in all_category:
        print(x)

def get_category_id(name):
    category_array = get_all_categories_data()
    for cat in category_array:
        if name.lower() == cat['name'].lower():
            print(cat['id'])
            return
    else:
        data = {
            "name": str(name),
            "image": {
                "src": ""
            }
        }
        res = woo_details().post("products/categories", data).json()
        print(res)
        print('Successful : Category created')

def create_category(cat_name, img_link):
    data = {
        "name": str(cat_name),
        "image": {
            "src": img_link
        }
    }
    cat = woo_details().post("products/categories", data).json()
    print(cat)

def update_category(cat_id,name):
    data = {
        "name" : name.lower(),
    }
    updated = woo_details().put("products/categories/%d" % (cat_id), data).json()
    print(updated)
    print('Successfully Updated')

def remove_category(cat_id):
    if not isinstance(cat_id, int):
        return "Please provide a number as an id"
    else:
        removed = woo_details().delete("products/categories/%d" % (cat_id), params={"force": True}).json()
        return removed
