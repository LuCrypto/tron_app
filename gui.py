import pprint
import re
from tronpy import Tron
import PySimpleGUI as sg
import time
from datetime import datetime
from api import *

def alignerTexteVertical(texte, background_color, font):
    result = [
        [sg.Text('',expand_x=True, expand_y=True, background_color=background_color)],
        [sg.Text(texte, expand_x=True, expand_y=True, background_color=background_color, justification='center', font=font)],
        [sg.Text('',expand_x=True, expand_y=True, background_color=background_color)]
    ]

    return sg.Column(result, expand_x=True, expand_y=True, vertical_alignment='center', justification='center', background_color=background_color)

def principal(energy_infos_tronlink,bandwitdh_infos_tronlink,tronpower_infos_tronlink,trx_unstake,energy_infos_cukies):
    # Couleurs
    if (tronpower_infos_tronlink[2]-tronpower_infos_tronlink[1] > 0):
        couleur_background_color_tronpower = 'red'
    else:
        couleur_background_color_tronpower = 'green'

    taille_titre = 12
    taille_case = 15

    # INFOS en tete : Premiere ligne
    haut = [ 
            sg.Text('', expand_x=True, expand_y=False, background_color="lightgrey", justification='center', font=f'ANY {taille_titre}', key='text_temps'),
            sg.Text('Energy', expand_x=True, expand_y=False, background_color='lightgrey', justification='center', font=f'ANY {taille_titre}'),
            sg.Text('Bandwidth', expand_x=True, expand_y=False, background_color='lightgrey', justification='center', font=f'ANY {taille_titre}'),
            sg.Text('Tronpower', expand_x=True, expand_y=False, background_color='lightgrey', justification='center', font=f'ANY {taille_titre}'),
            sg.Text('TRX', expand_x=True, expand_y=False, background_color='lightgrey', justification='center', font=f'ANY {taille_titre}')
        ]

    # CUKIES : Deuxieme ligne
    taille_y = 14
    cukies = [ 
            alignerTexteVertical('Cukies','violet',f'ANY {taille_case}'),
            # la string donnée est trop grande sur une seule ligne
            sg.Text(energy_infos_cukies[0], expand_x=True, expand_y=True, background_color="grey", justification='center', font=f'ANY {taille_case}', key="text_cukies_energy"),
            
            alignerTexteVertical('NA/NA Bandwidth','grey',f'ANY {taille_case}'),
            alignerTexteVertical('NA/NA Tronpower','grey',f'ANY {taille_case}'),
            alignerTexteVertical('NA/NA TRX','grey',f'ANY {taille_case}')
        ]

    # TRONLINK : Troisieme ligne
    mon_tronlink = [
            alignerTexteVertical('Mon wallet\nTronlink','lightblue',f'ANY {taille_case}'),
            sg.Text(energy_infos_tronlink[0], background_color="grey", justification='center', size=(taille_case,taille_y), key="text_tronlink_energy"),
            sg.Text(bandwitdh_infos_tronlink[0], background_color="grey", justification='center', size=(taille_case,taille_y), key="text_tronlink_bandwidth"),
            sg.Text(tronpower_infos_tronlink[0], background_color=couleur_background_color_tronpower, justification='center', size=(taille_case,taille_y), key="text_tronlink_tronpower"),
            sg.Text(f'{trx_unstake}/NA TRX', background_color="grey", justification='center', size=(taille_case,taille_y),key="text_tronlink_trx")
        ]
    
    # Emplacement pour les boutons : Quatrième ligne
    taille_y = 2
    mes_boutons = [
        sg.Text('Je suis un test', background_color="blue", justification='center', size=(12,taille_y))
    ]

    # Layout global
    layout = [  haut,
                cukies,
                mon_tronlink,
                mes_boutons
            ]
    
    return layout