# create a menu with 4 buttons : play ,configuration, scores and profile in PySimpleGUI and a new window for each button empty
#also create a dropdow menu called difficulty with 3 buttons : easy, medium and hard

import PySimpleGUI as sg
from windows import profile_screen, config_screen, game_screen, scores_screen

def build():
    """"Construye la ventana del menú principal"""

    sg.theme("DarkPurple1")

    layout_center = [
        [sg.Text("FiguRace")],
        [sg.Button("Play", key="-GAME-")],
        [sg.Button("Configuration", key="-CONFIG-")],
        [sg.Button("Scores", key="-SCORES-")],
        [sg.Button("Profile", key="-PROFILE-")]
    ]

    layout_right = [
        [sg.OptionMenu(["Easy", "Medium", "Hard"], key="-DIFFICULTY-")],
        [sg.OptionMenu(["Jose", "Maria", "Pepe", "Ana"], key="-USER-")]
    ]

    layout = [[layout_right], [layout_center]]

    window = sg.Window("FiguRace *-* Inicio", layout, resizable=True, size=(500, 500), auto_size_buttons=True,
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
        profile_screen.build()
        current_window.close()
