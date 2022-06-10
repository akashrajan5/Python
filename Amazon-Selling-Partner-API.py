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

def create_report(seller_id, report_type):
    access_token = get_amz_access_token(str(seller_id))
    if access_token:
        url = "/reports/2021-06-30/reports"
        body_para = {"reportType": str(report_type),"marketplaceIds": ["A21TJRUUN4KGV"]}
        r = sgn_algo.signed_post_request(access_token, url, json.dumps(body_para))
        if r.status_code == 202 or 200:
            return json.loads(r.text)
        else:
            return f"code - {r.status_code} : Create Reports api error"
    return "Invalid access token"

# recursive function please be careful
def get_report_doc_id(seller_id, reportId):
    access_token = get_amz_access_token(str(seller_id))
    if access_token:
        url = f"/reports/2021-06-30/reports/{reportId}"
        r = sgn_algo.signed_get_request(access_token, url, "")
        if r.status_code == 202 or 200:
            data = json.loads(r.text)
            print(data["processingStatus"])
            if data["processingStatus"] == "DONE":
                return data
            elif data["processingStatus"] == "CANCELLED":
                return "Report Cancelled"
            elif data["processingStatus"] == "FATAL":
                return "Report Fatal error"
            elif data["processingStatus"] == "IN_QUEUE" or data["processingStatus"] == "IN_PROGRESS":
                time.sleep(4) # wait before recursive call 
                return get_report_doc_id(seller_id, reportId)
        else:
            return f"code - {r.status_code} : Get reports document api error"

def get_report_document(seller_id, reportDocumentId):
    access_token = get_amz_access_token(seller_id)
    if access_token != 1:
        report_document_link = f"/reports/2021-06-30/documents/{reportDocumentId}"
        query_para = ""
        r = sgn_algo.signed_get_request(access_token, report_document_link, query_para)
        if r.status_code == 200 or 202:
            data = json.loads(r.text)
            if data["url"] != "":
                return data
        else:
            return -1
    else:
        return -1

def reports_to_dataframe_and_save(url): # -> also save data as excel and returns array of sku ids of a merchant
    response = requests.request("GET", url)
    data = response.text
    df = pd.read_csv(StringIO(data), sep='\t', header=[0])
    df.index += 1
    file_name = "amazon_reports_" + str(int(time.time())) + ".xlsx"
    json_data = df.to_json(orient="records")
    if len(json_data) < 3:
        return "No Reports"
    save_xls = df.to_excel("/home/azureuser/api/pflask/static/ecom/amazon_all_products_report/" + file_name)
    return json_data #-> dict inside list

# get amz product details from asin
def get_amazon_prod_details(pid, asin_id, save=False):
    seller_partner_id = get_amz_seller_id(pid)
    ecom_db = dbutil.get_ecom_db()
    access_token = get_amz_access_token(str(seller_partner_id))
    data = dict()
    if access_token != 1:
        catalogue_items_link = f"/catalog/v0/items/{str(asin_id)}"
        r = sgn_algo.signed_get_request(access_token, catalogue_items_link, 'MarketplaceId=A21TJRUUN4KGV')

        if r.status_code == 200:
            res = r.json()
            delivered_orders_count = get_delivered_orders_count(asin_id)
            
            data["asin"] = res["payload"]["Identifiers"]["MarketplaceASIN"]["ASIN"]
            data["name"] = res["payload"]["AttributeSets"][0]["Title"]
            data["brand"] = res["payload"]["AttributeSets"][0]["Brand"]
            data["price"] = res["payload"]["AttributeSets"][0]["ListPrice"]["Amount"]
            data["img_url"] = res["payload"]["AttributeSets"][0]["SmallImage"]["URL"]
            data["prod_group"] = res["payload"]["AttributeSets"][0]["ProductGroup"]
            data["prod_type"] = res["payload"]["AttributeSets"][0]["ProductTypeName"]
            data["delivered_orders_count"] = delivered_orders_count

            if save:
                insert = dbutil.insert_query(ecom_db, "insert into `amazon_product_details` (pid, asin, name, brand, price, img_url, prod_group, prod_type, full_json) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", [[pid, data["asin"], data["name"], data["brand"], data["price"], data["img_url"], data["prod_group"], data["prod_type"], json.dumps(data)]])
            return data, 200
        else:
            return json.loads(r.text), r.status_code
    else:
        return "Please check the Seller id", 400
