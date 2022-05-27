import stripe
import datetime
import json

STRIPE_API_KEY = "your stripe api key"

# create a customer
def create_customer(name, email):
    stripe.api_key = STRIPE_API_KEY
    customer = stripe.Customer.create(
        name = str(name),
        email = str(email)
    )
    return customer

# get customer details
def get_customer(customer_id):
    stripe.api_key = STRIPE_API_KEY
    customer = stripe.Customer.retrieve(str(customer_id))
    return customer

# remove a customer
def remove_customer(customer_id):
    stripe.api_key = STRIPE_API_KEY
    remove_customer = stripe.Customer.delete(str(customer_id))
    return remove_customer

# create acss payment
def create_acss_payment_intent(customer_id, total):
    stripe.api_key = STRIPE_API_KEY
    response = stripe.PaymentIntent.create(
        customer = str(customer_id),
        amount = total,
        currency = "cad",
        setup_future_usage = "off_session",
        payment_method_types = ["acss_debit"],
        payment_method_options = {
            "acss_debit": {
                "mandate_options": {
                    "payment_schedule": "interval",
                    "interval_description": "5 day interval", #TODO add as parameter
                    "transaction_type": "personal",
                },
            },
        },
    )
    print(response)
    return response

# create ach payment
def create_ach_payment_intent(customer_id, total):
    stripe.api_key = STRIPE_API_KEY
    response = stripe.PaymentIntent.create(
        customer = str(customer_id),
        amount = total,
        currency = "usd",
        setup_future_usage = "off_session",
        payment_method_types = ["us_bank_account"],
        payment_method_options = {
            "us_bank_account": {
                "financial_connections": {"permissions": ["payment_method"]},
            },
        },
    )
    print(response)
    return response

# reusing a payment method using authorized mandate
def confirm_acss_payment_intent(customer_id, amount, payment_method_id, mandate_id):
    stripe.api_key = STRIPE_API_KEY
    response = stripe.PaymentIntent.create(
        payment_method_types = ["acss_debit"],
        payment_method = str(payment_method_id),
        customer = str(customer_id),
        mandate = str(mandate_id),
        confirm = True,
        amount = amount,
        currency = "cad",
    )
    print(response)
    return response

# setup payment method and save bank details for future payment using setup intent for canadian bank
def create_acss_setup_intent(customer_id):
    stripe.api_key = STRIPE_API_KEY
    response = stripe.SetupIntent.create(
        payment_method_types = ["acss_debit"],
        customer = str(customer_id),
        payment_method_options = {
            "acss_debit": {
            "currency": "cad",
            "mandate_options": {
                "payment_schedule": "interval",
                "interval_description": "5 day interval",
                "transaction_type": "personal",
            },
            },
        },
    )
    print(response)
    return response

# cancel payment intent
def cancel_payment_intent(payment_intent_id):
    stripe.api_key = STRIPE_API_KEY
    response = stripe.PaymentIntent.cancel(
        str(payment_intent_id),
    )
    print(response)
    return response

# setup payment method and save bank details for future payment using setup intent for us bank
def create_ach_setup_intent(customer_id):
    stripe.api_key = STRIPE_API_KEY
    response = stripe.SetupIntent.create(
        customer = str(customer_id),
        payment_method_types = ["us_bank_account"],
        payment_method_options = {
            "us_bank_account": {
            "financial_connections": {"permissions": ["payment_method"]},
            },
        },
    )
    print(response)
    return response

