from email.policy import default
from types import NoneType
import PySimpleGUI as sg
import json
import os
from windows import profile_screen, config_screen, game_screen, scores_screen


def check_user(user):
    return user == "USUARIO" or user == ""


def getting_users():
    with open(os.path.join(os.path.dirname(__file__), '..', 'users', 'users.json'), 'r') as users:
        users_list = json.load(users)
    return [user['Nickname'] for user in users_list]


def create_user_file():
    """"Crea el archivo de usuarios"""
    default_user = {
        'Nickname':"User",
        'Edad':0,
        'Genero':'Otro'}
    with open(os.path.join(os.path.dirname(__file__), '..', 'users', 'users.json'), 'w') as users:
        json.dump([default_user], users)
    return getting_users()



def generate_option_menu():
    """"Genera el menu de opciones desde el json"""
    try:
        return getting_users()
    except FileNotFoundError or NoneType:
        return create_user_file() 

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
    return dificultad == "DIFICULTAD"


def build():
    """"Construye la ventana del menú principal"""

    sg.theme("LightBlue")

    path_images = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))
    path_logo = os.path.join(path_images, 'logo.png')

    col_options = [
        [sg.OptionMenu(values=generate_dificulty_menu(),
                       default_value="DIFICULTAD", size=(13, 3), key="-DIFFICULTY-")],
        [sg.OptionMenu(values=generate_option_menu(), default_value="USUARIO", size=(13, 3), key="-USER-")]
    ]

    layout = [
        [sg.Push(), sg.Column(col_options, element_justification="r")],
        [sg.VPush()],
        [sg.Image(path_logo)],
        [sg.Text('')],
        [sg.Button("JUGAR", font=("Verdana", 12), border_width=2, size=(22, 2), key="-GAME-")],
        [sg.Button("PERFILES", font=("Verdana", 12), border_width=2, size=(22, 2), key="-PROFILE-")],
        [sg.Button("PUNTAJES", font=("Verdana", 12), border_width=2, size=(22, 2), key="-SCORES-")],
        [sg.Button("CONFIGURACION", font=("Verdana", 12), border_width=2, size=(22, 2), key="-CONFIG-")],
        [sg.Button("SALIR", font=("Verdana", 12), border_width=2, size=(22, 2), key="-EXIT-")],
        [sg.VPush()]
    ]
    window = sg.Window("FiguRace", layout, resizable=True, size=(600, 600), auto_size_buttons=True,
                       element_justification="c")

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "-EXIT-"):
            break
        elif event == "-GAME-":
            if check_user(values['-USER-']):
                sg.popup("Seleccione un usuario o regístrese", title="¡Ups!")
            elif check_difficulty(values['-DIFFICULTY-']):
                sg.popup("Seleccione una dificultad para jugar", title="¡Ups!")
            else:
                window.hide()
                game_screen.build(values["-USER-"], values["-DIFFICULTY-"])
                window.un_hide()
        elif event == "-CONFIG-":
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
