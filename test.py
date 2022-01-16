import requests
import json
import pprint
from datetime import datetime

# https://github.com/iexbase/tron-api-python
# from tronapi import *

# https://tronpy.readthedocs.io/en/latest/quickstart.html
from tronpy import Tron

client = Tron()

ressource = client.get_account_resource("THESbAsrsX8JfRiYm7P1Kupcs1i7JaB1cM")

pprint.pprint(ressource)

# Lien : https://developers.tron.network/reference/testinput

# 255 362 841
# 230 464 897

# full_node = 'https://api.trongrid.io'
# solidity_node = 'https://api.trongrid.io'
# event_server = 'https://api.trongrid.io'

# tron = Tron(full_node=full_node,
#         solidity_node=solidity_node,
#         event_server=event_server)

# tron.default_block = 'latest'


# tron.getAccountResources("THESbAsrsX8JfRiYm7P1Kupcs1i7JaB1cM")

# print("result : ", tron.toHex(text="THESbAsrsX8JfRiYm7P1Kupcs1i7JaB1cM"))



# print("infos : ", tron.get_block('latest'))

# ma_cle_trongrid = "0c3185b7-6507-4405-9d01-620c5b276b8c"
# network = "https://api.trongrid.io"

# url = "https://api.trongrid.io/wallet/getaccountresource"

# payload = {
#     "address": "41BF97A54F4B829C4E9253B26024B1829E1A3B1120",
#     "visible": False
# }
# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json"
# }

# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)
# response_dict = json.loads(response.text)
# print("======\n")
# pprint.pprint(response_dict)

# bandwith : freeNetLimit


# url = "https://api.trongrid.io/v1/accounts/THESbAsrsX8JfRiYm7P1Kupcs1i7JaB1cM"

# headers = {"Accept": "application/json"}

# response = requests.request("GET", url, headers=headers)

# Permet de charger la string direct en dictionnaire
# response_dict = json.loads(response.text)

# pprint.pprint(response_dict)

# INFOS =================
# energy usage :
"""
Avant : 

web : 25 738 909
api : 229 622 285

Après : 

web : 25,858,635
api : 229 502 490

"""
# acquired from frozen energy : 8 250 000 000 000

# timestamp = 1642241049
# dt_object = datetime.fromtimestamp(timestamp)

# print("last consume of energy : ", dt_object)

if (False):
    url = "https://api.trongrid.io/wallet/getaccountresource"

    payload = {"address": "54484553624173727358384a665269596d3750314b757063733169374a614231634d"}

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print("ok : ", response.ok)
    print(response.text)

# Exemple pour Get transaction info by contract address 
if (False):
    url = "https://api.shasta.trongrid.io/v1/contracts/THESbAsrsX8JfRiYm7P1Kupcs1i7JaB1cM/transactions"

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers)

    print(response.text)

# Exemple pour créer une transaction
if (False):
    url = "https://api.trongrid.io/wallet/createtransaction"

    payload = "{\n    \"to_address\": \"41e9d79cc47518930bc322d9bf7cddd260a0260a8d\",   \
                \n    \"owner_address\": \"41D1E7A6BC354106CB410E65FF8B181C600FF14292\" \
                ,\n    \"amount\": 1000\n}"

    headers = {
        'Content-Type': "application/json",
        'TRON-PRO-API-KEY': "0c3185b7-6507-4405-9d01-620c5b276b8c"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)