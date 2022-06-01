import PySimpleGUI as sg
import os
import json


def crear_arch_config():
    """Crea el json de configuración con una configuración estándar inicial"""

    config = {'Tiempo': 60, 'Rondas': 5, 'Puntaje_sumar': 10, 'Puntaje_restar': 5,
              'Cant_pistas': {'Facil': 5, 'Normal': 3, 'Dificil': 2},
              'Datasets': {'Volcanes': True, 'Spotify': True, 'FIFA': True}
              }
    with open(os.path.join(os.path.dirname(__file__), '..', 'users', 'config.json'), 'w') as arch:
        json.dump(config, arch, indent=4)


def actualizar_config(values):
    """Actualiza la configuración en el json"""

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
    if values['-VOLCANES-'] != config['Datasets']['Volcanes']:
        config['Datasets']['Volcanes'] = values['-VOLCANES-']
    if values['-SPOTIFY-'] != config['Datasets']['Spotify']:
        config['Datasets']['Spotify'] = values['-SPOTIFY-']
    if values['-FIFA-'] != config['Datasets']['FIFA']:
        config['Datasets']['FIFA'] = values['-FIFA-']

    with open(os.path.join(os.path.dirname(__file__), '..', 'users', 'config.json'), 'w') as arch:
        json.dump(config, arch, indent=4)


def verificar_config():
    """Verifica que la configuracion ingresada por el usuario no sea ilógica para el juego"""

    with open(os.path.join(os.path.dirname(__file__), '..', 'users', 'config.json'), 'r') as arch:
        config = json.load(arch)
        if 0 in (config['Tiempo'], config['Rondas']) or True not in (list(config['Datasets'].values())):
            return False
    return True


def build():
    """Crea la ventana de configuración del juego"""

    sg.theme('LightBlue')
    with open(os.path.join(os.path.dirname(__file__), '..', 'users', 'config.json'), 'r') as arch:
        config = json.load(arch)

    #construcción del área de configuraciones generales
    gen_txt = [
        [sg.Text('Tiempo límite por ronda (en segundos)', font=('Verdana', 12), pad=(10, 10))],
        [sg.Text('Cantidad de rondas por juego', font=('Verdana', 12), pad=(10, 10))],
        [sg.Text('Puntaje sumado por cada respuesta correcta', font=('Verdana', 12), pad=(10, 10))],
        [sg.Text('Puntaje restado por cada respuesta incorrecta', font=('Verdana', 12), pad=(10, 10))],
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
        [sg.Frame('Configuración general', [[
            sg.VPush(),
            sg.Column(layout=gen_txt, element_justification='l'),
            sg.Push(),
            sg.Column(layout=gen_opt, element_justification='r'),
            sg.VPush()
        ]], font=('Verdana', 14), size=(550, 200))]
    ]

    #construcción del área de selección de datasets
    datasets_opt = [
        [sg.Text('Elige al menos una', font=('Verdana', 11))],
        [sg.Checkbox('Erupciones volcanicas', default=config['Datasets']['Volcanes'],
                     enable_events=True, font=('Verdana', 12), pad=(10, 10), key='-VOLCANES-')],
        [sg.Checkbox('Spotify Top 100 2010-2019', default=config['Datasets']['Spotify'],
                     enable_events=True, font=('Verdana', 12), pad=(10, 10), key='-SPOTIFY-')],
        [sg.Checkbox('Jugadores FIFA 2021', default=config['Datasets']['FIFA'],
                     enable_events=True, font=('Verdana', 12), pad=(10, 10), key='-FIFA-')]
    ]

    datasets = [
        [sg.Frame('Categorías para jugar', layout=datasets_opt, font=('Verdana', 14),
                  pad=(10, 10), size=(550, 200))]
    ]

    #construcción del área de configuraciones por nivel
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
        ]], font=('Verdana', 14), size=(550, 180))]
    ]

    #construcción del layout
    layout = [
        [sg.VPush()],
        [sg.Column(general, element_justification='c')],
        [sg.Column(level, element_justification='c')],
        [sg.Column(datasets, element_justification='c')],
        [sg.VPush()],
        [sg.Button('Aceptar', font=('Verdana', 12), border_width=2, size=(10, 1), key='-OK-')],
        [sg.Button('Volver', font=('Verdana', 12), border_width=2, size=(10, 1), key='-VOLVER-')]
    ]

    window = sg.Window('FiguRace *-* Configuración', layout, resizable=True, size=(800, 800), auto_size_buttons=True,
                       keep_on_top=False, finalize=True, element_justification='c')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break
        if event == '-OK-':
            actualizar_config(values)
            if verificar_config():
                sg.popup('Configuración guardada con éxito', title='¡Hecho!', keep_on_top=True,
                         font=('Verdana', 12))
                window.close()
            else:
                sg.popup('Por favor verifica tus opciones', title='¡Cuidado!', keep_on_top=True,
                         font=('Verdana', 12))
        elif event == '-VOLVER-':
            window.close()
            break
