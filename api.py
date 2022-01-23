import pprint
from tronpy import Tron
import PySimpleGUI as sg
import time
from datetime import datetime

client = Tron()
adresse_cukies = "THESbAsrsX8JfRiYm7P1Kupcs1i7JaB1cM"
mon_adresse_tronlink = "TVLkepuiaDYesEHDVELBHTTCqnWFiVXsN3"
adresse_vote = "https://tronscan.io/#/sr/votes?from=tronlink"
adresse_tronlink_victor = "TQ3ATvXV91QUWk4zimTNQxQkgKmSv3AUT7"

def myTron():
    return client

def myAdress() -> tuple[str, str]:
    return (mon_adresse_tronlink, adresse_tronlink_victor, adresse_cukies)

"""
Simply save it with a .pyw extension. This will prevent the console window from opening.

On Windows systems, there is no notion of an “executable mode”.
The Python installer automatically associates .py files with python.exe so that
a double-click on a Python file will run it as a script. The extension can also be .pyw,
in that case, the console window that normally appears is suppressed.

"""
# Renvoie l'energie du compte
def getEnergy(ressource : dict) -> tuple[str, float, float, float]:

    # print("=======\n")
    # pprint.pprint(ressource)

    try:
        energy_used = ressource['EnergyUsed']
    except:
        energy_used = 0

    try:
        energy_limit = ressource['EnergyLimit']
    except:
        energy_limit = 0
    
    free_energy = energy_limit - energy_used
    if (free_energy < 0):
        free_energy = 0

    free_energy_in_thousands = round(free_energy/1000, 1)
    free_energy_in_millions = round(free_energy/1000000, 1)

    limit_energy_in_thousands = round(energy_limit/1000, 1)
    limit_energy_in_millions = round(energy_limit/1000000, 1)

    if (energy_limit != 0):
        pourcentage_energy = round(free_energy/energy_limit*100,1)
    else:
        pourcentage_energy = 0

    my_string = f"{free_energy} / {energy_limit}\n\n{free_energy_in_thousands}K / {limit_energy_in_thousands}K\n\n{free_energy_in_millions}M / {limit_energy_in_millions}M\n\n{pourcentage_energy}%"

    # print(my_string)

    return (my_string,free_energy,free_energy_in_thousands,free_energy_in_millions)

"""

montant = total-(NetUsed+freeNetUsed)
total = freeNetLimit+NetLimit

freeNetUsed	 : Free bandwidth used
freeNetLimit : Total free bandwidth

NetUsed	     : Used amount of bandwidth obtained by staking
NetLimit	 : Total bandwidth obtained by staking

lien : https://developers.tron.network/reference/getaccountresource

"""
# Renvoie la bandwidth du compte
def getBandwitdh(ressource : dict) -> tuple[str, float, float, float]:
    total_limit_bandwidth = ressource['freeNetLimit']+ressource['NetLimit']

    try:
        net_used = ressource['NetUsed']
    except:
        net_used = 0

    try:
        free_net_used = ressource['freeNetUsed']
    except:
        free_net_used = 0

    montant_bandwidth = total_limit_bandwidth-(net_used+free_net_used)

    pourcentage_bandwidth = round((montant_bandwidth/total_limit_bandwidth)*100, 1)
    my_string=f"{montant_bandwidth}/{total_limit_bandwidth}\n\n{pourcentage_bandwidth}%"

    # print(my_string)

    return (my_string,montant_bandwidth,total_limit_bandwidth,pourcentage_bandwidth)

# Renvoie le nombre de tronpower
def getTronpower(ressource : dict) -> tuple[str,int,int]:
    try:
        tron_power_used = ressource['tronPowerUsed']
    except:
        tron_power_used = 0

    try:
        tronPowerLimit = ressource['tronPowerLimit']
    except:
        tronPowerLimit = 0
    
    return (f"{tron_power_used}/{tronPowerLimit} Tronpower\n\nNon utilisé : {tronPowerLimit-tron_power_used}",tron_power_used, tronPowerLimit)

# Requete pour donner tronlink
def actualiser_donnees_tronlink(adresse_tronlink):
    global client
    # ============== TRONLINK
    ressource = client.get_account_resource(adresse_tronlink)
    # pprint.pprint(ressource)

    return getEnergy(ressource),getBandwitdh(ressource),getTronpower(ressource),client.get_account_balance(adresse_tronlink)

# Requete pour donner cukies
def actualiser_donnees_cukies():
    # ============== CUKIES
    ressource = client.get_account_resource(adresse_cukies)
    # pprint.pprint(ressource)

    return getEnergy(ressource)
