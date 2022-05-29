import PySimpleGUI as sg

def build(valores):
    """Crea la ventana de configuración del juego"""

    sg.theme("LightBlue")

    gen_txt = [
        [sg.Text("Tiempo límite por ronda: ", font=("Verdana", 12), pad=(10, 10))],
        [sg.Text("Cantidad de rondas por juego: ", font=("Verdana", 12), pad=(10, 10))],
        [sg.Text("Puntaje sumado por cada respuesta correcta: ", font=("Verdana", 12), pad=(10, 10))],
        [sg.Text("Puntaje restado por cada respuesta incorrecta: ", font=("Verdana", 12), pad=(10, 10))]
    ]

    gen_opt = [
        [sg.InputCombo((1, 2, 3), size=(10, 1), pad=(10, 10), key="-TIME-")],
        [sg.InputCombo((5, 10, 15, 20), size=(10, 1), pad=(10, 10), key="-ROUNDS-")],
        [sg.InputCombo([5, 10, 15], size=(10, 1), pad=(10, 10), key="-WINSCORE-")],
        [sg.InputCombo([0, 5, 10], size=(10, 1), pad=(10, 10), key="-LOSESCORE-")]
    ]

    general = [
        [sg.Frame("Configuraciones generales", [[
            sg.Column(layout=gen_txt, element_justification="l"),
            sg.Column(layout=gen_opt, element_justification="r")
        ]], font=("Verdana", 12))]
    ]

    level_txt = [
        [sg.Text("Fácil", font=("Verdana", 12), pad=(10, 10))],
        [sg.Text("Normal", font=("Verdana", 12), pad=(10, 10))],
        [sg.Text("Difícil", font=("Verdana", 12), pad=(10, 10))],
        [sg.Text("Extremo", font=("Verdana", 12), pad=(10, 10))]
    ]

    level_opt = [
        [sg.InputCombo((1, 2, 3, 4, 5), size=(10, 1), pad=(10, 10), key="-EASYCAR-")],
        [sg.InputCombo((1, 2, 3, 4), size=(10, 1), pad=(10, 10), key="-NORMALCAR-")],
        [sg.InputCombo((1, 2, 3), size=(10, 1), pad=(10, 10), key="-HARDCAR-")],
        [sg.InputCombo((1, 2), size=(10, 1), pad=(10, 10), key="-EXTREMECAR-")]
    ]

    level = [
        [sg.Frame("Cantidad de características a mostrar según el nivel", [[
            sg.Column(layout=level_txt, element_justification="l"),
            sg.Push(),
            sg.Column(layout=level_opt, element_justification="r")
        ]], font=("Verdana", 12))]
    ]

    layout = [
        [sg.VPush()],
        [sg.Column(general, element_justification="c")],
        [sg.Column(level, element_justification="c")],
        [sg.VPush()],
        [sg.Button("Aceptar", font=("Verdana", 12), border_width=2, size=(10, 1), key="-OK-")],
        [sg.Button("Volver", font=("Verdana", 12), border_width=2, size=(10, 1), key="-VOLVER-")]
    ]

    window = sg.Window("FiguRace *-* Configuración", layout, resizable=True, size=(800, 600), auto_size_buttons=True,
                       keep_on_top=False, finalize=True, element_justification="center")
    while True:
        event, values = window.read()

        if event == "-OK-":
            sg.popup("Configuración guardada con éxito", title="FiguRace *-* Configuración", keep_on_top=True)
        elif event == "-VOLVER-":
            window.close()
            break
