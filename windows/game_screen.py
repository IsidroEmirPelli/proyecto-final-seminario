from venv import create
import PySimpleGUI as sg
from random import randrange
from scripts.gamescreen.scripts import *
from scripts.gamescreen.constant import *
from time import time


def build(user, dificultad):
    """ Construyo la ventana de juego"""

    config = get_config()
    csv_selected, header, data = get_card_data()
    num_carta = randrange(len(data))  # obtengo carta a jugar aleatoriamente
    puntaje = 0

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

    window = sg.Window("FiguRace *-* ¡A jugar!", layout, resizable=True, size=(700, 640), auto_size_buttons=True)
    img_act = []
    carta_buena = data[num_carta][5]
    start_time = time()
    time_y_punt = [start_time, puntaje]

    while True:
        if len(img_act) != config['Rondas']:
            event, values = window.read(timeout=250, timeout_key='-TIMEOUT-')
            if event == sg.WIN_CLOSED:
                break
            elif event == '-VOLVER-':
                window.close()

            # countdown
            elif event == '-TIMEOUT-':
                countdown(window, time_y_punt, config, data, dificultad, img_act)
            else:
                if window[event].get_text() == carta_buena:
                    window[f'-IMG_{len(img_act) + 1}-'].update(PATH_CHECK_PNG)
                    img_act.append(True)
                    time_y_punt[1] += config['Puntaje_sumar']
                    carta_buena = data[window_update(window, dificultad)][5]
                    time_y_punt[0] = time()
                else:  # si llega aca carta perdida
                    window[f'-IMG_{len(img_act) + 1}-'].update(PATH_NOTCHECK_PNG)
                    img_act.append(False)
                    time_y_punt[1] -= config['Puntaje_restar']
                    carta_buena = data[window_update(window, dificultad)][5]
                    time_y_punt[0] = time()

        else:
            if time_y_punt[1] <= 0:
                time_y_punt[1] = 0
            sg.popup("No puedes seguir jugando", "Puntaje obtenido: ", f'{time_y_punt[1]}')
            guardar_puntaje(user, time_y_punt[1])
            guardar_info(user, dificultad)
            window.close()
            break
