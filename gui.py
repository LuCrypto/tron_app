import pprint
import re
from tronpy import Tron
import PySimpleGUI as sg
import time
from datetime import datetime
from api import *

NOMBRE_BABY_LOADING = 3
date_bebe_1 = datetime(2022, 1, 24, 13, 18, 3)
date_bebe_2 = datetime(2022, 1, 24, 17, 28, 39)
date_bebe_3 = datetime(2022, 1, 24, 23, 55, 30)

def alignerTexteVertical(texte, background_color, font, key=None):
    result = [
        [sg.Text('',expand_x=True, expand_y=True, background_color=background_color)],
        [sg.Text(texte, expand_x=True, expand_y=True, background_color=background_color, justification='center', font=font, key=key)],
        [sg.Text('',expand_x=True, expand_y=True, background_color=background_color)]
    ]

    return sg.Column(result, expand_x=True, expand_y=True, vertical_alignment='center', justification='center', background_color=background_color)

# Renvoie un tuple contenant la difference de temps en
# datetime ainsi que chaine de caractere recap
def diff_date(date_debut : datetime, date_fin : datetime) -> tuple[datetime, str]:
    difference = date_fin-date_debut

    en_minutes = round(difference.total_seconds() / 60, 2)
    en_heures = round(en_minutes / 60, 2)
    en_jours = round(en_heures / 24, 2)

    string_result = "{} jours => {} heures => {} minutes".format(en_jours,en_heures,en_minutes)

    return difference,string_result

