import webbrowser
import pprint
from datetime import datetime
from tronpy import Tron
import PySimpleGUI as sg
import time
import base58
import requests
import random
from playsound import playsound

# Mes fichiers
from api import *
from gui import principal

# Adresse vers les sites importants
adresse_vote = "https://tronscan.io/#/sr/votes?from=tronlink"
adresse_site_official = "https://www.cukies.world/"
adresse_dapp = "https://marketplace.cukies.world/dashboard"
adresse_token_goodies = "https://www.tokengoodies.com/"
adresse_whitepaper = "https://whitepaper.cukies.world/introduction/start-here"
adresse_contract_cukies = "https://tronscan.org/#/address/THESbAsrsX8JfRiYm7P1Kupcs1i7JaB1cM"
adresse_contract_stack_trx = "https://tronscan.io/#/wallet/resources?from=tronlink"

# MAIN
if __name__ == '__main__':
    # INITIALISATION
    client = myTron()
    mon_adresse_tronlink, adresse_tronlink_victor, adresse_cukies = myAdress()

    energy_infos_mon_tronlink,bandwitdh_infos_mon_tronlink,tronpower_infos_mon_tronlink,trx_unstake_mon_tronlink = actualiser_donnees_tronlink(mon_adresse_tronlink)
    energy_infos_tronlink_victor,bandwitdh_infos_tronlink_victor,tronpower_infos_tronlink_victor,trx_unstake_victor = actualiser_donnees_tronlink(adresse_tronlink_victor)
    energy_infos_cukies = actualiser_donnees_cukies()

    layout = principal(energy_infos_mon_tronlink,bandwitdh_infos_mon_tronlink,tronpower_infos_mon_tronlink,trx_unstake_mon_tronlink,
                        energy_infos_cukies,
                        energy_infos_tronlink_victor,bandwitdh_infos_tronlink_victor,tronpower_infos_tronlink_victor,trx_unstake_victor
                        )

    # Create the Window
    window = sg.Window('LuCrypto - Mon application TRON', layout, margins=(10,10), resizable=True, finalize=True)
    # Permet de centrer les elements au centre de la fenetre
    # element_justification='c'
    
    current_time = 0
    compteur = 0
    start_time = int(round(time.time() * 100))
    envoyer_son = False

    secondes = 1
    who_refresh = 0
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=1000*secondes)
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break

        # EVENEMENT BOUTON
        # =================================================================
        if (event == "--RAFRAICHIR--"):
            print("RAFRAICHIR MANUAL")
            # Mettre une protection pour ne pas spammer et freeze l'application
        elif (event == "--VOTE--"):
            webbrowser.open(adresse_vote)
            continue
        elif (event == "--TOKEN_GOODIES--"):
            webbrowser.open(adresse_token_goodies)
            continue
        elif (event == "--SITE_OFFICIAL--"):
            webbrowser.open(adresse_site_official)
            continue
        elif (event == "--DAPP--"):
            webbrowser.open(adresse_dapp)
            continue
        elif (event == "--WHITEPAPER--"):
            webbrowser.open(adresse_whitepaper)
            continue
        elif (event == "--CONTRACT_ENERGY--"):
            webbrowser.open(adresse_contract_cukies)
            continue
        elif (event == "--STACK_TRX--"):
            webbrowser.open(adresse_contract_stack_trx)
            continue
        print('You entered ', event)
        # =================================================================

        compteur += 1

        # Temps
        current_time = int(round(time.time() * 100)) - start_time
        window['text_temps'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                            (current_time // 100) % 60,
                                                            current_time % 100))

        # Rafraichir toutes les 10 secondes
        if (compteur % secondes == 0):
            print(f"RAFRAICHIR DONNEES : {compteur}")

            if (who_refresh == 0):
                who_refresh = 1
            else:
                who_refresh = 0

            # CUKIES
            if (who_refresh == 0):
                energy_infos_cukies = actualiser_donnees_cukies()
            # TRONLINK
            elif (who_refresh == 1):
                energy_infos_mon_tronlink,bandwitdh_infos_mon_tronlink,tronpower_infos_mon_tronlink,trx_unstake_mon_tronlink = actualiser_donnees_tronlink(mon_adresse_tronlink)

            # TEXTES
            # =================================================================
            # CUKIES
            window['text_cukies_energy'].update(energy_infos_cukies[0])
            # MON TRONLINK
            window['text_tronlink_energy'].update(energy_infos_mon_tronlink[0])
            window['text_tronlink_bandwidth'].update(bandwitdh_infos_mon_tronlink[0])
            window['text_tronlink_tronpower'].update(tronpower_infos_mon_tronlink[0])
            window['text_tronlink_trx'].update(trx_unstake_mon_tronlink)
            # VICTOR TRONLINK
            window['text_tronlink_energy_victor'].update(energy_infos_tronlink_victor[0])
            window['text_tronlink_bandwidth_victor'].update(bandwitdh_infos_tronlink_victor[0])
            window['text_tronlink_tronpower_victor'].update(tronpower_infos_tronlink_victor[0])
            window['text_tronlink_trx_victor'].update(trx_unstake_victor)

            # COULEURS
            # =================================================================
            # TRONLINK energie
            if (energy_infos_mon_tronlink[1] > 200_000):
                window['text_tronlink_energy'].update(background_color="green")
            elif (energy_infos_mon_tronlink[1] > 100_000):
                window['text_tronlink_energy'].update(background_color="orange")
            else:
                window['text_tronlink_energy'].update(background_color="red")
            
            # TRONLINK TRX unstake
            if (trx_unstake_mon_tronlink > 200):
                window['text_tronlink_trx'].update(background_color="green")
            elif (trx_unstake_mon_tronlink > 100):
                window['text_tronlink_trx'].update(background_color="orange")
            else:
                window['text_tronlink_trx'].update(background_color="red")
            
            # TRONLINK bandwidth
            if (bandwitdh_infos_mon_tronlink[1] > 1000):
                window['text_tronlink_bandwidth'].update(background_color="green")
            elif (bandwitdh_infos_mon_tronlink[1] > 500):
                window['text_tronlink_bandwidth'].update(background_color="orange")
            else:
                window['text_tronlink_bandwidth'].update(background_color="red")

            # TRONLINK TRON power
            if (tronpower_infos_mon_tronlink[2]-tronpower_infos_mon_tronlink[1] > 0):
                window['text_tronlink_tronpower'].update(background_color="red")
            else:
                window['text_tronlink_tronpower'].update(background_color="green")
            
            # CUKIES energie
            if (energy_infos_cukies[1] > 10_000_000):
                window['text_cukies_energy'].update(background_color="green")
            elif (energy_infos_cukies[1] > 2_000_000):
                window['text_cukies_energy'].update(background_color="orange")
            elif (energy_infos_cukies[1] > 1_000_000):
                window['text_cukies_energy'].update(background_color="orange red")
                if (not(envoyer_son)):
                    playsound("imperial-alertdeath-star-alarmclean.mp3")
                    envoyer_son = True
            else:
                window['text_cukies_energy'].update(background_color="red")



    # FIN BOUCLE PRINCIPALE
    window.close()
