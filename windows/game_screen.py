from venv import create
import PySimpleGUI as sg
from random import randrange
from scripts.gamescreen.scripts import *
from scripts.gamescreen.constant import *


def build(user, dificultad):
    """ Construyo la ventana de juego"""

    csv_selected, header, data = get_card_data()
    num_carta = randrange(len(data))  # obtengo carta a jugar aleatoriamente
    
    # Construccion de la ventana del juego
    sg.theme("LightBlue")
    
    # Columna izquierda resultado parcial
    col_left = create_col_result(csv_selected, user)
    col_right = create_right_col(header, data, dificultad, num_carta)

    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Column(col_left), sg.Push(), sg.Column(col_right), sg.Push()],
        [sg.VPush()]
    ]

    window = sg.Window("FiguRace *-* ¡A jugar!", layout, resizable=True, size=(800, 600), auto_size_buttons=True)
    img_act = []
    carta_buena = data[num_carta][5]
    while True:
        if len(img_act) != 10:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == '-VOLVER-':
                window.close()
            elif window[event].get_text() == carta_buena:
                window[f'-IMG_{len(img_act)+1}-'].update(PATH_CHECK_PNG)
                img_act.append(True)
                carta_buena = window_update(window, dificultad)
            else:
                window[f'-IMG_{len(img_act)+1}-'].update(PATH_NOTCHECK_PNG)
                img_act.append(False)
                carta_buena = window_update(window, dificultad)
        else:
            sg.popup("No puedes seguir jugando")
            window.close()
            break