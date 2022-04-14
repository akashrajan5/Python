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
        return

    # codes to be added

    create_prod = {
        "name": str(data.get("name")),
        "type": "simple",
        "sku": str(data.get("sku")),
        "price": str(data.get("price")),
        "regular_price": str(data.get("regular_price")),
        "sale_price": str(data.get("sale_price")),
        "stock_status": str(data.get("stock_status")),
        "stock_quantity": int(data.get("stock_quantity")),
        "description": str(data.get("description")),
        "short_description": str(data.get("short_description")),
        "categories": [{"id": 9},{"id": 14}],
        "images": [{"src": str(img)} for img in img_link],
        "status":"publish", # draft, pending, private
        "weight": "",
        "dimensions": {"length": "", "width": "", "height": ""},
        "attributes": [
            {
                "id": 6,
                "name": "Color",
                "position": 0,
                "visible": false,
                "variation": true,
                "options": ["Black","Green"]
            },
            {
                "id": 0,
                "name": "Size",
                "position": 0,
                "visible": true,
                "variation": true,
                "options": ["S","M","L"]
            }
        ],
        "default_attributes": [
            {
                "id": 6,
                "name": "Color",
                "option": "black"
            },
            {
                "id": 0,
                "name": "Size",
                "option": "S"
            }
        ],
        "featured": False
    }


    # pdata = {}
    # pdata["name"] = data["name"]

    # cat_id_1 = get_category_id(pdata["Category1"])

    # res = woo_details().post("products", data).json()
    # if 'code' in res:
    #     print("Error, Details : ", res)
    # else:
    #     print("Product successfully created")

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

def create_category(data):
    if not data.get("name"):
        return "Name is mandatory, please provide a name."
    attributes = ["slug", "description"]
    category = {"name": str(data.get("name").capitalize()), "image": {"src": str(data.setdefault("image", "A default url has to be set"))}}
    for key, value in data.items():
        if key.lower() in attributes.lower():
            category.update({str(key.lower()): str(value)})
    response = woo_details().post("products/categories", category).json()
    return response.get("id")

def get_all_categories_data():
    all_category, page = list(), 1
    while True:
        all_cat = woo_details().get(f"products/categories?per_page=50&page={page}").json()
        if len(all_cat) == 0:
            break
        for cat in all_cat:
            all_category.append(cat)
        page =+ 1
    return all_category

def get_all_categories_name():
    all_categories, page = list(), 1
    while True:
        all_category = woo_details().get(f"products/categories?per_page=50&page={page}").json()
        if len(all_category) == 0:
            break
        for cat in all_category:
            all_categories.append(cat['name'])
        page += 1
    return all_categories

def get_category_id(category_name):
    category_array = get_all_categories_data()
    for cat in category_array:
        if str(category_name.capitalize()) == str(cat['name']):
            return cat['id']
    else:
        return create_category({"name": str(category_name.capitalize())})

def update_category(cat_id,name):
    data = {"name" : name.lower(), "image": "-----", "description": "hello"}
    updated = woo_details().put("products/categories/%d" % (cat_id), data).json()
    print(updated)
    print('Successfully Updated')

def remove_category(cat_id):
    if not isinstance(cat_id, int):
        return "Please provide a number as an id"
    else:
        removed = woo_details().delete("products/categories/%d" % (cat_id), params={"force": True}).json()
        return removed
