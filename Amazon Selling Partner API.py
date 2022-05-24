import requests
import amazon_signer as sgn_algo


def product_details_from_sku(seller_partner_id, sku):
    access_token = get_amz_access_token(str(seller_partner_id))
    if access_token:
        url = f'/listings/2021-08-01/items/{seller_partner_id}/{sku}'
        r = sgn_algo.signed_get_request(access_token, url, 'marketplaceIds=A21TJRUUN4KGV')
        print(r)
        if r.status_code == 200:
            print(r.text)
