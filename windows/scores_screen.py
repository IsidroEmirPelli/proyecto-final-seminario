import PySimpleGUI as sg

def build():
    """Construye la ventana de las puntuaciones"""
    sg.theme("DarkPurple1")

    layout = [
        [sg.Button("Volver", key="-MENU-")]
    ]

    window = sg.Window("FiguRace *-* Puntajes", layout, resizable=True, size=(500, 500), auto_size_buttons=True,
                       keep_on_top=False, finalize=True)

    return window
