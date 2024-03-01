import requests
import json
import pprint
from datetime import datetime
import base58
import random

# https://github.com/iexbase/tron-api-python
# from tronapi import *

# https://tronpy.readthedocs.io/en/latest/quickstart.html
from tronpy import Tron

CONF_MAINNET = {
    "fullnode": "https://api.trongrid.io",
    "event": "https://api.trongrid.io",
}

# The long running, maintained by the tron-us community
CONF_SHASTA = {
    "fullnode": "https://api.shasta.trongrid.io",
    "event": "https://api.shasta.trongrid.io",
    "faucet": "https://www.trongrid.io/faucet",
}

# Maintained by the official team
CONF_NILE = {
    "fullnode": "https://api.nileex.io",
    "event": "https://event.nileex.io",
    "faucet": "http://nileex.io/join/getJoinPage",
}

# Maintained by the official team
CONF_TRONEX = {
    "fullnode": "https://testhttpapi.tronex.io",
    "event": "https://testapi.tronex.io",
    "faucet": "http://testnet.tronex.io/join/getJoinPage",
}

ALL = {
    "mainnet": CONF_MAINNET,
    "nile": CONF_NILE,
    "shasta": CONF_SHASTA,
    "tronex": CONF_TRONEX,
}

DEFAULT_CONF = {
    'fee_limit': 10_000_000,
    'timeout': 10.0,  # in second
}

def conf_for_name(name: str) -> dict:
    return ALL.get(name, None)

DEFAULT_API_KEYS = [
    'f92221d5-7056-4366-b96f-65d3662ec2d9',
    '1e0a625f-cfa5-43ee-ba41-a09db1aae55f',
    'f399168e-2259-481c-90fc-6b3d984c5463',
    'da63253b-aa9c-46e7-a4e8-22d259a8026d',
    '88c10958-af7b-4d5a-8eef-6e84bf5fb809',
    '169bb4b3-cbe8-449a-984e-80e9adacac55',
]

# Choisir une clé de facon aléatoire
def random_api_key(parametre):
    return random.choice(parametre)

# Renvoie un tuple contenant la difference de temps en
# datetime ainsi que chaine de caractere recap
def diff_date(date_debut : datetime, date_fin : datetime) -> 'tuple[datetime, str]':
    difference = date_fin-date_debut

    en_minutes = round(difference.total_seconds() / 60, 2)
    en_heures = round(en_minutes / 60, 2)
    en_jours = round(en_heures / 24, 2)

    string_result = "{} jours => {} heures => {} minutes".format(en_jours,en_heures,en_minutes)

    return difference,string_result

# MAIN
if __name__ == '__main__':
    
    # Partie réseau - requete API
    client = Tron()

    ressource = client.get_account_resource("THESbAsrsX8JfRiYm7P1Kupcs1i7JaB1cM")

    pprint.pprint(ressource)

    adresse_cukies = "THESbAsrsX8JfRiYm7P1Kupcs1i7JaB1cM"
    adresse_tronlink = "TVLkepuiaDYesEHDVELBHTTCqnWFiVXsN3"
    adresse_vote = "https://tronscan.io/#/sr/votes?from=tronlink"

    client = Tron()

    adresse_cukies_base58 = base58.b58decode_check(adresse_cukies).hex()
    adresse_tronlink_base58 = base58.b58decode_check(adresse_tronlink).hex()

    print("adresse_cukies_base58 ! ", adresse_cukies_base58)
    print("adresse_tronlink_base58 : ", adresse_tronlink_base58)

    # https://api.trongrid.io/wallet/triggerconstantcontract

    """
    
    A tester : 

    {
        "contract_address": "41d8f6798aff04da7fcdab930291cd1f7bb0696fdf",
        "owner_address": "41d47d8bd0d26d2f0710581103c01cda66e6c1730c",
        "function_selector": "totalSupply()",
        "parameter": ""
    }

    """

    exit(1)

    # ZONE DE TEST
    # print("Debut")

    mes_cles_api = DEFAULT_API_KEYS.copy()

    mon_provider = requests.session()
    mon_provider.headers["User-Agent"] = "Tronpy/0.2"
    mon_provider.headers["Tron-Pro-Api-Key"] = random_api_key(mes_cles_api)

    url = "https://api.trongrid.io/wallet/triggersmartcontract "
    params = {'contract_address': adresse_cukies_base58,
                'function_selector': "name()",
                'owner_address' : adresse_tronlink_base58
                }
    resp = mon_provider.post(url, json=params, timeout=10)
    # print("resp ", resp)
    print("header : ", resp.headers)

    """

    adresse_cukies_base58 !  414faa7674e50271a075a07097112d993662f634d3
    adresse_tronlink_base58 :  41d47d8bd0d26d2f0710581103c01cda66e6c1730c

    curl.exe -X POST https://api.trongrid.io/wallet/triggersmartcontract -d '{
            "contract_address":"THESbAsrsX8JfRiYm7P1Kupcs1i7JaB1cM",
            "function_selector":"name()",
            "owner_address":"TVLkepuiaDYesEHDVELBHTTCqnWFiVXsN3"
    }'

    curl.exe -X POST https://api.trongrid.io/wallet/triggersmartcontract -d '{
            "contract_address":"414faa7674e50271a075a07097112d993662f634d3",
            "function_selector":"name()",
            "owner_address":"41d47d8bd0d26d2f0710581103c01cda66e6c1730c"
    }'

        """

    # resp = resp.json()
    # pprint.pprint(resp)

    # GET ACCOUNT
    # url = "https://api.trongrid.io/wallet/getaccount"
    # params = {'address': 'TVLkepuiaDYesEHDVELBHTTCqnWFiVXsN3', 'visible': True}
    # resp = mon_provider.post(url, json=params, timeout=10)
    # resp = resp.json()
    # pprint.pprint(resp)

    # print("adresse normale : ", adresse_tronlink)
    # print("adresse base58 : ", adresse_tronlink_base58)
    # print("adresse hex : ", adresse_tronlink_base58.hex())