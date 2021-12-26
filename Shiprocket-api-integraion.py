#shiprocket header + bearer token
def shiprocket_header():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {token here}'
    }
    return headers

#webhook sync + adding data to mysql
def shiprocket_sync(data):
    sr_order_id = data["order_id"]
    awb = data["awb"]
    current_status = data["current_status"]
    current_status_id = data["current_status_id"]
    shipment_status = data["shipment_status"]
    shipment_status_id = data["shipment_status_id"]
    current_timestamp = data["current_timestamp"]
    channel_order_id = data["channel_order_id"]
    channel = data["channel"]
    courier_name = data["courier_name"]
    etd = data["etd"]
    scans = data["scans"]
    training_db = dbutil.get_training_db()
    dbutil.insert_query(training_db, "insert into table_name (order_id, awb, current_status, current_status_id, shipment_status, shipment_status_id, curr_timestamp, channel_order_id, channel, courier_name, etd, scans, full_json) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [[sr_order_id, awb, current_status, current_status_id, shipment_status, shipment_status_id, current_timestamp, channel_order_id, channel, courier_name, etd, json.dumps(scans), json.dumps(data)]])


#create shiprocket order(only create order)
def create_simple_shiprocket_order(data):

    order_id = data["order_id"]
    order_date = data["order_date"]
    pickup_location = data["pickup_location"]
    billing_name = data["billing_name"]
    billing_last_name = data["billing_lname"]
    billing_address = data["billing_address_1"]
    billing_city = data["billing_city"]
    billing_pincode = data["billing_pincode"]
    billing_state = data["billing_state"]
    billing_country = data["billing_country"]
    billing_email = data["billing_email"]
    billing_phone = data["billing_phone"]
    shipping_is_billing = data["shipping_is_billing"]
    shipping_name = data["shipping_customer_name"]
    shipping_last_name = data["shipping_last_name"]
    shipping_address = data["shipping_address_1"]
    shipping_city = data["shipping_city"]
    shipping_pincode = data["shipping_pincode"]
    shipping_state = data["shipping_state"]
    shipping_country = data["shipping_country"]
    shipping_email = data["shipping_email"]
    shipping_phone = data["shipping_phone"]
    payment_method = data["payment_method"]
    discount = data["discount"]
    subtotal = data["subtotal"]
    weight = data["weight"]
    length = data["length"]
    breadth = data["breadth"]
    height = data["height"]
    shipping_charges = data["shipping_charges"]
    transaction_charges = data["transaction_charges"]
    order_items = data["order_items"]

    shiprocket_json = {
        "order_id": order_id,
        "order_date": order_date,
        "pickup_location": pickup_location,
        "channel_id": "",
        "billing_customer_name": billing_name,
        "billing_last_name": billing_last_name,
        "billing_address": billing_address,
        "billing_city": billing_city,
        "billing_pincode": billing_pincode,
        "billing_state": billing_state,
        "billing_country": billing_country,
        "billing_email": billing_email,
        "billing_phone": billing_phone,
        "shipping_is_billing": shipping_is_billing,
        "shipping_customer_name": shipping_name,
        "shipping_last_name" : shipping_last_name,
        "shipping_address": shipping_address,
        "shipping_city": shipping_city,
        "shipping_pincode": shipping_pincode,
        "shipping_country": shipping_country,
        "shipping_state": shipping_state,
        "shipping_email": shipping_email,
        "shipping_phone": shipping_phone,
        "payment_method": payment_method,
        "shipping_charges": shipping_charges,
        "transaction_charges": transaction_charges,
        "total_discount": discount,
        "sub_total": subtotal,
        "length": length,
        "breadth": breadth,
        "height": height,
        "weight": weight,
        "order_items": order_items
    }
    
    url = "https://apiv2.shiprocket.in/v1/external/orders/create/adhoc"
    header = shiprocket_header()
    response = requests.request("POST", url, headers=header, data = json.dumps(shiprocket_json)).json()
    if response.get("status_code") == 1:
        sr_order_id = response["order_id"]
        row_data = [pickup_location, sr_order_id, order_id, order_date, billing_name, billing_last_name, billing_address, billing_city, billing_pincode, billing_state, billing_country, billing_email, billing_phone, shipping_is_billing, shipping_name, shipping_last_name, shipping_address, shipping_city, shipping_pincode, shipping_state, shipping_country, shipping_email, shipping_phone, shipping_charges, payment_method, transaction_charges, discount, subtotal, length, breadth, height, weight, json.dumps(order_items), json.dumps(shiprocket_json), json.dumps(response)]
        training_db = dbutil.get_training_db()
        dbutil.insert_query(training_db, "insert into table_name (pickup_location, shiprocket_order_id, order_id, order_date, billing_name, billing_last_name, billing_address, billing_city, billing_pincode, billing_state, billing_country, billing_email, billing_phone, shipping_is_billing, shipping_name, shipping_last_name, shipping_address, shipping_city, shipping_pincode, shipping_state, shipping_country, shipping_email, shipping_phone, shipping_charges, payment_method, transaction_charges, discount, subtotal, length, breadth, height, weight, order_items, to_shiprocket_json, from_shiprocket_json) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [row_data])


#create pickup address
def create_pickup_address(data):

    shiprocket_address = json.dumps({
        "pickup_location": data["pickup_location"],
        "name": data["name"],
        "email": data["email"],
        "phone": data["phone"],
        "address": data["address"],
        "address_2": data["address_2"],
        "city": data["city"],
        "state":data["state"],
        "country": data["country"],
        "pin_code": data["pin_code"]
    })

    url = "https://apiv2.shiprocket.in/v1/external/settings/company/addpickup"
    header = shiprocket_header()
    response = requests.request("POST", url, headers=header , data=shiprocket_address).json()
    if response.get("success"):
        name = response["address"]["name"]
        address_1 = response["address"]["address"]
        address_2 = response["address"]["address_2"]
        phone = response["address"]["phone"]
        email = response["address"]["email"]
        pid = 256
        door_no = "-"
        pickup_location = response["address"]["pickup_code"]
        ecom_db = dbutil.get_ecom_db()
        create = dbutil.insert_query(ecom_db, "insert into warehouse (name, address_1, address_2, phone_no, email, door_no, pid, pickup_location) values (%s, %s, %s, %s, %s, %s, %s, %s)", [[name, address_1, address_2, phone, email, door_no, pid, pickup_location]])
        return response.get("success") , response["address"]["pickup_code"]
    else:
        return response["message"], response["errors"]


#cancel shiprocket order , not working properly
def cancel_order():
    url = "https://apiv2.shiprocket.in/v1/external/orders/cancel"

    payload = json.dumps({
    "ids": [
        224-447
        ]
    })
    headers = shiprocket_header()
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())

#get all shiprocket orders
def get_all_orders():
    url = "https://apiv2.shiprocket.in/v1/external/orders"
    payload={}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+ str(auth_token)
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.json())


