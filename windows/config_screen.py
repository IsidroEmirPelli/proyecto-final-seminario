import PySimpleGUI as sg
import os
import json


def crear_arch_config():
    config = {"Tiempo": "60", "Rondas": "5", "Puntaje_sumar": "10", "Puntaje_restar": "5",
              "Cant_pistas": {"Facil": "5", "Normal": "3", "Dificil": "2"}
              }
    with open(os.path.join(os.path.dirname(__file__), '..', 'users', 'config.json'), 'w') as arch:
        json.dump(config, arch, indent=4)


def actualizar_config(values):
    with open(os.path.join(os.path.dirname(__file__), '..', 'users', 'config.json'), 'r') as arch:
        config = json.load(arch)

    if values['-TIME-']:
        config['Tiempo'] = int(values['-TIME-'])
    if values['-ROUNDS-']:
        config['Rondas'] = int(values['-ROUNDS-'])
    if values['-WINSCORE-']:
        config['Puntaje_sumar'] = int(values['-WINSCORE-'])
    if values['-LOSESCORE-']:
        config['Puntaje_restar'] = int(values['-LOSESCORE-'])
    if values['-EASYCAR-']:
        config['Cant_pistas']['Facil'] = int(values['-EASYCAR-'])
    if values['-NORMALCAR-']:
        config['Cant_pistas']['Normal'] = int(values['-NORMALCAR-'])
    if values['-HARDCAR-']:
        config['Cant_pistas']['Dificil'] = int(values['-HARDCAR-'])

    with open(os.path.join(os.path.dirname(__file__), '..', 'users', 'config.json'), 'w') as arch:
        json.dump(config, arch, indent=4)


def build():
    """Crea la ventana de configuración del juego"""

    sg.theme('LightBlue')
    with open(os.path.join(os.path.dirname(__file__), '..', 'users', 'config.json'), 'r') as arch:
        config = json.load(arch)

    gen_txt = [
        [sg.Text('Tiempo límite por ronda', font=('Verdana', 12), pad=(10, 10))],
        [sg.Text('Cantidad de rondas por juego', font=('Verdana', 12), pad=(10, 10))],
        [sg.Text('Puntaje sumado por cada respuesta correcta', font=('Verdana', 12), pad=(10, 10))],
        [sg.Text('Puntaje restado por cada respuesta incorrecta', font=('Verdana', 12), pad=(10, 10))]
    ]

    gen_opt = [
        [sg.InputCombo((30, 60, 90), default_value=config['Tiempo'], size=(10, 1), pad=(10, 10), key='-TIME-')],
        [sg.InputCombo((5, 8, 10), default_value=config['Rondas'], size=(10, 1), pad=(10, 10), key='-ROUNDS-')],
        [sg.InputCombo([5, 10, 15], default_value=config['Puntaje_sumar'], size=(10, 1), pad=(10, 10),
                       key='-WINSCORE-')],
        [sg.InputCombo([0, 5, 10], size=(10, 1), default_value=config['Puntaje_restar'], pad=(10, 10),
                       key='-LOSESCORE-')]
    ]

    general = [
        [sg.Frame('Configuraciones generales', [[
            sg.Column(layout=gen_txt, element_justification='l'),
            sg.Column(layout=gen_opt, element_justification='r')
        ]], font=('Verdana', 12))]
    ]

    level_txt = [
        [sg.Text('Fácil', font=('Verdana', 12), pad=(10, 10))],
        [sg.Text('Normal', font=('Verdana', 12), pad=(10, 10))],
        [sg.Text('Difícil', font=('Verdana', 12), pad=(10, 10))]
    ]

    level_opt = [
        [sg.OptionMenu((1, 2, 3, 4, 5), default_value=config['Cant_pistas']['Facil'], size=(10, 1), pad=(10, 10),
                       key='-EASYCAR-')],
        [sg.OptionMenu((1, 2, 3, 4), default_value=config['Cant_pistas']['Normal'], size=(10, 1), pad=(10, 10),
                       key='-NORMALCAR-')],
        [sg.OptionMenu((1, 2, 3), default_value=config['Cant_pistas']['Dificil'], size=(10, 1), pad=(10, 10),
                       key='-HARDCAR-')]
    ]

    level = [
        [sg.Frame('Cantidad de características a mostrar según el nivel', [[
            sg.Column(layout=level_txt, element_justification='l'),
            sg.Push(),
            sg.Column(layout=level_opt, element_justification='r')
        ]], font=('Verdana', 12))]
    ]

    layout = [
        [sg.VPush()],
        [sg.Column(general, element_justification='c')],
        [sg.Column(level, element_justification='c')],
        [sg.VPush()],
        [sg.Button('Aceptar', font=('Verdana', 12), border_width=2, size=(10, 1), key='-OK-')],
        [sg.Button('Volver', font=('Verdana', 12), border_width=2, size=(10, 1), key='-VOLVER-')]
    ]

    window = sg.Window('FiguRace *-* Configuración', layout, resizable=True, size=(800, 600), auto_size_buttons=True,
                       keep_on_top=False, finalize=True, element_justification='c')
    while True:
        event, values = window.read()

        if event == '-OK-':
            actualizar_config(values)
            sg.popup('Configuración guardada con éxito', title='FiguRace *-* Configuración', keep_on_top=True)
        elif event == '-VOLVER-':
            window.close()
            break
