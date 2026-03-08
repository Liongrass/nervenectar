# Modules
import logging
import requests

# Functions and variables
from var import acl_api_token, currency, lnbits_server, lnbits_wallet, lnurl, price, switch_title, ws_switch, x_api_key

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
	if web_setup == True:
		headers = {"X-Api-Key" : x_api_key, "Content-type" : "application/json"}
	else:
		headers = {'accept' : 'application/json', 'Authorization' : f'Bearer {acl_api_token}'}
	return headers

def get_setup_method():
	global web_setup
	try:
		x_api_key
	except IndexError:
		logging.debug("LNbits invoice key not found.")
		logging.info("Continuing by setting up Bitcoin Switch Extension")
		web_setup = False
		#get_switches()
		#get_lnurl()
	else:
		logging.debug("LNbits invoice key found.")
		logging.info("Not setting up anything.")
		web_setup = True

def get_switches():
	print(url_base_switch)
	print(headers)
	switches_request = requests.get(url_base_switch, headers=get_headers())
	global switches
	switches = switches_request.json()
	logging.debug(switches) 
	if ['title'] == switch_title in switches:
		logging.debug(f"Switch found. Continuing")
	else:
		logging.debug(f"No switch found. Creating switch.")
		create_switch()

def create_switch():
	new_switch = requests.post(url_base_switch, json=define_switch(), headers=get_headers())
	print(new_switch.json())

'''
def get_lnurl():
	print(url_base_switch)
	print(headers)
	#params = {"pin": 5}
	url = url_base_switch + "/" + "WB4kjkTtQRVWdSL7FeV6b3"
	lnurl_request = requests.get(url, headers=get_headers())
	lnurl = lnurl_request.json()
	print(lnurl)
	print("WOHOO")
'''

def get_payments():
	payments_request = requests.get(url_base_payments, headers=get_headers())
	payments = payments_request.json()
	amount = payments[0]['amount']/1000
	logging.info(f"Payment received: {amount} satoshi")
	return amount

#https://send.laisee.org/bitcoinswitch/api/v1/lnurl/{bitcoinswitch_id}
#https://send.laisee.org/bitcoinswitch/api/v1/public/{bitcoinswitch_id}

'''
1. Get list of Bitcoin Switches
2. Check if switch already exists (identified by name)
3. Register switch
4. Update switch
5. Retrieve LNURL
6. Listen to websockets
'''