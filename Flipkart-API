import requests
import json
import pdb

# https://seller.flipkart.com/api-docs/index.html - Flipkart API docs link

FLIPKART_MARKETPLACEAPI_URL = 'https://seller.api.flipkart.net'
AUTH_TOKEN = "" # Flipkart auth token generated using clientid and clientSecret, clientid and ClientSecret is received by mail and register new application for auth token. 

# get product details using skuid
def get_product_details_from_sku(sku_id):
    token = AUTH_TOKEN
    if token and sku_id:
        url = FLIPKART_MARKETPLACEAPI_URL + f'/sellers/listings/v3/{sku_id}'
        headers = {"Authorization": "Bearer" + token, "Content-Type": "application/json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return "Status code: " + response.status_code, "data: " + response.text

if __name__ == "__main__":
    # print(get_product_details_from_sku("IGO_123"))
    pass
