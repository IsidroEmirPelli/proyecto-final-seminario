import PySimpleGUI as sg
import os
import profile_screen, config_screen, game_screen, scores_screen


def build():
    """"Construye la ventana del menú principal"""

    sg.theme("LightBlue")

    path_images = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))
    path_logo = os.path.join(path_images, 'logo.png')

    col_options = [
        [sg.OptionMenu(values=["Fácil", "Normal", "Difícil", "Experto"],
                       default_value="Dificultad", size=(10, 3), key="-DIFFICULTY-")],
        [sg.OptionMenu(values=["Jose", "Maria", "Pepe", "Ana"], default_value="Usuario", size=(10, 3), key="-USER-")]
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
    return window


build()


while True:
    current_window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == "-EXIT-":
        current_window.close()
        break
    elif event == "-MENU-":
        build()
        current_window.close()
    elif event == "-GAME-":
        game_screen.build()
        current_window.close()
    elif event == "-CONFIG-":
        config_screen.build()
        current_window.close()
    elif event == "-PROFILE-":
        profile_screen.build()
        current_window.close()
    elif event == "-SCORES-":
        scores_screen.build()
        current_window.close()
