import PySimpleGUI as sg
from scripts.graphics import *


def build():
    sg.theme('LightBlue')
    fuente = 'Verdana', 11

    layout = [
        [sg.VPush()],
        [sg.Button('Partidas Finalizadas por Dificultad', font=fuente, size=(30, 1), key='-PAR_FIN_DIF-')],
        [sg.Button('Volver', font=fuente, size=(10, 1), key='-VOLVER-')],
        [sg.VPush()]
    ]

    window = sg.Window('FiguRace *-* Estadisticas', layout, resizable=True, size=(600, 640), auto_size_buttons=True,
                       element_justification='c')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == '-PAR_FIN_DIF-':
            level_graphic()

        elif event == '-VOLVER-':
            window.close()
            break
