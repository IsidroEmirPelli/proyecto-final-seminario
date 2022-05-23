import PySimpleGUI as sg
from windows import profile_screen, config_screen, game_screen, scores_screen


def build():
    """"Construye la ventana del menú principal"""

    sg.theme("LightBlue")

    col = [
        [sg.OptionMenu(values=["Fácil", "Normal", "Difícil", "Experto"],
                       default_value="Dificultad", key="-DIFFICULTY-")],
        [sg.OptionMenu(values=["Jose", "Maria", "Pepe", "Ana"], default_value="Usuario", key="-USER-")]
    ]

    layout = [
        [sg.Push(), sg.Column(col, element_justification="right")],
        [sg.Push(), sg.Image(filename="logo.png"), sg.Push()],
        [sg.Push(), sg.Button("Jugar", font="Verdana 12", border_width=2, key="-GAME-"), sg.Push()],
        [sg.Push(), sg.Button("Configuración", font="Verdana 12", border_width=2, key="-CONFIG-"), sg.Push()],
        [sg.Push(), sg.Button("Puntajes", font="Verdana 12", border_width=2, key="-SCORES-"), sg.Push()],
        [sg.Push(), sg.Button("Perfiles", font="Verdana 12", border_width=2, key="-PROFILE-"), sg.Push()],
    ]

    window = sg.Window("FiguRace", layout, resizable=True, size=(500, 600), auto_size_buttons=True,
                       keep_on_top=False, finalize=True)
    return window


build()


while True:
    current_window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
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
