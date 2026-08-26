# Modules
import logging
import requests

# Functions and variables
from var import currency, lnbits_server, lnurl, price, ws_switch, x_api_key

url_base_switch = "https://" + lnbits_server + "/bitcoinswitch/api/v1"
url_base_payments = "https://" + lnbits_server + "/api/v1/payments"

def define_switch():
	params = 	{"title": switch_title,
  				"wallet": wallet_id,
  				"currency": currency,
  				"switches": [
    			{
      			"amount": price,
      			"duration": 1000,
      			"pin": 5,
      			"comment": True,
      			"variable": False,
      			"label": switch_title}
  				],
  				#"password": "",
  				"disabled": False,
  				"disposable": False
				}
	return params

def get_headers():
	global headers
	headers = {"X-Api-Key" : x_api_key, "Content-type" : "application/json"}
	return headers

def create_switch():
	new_switch = requests.post(url_base_switch, json=define_switch(), headers=get_headers())
	print(new_switch.json())

def get_payments():
	payments_request = requests.get(url_base_payments, headers=get_headers())
	payments = payments_request.json()
	amount = payments[0]['amount']/1000
	logging.info(f"Payment received: {amount} satoshi")
	return amount