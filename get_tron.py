import pprint
from tronpy import Tron
import PySimpleGUI as sg
import time
from datetime import datetime
from api import *
from gui import principal

# MAIN
if __name__ == '__main__':
    # INITIALISATION
    client = myTron()
    adresse_tronlink, adresse_cukies = myAdress()

    # ZONE DE TEST
    print("Debut")
    
    # ressource = client.get_account_asset_balance()
    # ressource = client.get_account(adresse_tronlink)
    # pprint.pprint(ressource)

    # print("=====")
    # print("=====")
    # print("=====")

    # infos = ressource.get('account_resource', 0).get('frozen_balance_for_energy', 0)
    # print("infos : ", infos.get('frozen_balance',0))
    # temps = infos.get('expire_time',0)
    # print("infos temps : ", temps)
    # print("infos temps : ", type(temps))
    # # temps = datetime.timestamp(temps)
    # # print("infos temps : ", temps)
    # print("infos temps converti : ", datetime.fromtimestamp(1642338888))

    # exit(1)

    energy_infos_tronlink,bandwitdh_infos_tronlink,tronpower_infos_tronlink,trx_unstake = actualiser_donnees_tronlink()
    energy_infos_cukies = actualiser_donnees_cukies()

    layout = principal(energy_infos_tronlink,bandwitdh_infos_tronlink,tronpower_infos_tronlink,trx_unstake,energy_infos_cukies)

    # Create the Window
    window = sg.Window('LuCrypto - Mon application TRON', layout, margins=(10,10), resizable=True, finalize=True)
    # Permet de centrer les elements au centre de la fenetre
    # element_justification='c'
    
    current_time = 0
    compteur = 0
    start_time = int(round(time.time() * 100))

    secondes = 1
    who_refresh = 0
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=1000)

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
                energy_infos_tronlink,bandwitdh_infos_tronlink,tronpower_infos_tronlink,trx_unstake = actualiser_donnees_tronlink()

            # TEXTES
            # =================================================================
            window['text_cukies_energy'].update(energy_infos_cukies[0])
            window['text_tronlink_energy'].update(energy_infos_tronlink[0])
            window['text_tronlink_bandwidth'].update(bandwitdh_infos_tronlink[0])
            window['text_tronlink_tronpower'].update(tronpower_infos_tronlink[0])
            window['text_tronlink_trx'].update(trx_unstake)

            # COULEURS
            # =================================================================
            # TRONLINK energie
            if (energy_infos_tronlink[1] > 200_000):
                window['text_tronlink_energy'].update(background_color="green")
            elif (energy_infos_tronlink[1] > 100_000):
                window['text_tronlink_energy'].update(background_color="orange")
            else:
                window['text_tronlink_energy'].update(background_color="red")
            
            # TRONLINK TRX unstake
            if (trx_unstake > 200):
                window['text_tronlink_trx'].update(background_color="green")
            elif (trx_unstake > 100):
                window['text_tronlink_trx'].update(background_color="orange")
            else:
                window['text_tronlink_trx'].update(background_color="red")
            
            # TRONLINK bandwidth
            if (bandwitdh_infos_tronlink[1] > 1000):
                window['text_tronlink_bandwidth'].update(background_color="green")
            elif (bandwitdh_infos_tronlink[1] > 500):
                window['text_tronlink_bandwidth'].update(background_color="orange")
            else:
                window['text_tronlink_bandwidth'].update(background_color="red")

            # TRONLINK TRON power
            if (tronpower_infos_tronlink[2]-tronpower_infos_tronlink[1] > 0):
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
            else:
                window['text_cukies_energy'].update(background_color="red")


        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        print('You entered ', event)

    # FIN BOUCLE PRINCIPALE
    window.close()
