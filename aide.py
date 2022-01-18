import pprint
from tronpy import Tron
import PySimpleGUI as sg
import time

adresse_tronlink="TVLkepuiaDYesEHDVELBHTTCqnWFiVXsN3"

client = Tron()

ressource = client.get_account_resource(adresse_tronlink)
{'EnergyLimit': 243968,
 'EnergyUsed': 156598,
 'NetLimit': 2023,
 'NetUsed': 1896,
 'TotalEnergyLimit': 90000000000,
 'TotalEnergyWeight': 2914309879,
 'TotalNetLimit': 43200000000,
 'TotalNetWeight': 24380233698,
 'freeNetLimit': 1500,
 'freeNetUsed': 241,
 'tronPowerLimit': 9042,
 'tronPowerUsed': 9042}

ressource = client.get_account(adresse_tronlink)
{'account_resource': {'energy_usage': 156389,
                      'frozen_balance_for_energy': {'expire_time': 1642338888000,
                                                    'frozen_balance': 7900000000},
                      'latest_consume_time_for_energy': 1642452465000},
 'active_permission': [{'id': 2,
                        'keys': [{'address': 'TVLkepuiaDYesEHDVELBHTTCqnWFiVXsN3',
                                  'weight': 1}],
                        'operations': '7fff1fc0033e0300000000000000000000000000000000000000000000000000',
                        'permission_name': 'active',
                        'threshold': 1,
                        'type': 'Active'}],
 'address': 'TVLkepuiaDYesEHDVELBHTTCqnWFiVXsN3',
 'balance': 154632662,
 'create_time': 1637370972000,
 'free_net_usage': 240,
 'frozen': [{'expire_time': 1642595547000, 'frozen_balance': 1142000000}],
 'latest_consume_free_time': 1642454265000,
 'latest_consume_time': 1642454208000,
 'latest_opration_time': 1642454265000,
 'latest_withdraw_time': 1642454265000,
 'net_usage': 1894,
 'owner_permission': {'keys': [{'address': 'TVLkepuiaDYesEHDVELBHTTCqnWFiVXsN3',
                                'weight': 1}],
                      'permission_name': 'owner',
                      'threshold': 1},
 'votes': [{'vote_address': 'TJBtdYunmQkeK5KninwgcjuK1RPDhyUWBZ',
            'vote_count': 9042}]}

ressource = client.get_account_balance(adresse_tronlink)

# Decimal('154.632662')


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
    

    