def principal(energy_infos_mon_tronlink,bandwitdh_infos_mon_tronlink,tronpower_infos_mon_tronlink,trx_unstake_mon_tronlink,energy_infos_cukies
            ,energy_infos_tronlink_victor,bandwitdh_infos_tronlink_victor,tronpower_infos_tronlink_victor,trx_unstake_victor):
    # Initialisation
    taille_titre = 12
    taille_case = 15
    taille_button = 12

    haut = []
    milieu = []
    bas = []

    # Couleurs
    if (tronpower_infos_mon_tronlink[2]-tronpower_infos_mon_tronlink[1] > 0):
        couleur_background_color_tronpower = 'red'
    else:
        couleur_background_color_tronpower = 'green'
    
    # =================================================================

    # INFOS en tete : Premiere ligne
    infos = [ 
            sg.Text('', expand_x=True, expand_y=False,
            background_color="lightgrey", justification='center', font=f'ANY {taille_titre}', key='text_temps'),

            sg.Text('Energy', expand_x=True, expand_y=False,
            background_color='lightgrey', justification='center', font=f'ANY {taille_titre}'),

            sg.Text('Bandwidth', expand_x=True, expand_y=False,
            background_color='lightgrey', justification='center', font=f'ANY {taille_titre}'),

            sg.Text('Tronpower', expand_x=True, expand_y=False,
            background_color='lightgrey', justification='center', font=f'ANY {taille_titre}'),

            sg.Text('TRX', expand_x=True, expand_y=False,
            background_color='lightgrey', justification='center', font=f'ANY {taille_titre}'),

            sg.Text('AUTRES', expand_x=True, expand_y=False,
            background_color='lightgrey', justification='center', font=f'ANY {taille_titre}')
        ]

    # =================================================================

    # CUKIES : Deuxieme ligne
    cukies = [ 
            alignerTexteVertical('Cukies','violet',f'ANY {taille_case}'),

            # La string donnée est trop grande sur une seule ligne
            sg.Text(energy_infos_cukies[0], expand_x=True, expand_y=True,
            background_color="grey", justification='center', font=f'ANY {taille_case}', key="text_cukies_energy"),
            
            alignerTexteVertical('NA/NA Bandwidth','grey',f'ANY {taille_case}'),

            alignerTexteVertical('NA/NA Tronpower','grey',f'ANY {taille_case}'),

            alignerTexteVertical('NA/NA TRX','grey',f'ANY {taille_case}'),

            alignerTexteVertical('Premier play2earn\nsur le réseau TRON','grey',f'ANY {taille_case}')
        ]

    # =================================================================

    # STRING 
    now = datetime.now()

    current_time = f"{now.day}/{now.month} {now.hour}:{now.minute}:{now.second}"

    restant_1 = diff_date(now, date_bebe_1)[1]
    restant_2 = diff_date(now, date_bebe_2)[1]
    restant_3 = diff_date(now, date_bebe_3)[1]
    
    string_11 = f"Date actuelle : {current_time}\n"
    string_1 = f"Nombre de bébés en attente : {NOMBRE_BABY_LOADING}\n\n"
    string_2 = f"Première date : {date_bebe_1}\n"
    string_22 = f"Restant 1 : {restant_1}\n\n"
    string_3 = f"Deuxième date : {date_bebe_2}\n"
    string_33 = f"Restant 2 : {restant_2}\n\n"
    string_4 = f"Troisième date : {date_bebe_3}\n"
    string_44 = f"Restant 3 : {restant_3}\n"

    string_autre_mon_tronlink =string_11+ string_1+string_2+string_22+string_3+string_33+string_4+string_44

    # MON TRONLINK : Troisieme ligne
    mon_tronlink = [
            alignerTexteVertical('Mon wallet\nTronlink','lightblue',f'ANY {taille_case}'),

            sg.Text(energy_infos_mon_tronlink[0], expand_x=True, expand_y=True,
             background_color="grey", justification='center', font=f'ANY {taille_case}', key="text_tronlink_energy"),

            sg.Text(bandwitdh_infos_mon_tronlink[0], expand_x=True, expand_y=True,
             background_color="grey", justification='center', font=f'ANY {taille_case}', key="text_tronlink_bandwidth"),

            sg.Text(tronpower_infos_mon_tronlink[0], expand_x=True, expand_y=True,
             background_color=couleur_background_color_tronpower, justification='center', font=f'ANY {taille_case}', key="text_tronlink_tronpower"),

            sg.Text(f'{trx_unstake_mon_tronlink}/NA TRX', expand_x=True, expand_y=True,
             background_color="grey", justification='center', font=f'ANY {taille_case}',key="text_tronlink_trx"),

            sg.Text(string_autre_mon_tronlink, expand_x=True, expand_y=True,
             background_color="grey", justification='left', font=f'ANY {taille_case}',key="text_tronlink_autre")
        ]

    # =================================================================

    # VICTOR TRONLINK : Quatrieme ligne
    tronlink_victor = [
            alignerTexteVertical('Victor\nTronlink','PaleGreen1',f'ANY {taille_case}'),

            sg.Text(energy_infos_tronlink_victor[0], expand_x=True, expand_y=True,
             background_color="grey", justification='center', font=f'ANY {taille_case}', key="text_tronlink_energy_victor"),

            sg.Text(bandwitdh_infos_tronlink_victor[0], expand_x=True, expand_y=True,
             background_color="grey", justification='center', font=f'ANY {taille_case}', key="text_tronlink_bandwidth_victor"),

            sg.Text(tronpower_infos_tronlink_victor[0], expand_x=True, expand_y=True,
             background_color=couleur_background_color_tronpower, justification='center', font=f'ANY {taille_case}', key="text_tronlink_tronpower_victor"),

            sg.Text(f'{trx_unstake_victor}/NA TRX', expand_x=True, expand_y=True,
             background_color="grey", justification='center', font=f'ANY {taille_case}',key="text_tronlink_trx_victor"),

            sg.Text("Mon bro Victor", expand_x=True, expand_y=True,
             background_color="grey", justification='left', font=f'ANY {taille_case}',key="text_tronlink_autre_victor")
        ]
        
    # =================================================================
    
    # Emplacement pour les boutons : Quatrième ligne
    mes_boutons = [
        sg.Button('REFRESH',font=f'ANY {taille_button}', button_color="purple", key="--RAFRAICHIR--"),
        sg.Button('VOTE', font=f'ANY {taille_button}', key="--VOTE--"),
        sg.Button('TOKEN_GOODIES', font=f'ANY {taille_button}', key="--TOKEN_GOODIES--"),
        sg.Button('SITE_OFFICIAL', font=f'ANY {taille_button}', key="--SITE_OFFICIAL--"),
        sg.Button('DAPP', font=f'ANY {taille_button}', key="--DAPP--"),
        sg.Button('WHITEPAPER', font=f'ANY {taille_button}', key="--WHITEPAPER--"),
        sg.Button('CONTRACT_ENERGY', font=f'ANY {taille_button}', key="--CONTRACT_ENERGY--"),
        sg.Button('STACK_TRX', font=f'ANY {taille_button}', key="--STACK_TRX--")
    ]

    # =================================================================
    haut.append(infos)
    milieu.append(cukies)
    milieu.append(mon_tronlink)
    milieu.append(tronlink_victor)
    bas.append(mes_boutons)

    layout = []
    for i in haut:
        layout.append(i)
    for i in milieu:
        layout.append(i)
    for i in bas:
        layout.append(i)

    # mon_image = [sg.Image("images/breaading_cukies.png")]

    # layout.append(mon_image)

    # Layout global
    # layout = [  haut,
    #             cukies,
    #             mon_tronlink,
    #             mes_boutons
    #         ]
    
    return layout