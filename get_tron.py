from asyncio.windows_events import NULL
import json
import pprint
from datetime import datetime
from tronpy import Tron
import PySimpleGUI as sg
import time

"""
Simply save it with a .pyw extension. This will prevent the console window from opening.

On Windows systems, there is no notion of an “executable mode”.
The Python installer automatically associates .py files with python.exe so that
a double-click on a Python file will run it as a script. The extension can also be .pyw,
in that case, the console window that normally appears is suppressed.

"""

# Renvoie l'energie du compte
def getEnergy(ressource : dict) -> tuple[str, float, float, float]:
    free_energy = ressource['EnergyLimit'] - ressource['EnergyUsed']

    free_energy_in_thousands = round(free_energy/1000, 1)
    free_energy_in_millions = round(free_energy/1000000, 1)

    limit_energy_in_thousands = round(ressource['EnergyLimit']/1000, 1)
    limit_energy_in_millions = round(ressource['EnergyLimit']/1000000, 1)

    pourcentage_energy = round(free_energy/ressource['EnergyLimit']*100,1)

    my_string = f"{free_energy} / {ressource['EnergyLimit']}\n\n{free_energy_in_thousands}K / {limit_energy_in_thousands}K\n\n{free_energy_in_millions}M / {limit_energy_in_millions}M\n\n{pourcentage_energy}%"

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
    montant_bandwidth = total_limit_bandwidth-(ressource['NetUsed']+ressource['freeNetUsed'])
    pourcentage_bandwidth = round((montant_bandwidth/total_limit_bandwidth)*100, 1)

    my_string=f"{montant_bandwidth}/{total_limit_bandwidth}\n\n{pourcentage_bandwidth}%"

    # print(my_string)

    return (my_string,montant_bandwidth,total_limit_bandwidth,pourcentage_bandwidth)

# Requete pour donner tronlink
def actualiser_donnees_tronlink():
    # ============== TRONLINK
    ressource = client.get_account_resource(adresse_tronlink)
    # pprint.pprint(ressource)

    return getEnergy(ressource),getBandwitdh(ressource)

# Requete pour donner cukies
def actualiser_donnees_cukies():
    # ============== CUKIES
    ressource = client.get_account_resource(adresse_cukies)
    # pprint.pprint(ressource)

    return getEnergy(ressource)

# MAIN
if __name__ == '__main__':
    adresse_cukies = "THESbAsrsX8JfRiYm7P1Kupcs1i7JaB1cM"
    adresse_tronlink = "TVLkepuiaDYesEHDVELBHTTCqnWFiVXsN3"
    address_account = adresse_tronlink

    # INITIALISATION
    client = Tron()

    energy_infos_tronlink,bandwitdh_infos_tronlink = actualiser_donnees_tronlink()
    energy_infos_cukies = actualiser_donnees_cukies()

    # INFOS en tete : Premiere ligne
    haut = [ 
            sg.Text('', background_color="lightgrey", justification='center', size=(30,1), key='text_temps'),

            sg.Text('Energy', background_color="lightgrey", justification='center', size=(30,1)),
            sg.Text('Bandwidth', background_color="lightgrey", justification='center', size=(30,1))
        ]

    # CUKIES : Deuxieme ligne
    taille_y = 14
    cukies = [ 
            sg.Text('Cukies', background_color="violet", justification='center', size=(30,taille_y)),
            sg.Text(energy_infos_cukies[0], background_color="grey", justification='center', size=(30,taille_y), key="text_cukies_energy"),
            sg.Text('NA/NA Bandwidth', background_color="grey", justification='center', size=(30,taille_y))
        ]
    
    # TRONLINK : Troisieme ligne
    mon_tronlink = [ 
            sg.Text('Mon wallet Tronlink', background_color="lightblue", justification='center', size=(30,taille_y)),
            sg.Text(energy_infos_tronlink[0], background_color="grey", justification='center', size=(30,taille_y), key="text_tronlink_energy"),
            sg.Text(bandwitdh_infos_tronlink[0], background_color="grey", justification='center', size=(30,taille_y), key="text_tronlink_bandwidth")
        ]

    # All the stuff inside your window.
    layout = [  haut,
                cukies,
                mon_tronlink
            ]

    # Create the Window
    window = sg.Window('Mon application TRON', layout, margins=(10,10), resizable=True, finalize=True)
    
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
                energy_infos_tronlink,bandwitdh_infos_tronlink = actualiser_donnees_tronlink()

            # TEXTES
            window['text_cukies_energy'].update(energy_infos_cukies[0])
            window['text_tronlink_energy'].update(energy_infos_tronlink[0])
            window['text_tronlink_bandwidth'].update(bandwitdh_infos_tronlink[0])

            # COULEURS
            # TRONLINK energie
            if (energy_infos_tronlink[1] > 200000):
                window['text_tronlink_energy'].Update(background_color="green")
            elif (energy_infos_tronlink[1] > 100000):
                window['text_tronlink_energy'].Update(background_color="orange")
            else:
                window['text_tronlink_energy'].Update(background_color="red")
            
            # TRONLINK bandwidth
            if (bandwitdh_infos_tronlink[1] > 1000):
                window['text_tronlink_bandwidth'].Update(background_color="green")
            elif (bandwitdh_infos_tronlink[1] > 500):
                window['text_tronlink_bandwidth'].Update(background_color="orange")
            else:
                window['text_tronlink_bandwidth'].Update(background_color="red")
            
            # CUKIES energie
            if (energy_infos_cukies[1] > 10000000):
                window['text_cukies_energy'].Update(background_color="green")
            elif (energy_infos_cukies[1] > 2000000):
                window['text_cukies_energy'].Update(background_color="orange")
            elif (energy_infos_cukies[1] > 1000000):
                window['text_cukies_energy'].Update(background_color="orange red")
            else:
                window['text_cukies_energy'].Update(background_color="red")

            

        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        print('You entered ', event)

    window.close()

    """
    EXEMPLE 1 

    layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Demo", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()

    ===========================
    EXEMPLE 2

    # Add a touch of color
    # sg.theme('DarkAmber')

    # column_to_be_centered = [  [sg.Text('My Window')],
    #             [sg.Input(key='-IN-')],
    #             [sg.Text(size=(12,1), key='-OUT-')],
    #             [sg.Button('Go'), sg.Button('Exit')]  ]

    # layout = [[sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))],  # the thing that expands from top
    #           [sg.Text('', pad=(0,0),key='-EXPAND2-'),              # the thing that expands from left
    #            sg.Column(column_to_be_centered, vertical_alignment='center', justification='center',  k='-C-')]]

    # window = sg.Window('Window Title', layout, resizable=True,finalize=True)
    # window['-C-'].expand(True, True, True)
    # window['-EXPAND-'].expand(True, True, True)
    # window['-EXPAND2-'].expand(True, False, True)

    # while True:             # Event Loop
    #     event, values = window.read()
    #     print(event, values)
    #     if event == sg.WIN_CLOSED or event == 'Exit':
    #         break
    #     if event == 'Go':
    #         window['-OUT-'].update(values['-IN-'])
    # window.close()

    """
    

    



