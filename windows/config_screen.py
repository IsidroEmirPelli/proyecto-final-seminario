import PySimpleGUI as sg

def build():
    """Crea la ventana de configuración del juego"""

    sg.theme("DarkPurple1")

    layout = [
        [sg.Text("Tiempo límite por ronda: "), sg.InputText()],
        [sg.Text("Cantidad de rondas por juego: "), sg.InputText()],
        [sg.Text("Puntaje sumado por cada respuesta correcta: "), sg.OptionMenu([5, 10, 15])],
        [sg.Text("Puntaje restado por cada respuesta incorrecta: "), sg.OptionMenu([0, 5, 10])],
        [sg.Text("Cantidad de características a mostrar según el nivel (?): ")],
        [sg.Button("Volver", key="-MENU-")]
    ]

    window = sg.Window("FiguRace *-* Configuración", layout, resizable=True, size=(500, 500), auto_size_buttons=True,
                       keep_on_top=False, finalize=True)

    return window
