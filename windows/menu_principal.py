import PySimpleGUI as sg
import json
import os
from windows import profile_screen, config_screen, game_screen, scores_screen


def check_user(user):
    return user == "Usuarios"


def generate_option_menu():
    """"Genera el menu de opciones desde el json"""
    try:
        with open(os.path.join(os.path.dirname(__file__), '..', 'users', 'users.json'), 'r') as users:
            users_list = json.load(users)
        return [user['Nickname'] for user in users_list]
    except FileNotFoundError:
        return []


def generate_dificulty_menu():
    """"Genera el menu de dificultad desde el json"""
    try:
        arch = open(os.path.join(os.path.dirname(__file__), '..', 'users', 'config.json'), 'r')
    except FileNotFoundError:
        config_screen.crear_arch_config()
        arch = open(os.path.join(os.path.dirname(__file__), '..', 'users', 'config.json'), 'r')
    finally:
        config = json.load(arch)
        arch.close()
        return config["Cant_pistas"].keys()

def check_difficulty(dificultad):
    return dificultad == "Dificultad"

def build():
    """"Construye la ventana del menú principal"""

    sg.theme("LightBlue")

    path_images = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))
    path_logo = os.path.join(path_images, 'logo.png')

    col_options = [
        [sg.OptionMenu(values=generate_dificulty_menu(),
                       default_value="Dificultad", size=(10, 3), key="-DIFFICULTY-")],
        [sg.OptionMenu(values=generate_option_menu(), default_value="Usuarios", size=(10, 3), key="-USER-")]
    ]

    layout = [
        [sg.Push(), sg.Column(col_options, element_justification="right")],
        [sg.Image(path_logo)],
        [sg.Button("Jugar", font=("Verdana", 12), border_width=2, size=(20, 2), key="-GAME-")],
        [sg.Button("Configuración", font=("Verdana", 12), border_width=2, size=(20, 2), key="-CONFIG-")],
        [sg.Button("Puntajes", font=("Verdana", 12), border_width=2, size=(20, 2), key="-SCORES-")],
        [sg.Button("Perfiles", font=("Verdana", 12), border_width=2, size=(20, 2), key="-PROFILE-")],
        [sg.Button("Salir", font=("Verdana", 12), border_width=2, size=(20, 2), key="-EXIT-")]
    ]
    window = sg.Window("FiguRace", layout, resizable=True, size=(500, 700), auto_size_buttons=True,
                       keep_on_top=False, finalize=True, element_justification="center")

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "-EXIT-"):
            break
        elif event == "-GAME-":
            if check_user(values['-USER-']):
                sg.popup("No hay usuarios registrados/seleccionados", title="FiguRace")
            elif check_difficulty(values['-DIFFICULTY-']):
                sg.popup("No selecciono una dificultad", title="Error")
            else:
                window.hide()
                game_screen.build(values["-USER-"], values["-DIFFICULTY-"])
                window.un_hide()
        elif event == "-CONFIG-":
            if check_user(values['-USER-']):
                sg.popup("Primero crea o selecciona un usuario.", title="FiguRace")
            else:
                window.hide()
                config_screen.build()
                window.un_hide()
        elif event == "-PROFILE-":
            window.close()
            profile_screen.build()
            build()
        elif event == "-SCORES-":
            window.hide()
            scores_screen.build()
            window.un_hide()