#create, ship, generate label & manifiest for orders
def create_ship_generate_shiprocket_order(data, woo_url, orderid):

    ecom_db = dbutil.get_ecom_db()
    result = dbutil.select_query(ecom_db, "SELECT * FROM `all_woo_lines` WHERE `store_url` LIKE %s AND `orderid` = %s", [woo_url, orderid])
    prod = []
    for i in range(len(result)):
        prod.append({
            "name": result[i]["name"],
            "sku": result[i]["sku"],
            "units": result[i]["quantity"],
            "selling_price": result[i]["total"]
            })

    order_id = data["order_id"]#woo orderid
    order_date = data["order_date"]
    channel_id = data["channel_id"]
    billing_customer_name = data["billing_customer_name"]
    billing_last_name = data["billing_last_name"]
    billing_address = data["billing_address"]
    billing_city = data["billing_city"]
    billing_pincode = data["billing_pincode"]
    billing_state = data["billing_state"]
    billing_country = data["billing_country"]
    billing_email = data["billing_email"]
    billing_phone = data["billing_phone"]
    shipping_is_billing = data["shipping_is_billing"]
    payment_method = data["payment_method"]
    shipping_charges = data["shipping_charges"]
    sub_total = data["sub_total"]
    discount = data["total_discount"]
    length = data["length"]
    breadth = data["breadth"]
    height = data["height"]
    weight = data["weight"]
    pickup_location = data["pickup_location"]
    order_items = prod

    shiprocket_json = json.dumps({
        "order_id": order_id,
        "order_date": order_date,
        "channel_id": channel_id,
        "billing_customer_name": billing_customer_name,
        "billing_last_name": billing_last_name,
        "billing_address": billing_address,
        "billing_city": billing_city,
        "billing_pincode": billing_pincode,
        "billing_state": billing_state,
        "billing_country": billing_country,
        "billing_email": billing_email,
        "billing_phone": billing_phone,
        "shipping_is_billing": shipping_is_billing,
        "order_items": order_items,
        "payment_method": payment_method,
        "shipping_charges" : shipping_charges,
        "sub_total": sub_total,
        "total_discount" : discount,
        "length": length,
        "breadth": breadth,
        "height": height,
        "weight": weight,
        "pickup_location": pickup_location
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+ str(auth_token)
    }
    url = "https://apiv2.shiprocket.in/v1/external/shipments/create/forward-shipment"
    response = requests.request("POST", url, headers=headers, data=shiprocket_json).json()
    if response.get("status") == 1:
        sr_order_id = response["payload"]["order_id"]
        label_url = response["payload"]["label_url"]
        manifest_url = response["payload"]["manifest_url"]
        routing_code = response["payload"]["routing_code"]
        pickup_token_number = response["payload"]["pickup_token_number"]
        row_data = [pickup_location, sr_order_id, order_id, order_date, billing_customer_name, billing_last_name, billing_address, billing_city, billing_pincode, billing_state, billing_country, billing_email, billing_phone, shipping_is_billing, shipping_charges, payment_method, discount, sub_total, length, breadth, height, weight, json.dumps(order_items), label_url, manifest_url, routing_code, pickup_token_number, shiprocket_json, json.dumps(response)]
        training_db = dbutil.get_training_db()
        dbutil.insert_query(training_db, "insert into shiprocket_order_details (pickup_location, shiprocket_order_id, order_id, order_date, billing_name, billing_last_name, billing_address, billing_city, billing_pincode, billing_state, billing_country, billing_email, billing_phone, shipping_is_billing,  shipping_charges, payment_method, discount, subtotal, length, breadth, height, weight, order_items, label_url, manifest_url, routing_code, pickup_token_number, to_shiprocket_json, from_shiprocket_json) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [row_data])
        print(response)

    return label_url, manifest_url, pickup_token_number