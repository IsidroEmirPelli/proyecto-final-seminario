import csv

import PySimpleGUI as sg
import os
from random import choice, randrange
import json


def build(user, dificultad):
    # path imagenes
    path_images = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))
    path_fifapng = os.path.join(path_images, 'FIFA21.png')
    path_erupcionespng = os.path.join(path_images, 'Erupciones-volcanicas.png')
    path_spotifypng = os.path.join(path_images, 'Spotify_2.png')
    path_checkpng = os.path.join(path_images, 'check.png')
    path_notcheckpng = os.path.join(path_images, 'not_check.png')

    # path csv
    path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data_sets'))
    path_spotifycsv = os.path.join(path_csv, 'New-Spotify-2010-2019-Top-100.csv')
    path_erupcionescsv = os.path.join(path_csv, 'new-significant-volcanic-eruption-database.csv')
    path_fifacsv = os.path.join(path_csv, 'New-FIFA-21-Complete.csv')

    # path json
    path_json = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'users'))
    path_config = os.path.join(path_json, 'config.json')

    with open(path_config, 'r') as j:
        config = json.load(j)

    # elijo csv a jugar aleatoriamente

    dicc_paths = {"Volcanes": (path_erupcionescsv, path_erupcionespng), "FIFA": (path_fifacsv, path_fifapng),
                  "Spotify": (path_spotifycsv, path_spotifypng)}

    clave_al = choice(["Volcanes", "Spotify", "FIFA"])
    while not config["Datasets"][clave_al]:  # itera hasta encontrar un dataset en true
        clave_al = choice(["Volcanes", "Spotify", "FIFA"])

    # apretura de csv
    with open(dicc_paths[clave_al][0], 'r', encoding='utf-8') as reader:
        reader = csv.reader(reader, delimiter=',')
        header, data = next(reader), list(reader)

    num_carta = randrange(len(data))  # obento carta a jugar aleatoriamente

    def otras_cartas(num_car) -> int:
        """retorna "cartas" aleatoria que no sea la que se esta jugando"""
        num = randrange(len(data))
        while num == num_car:
            randrange(len(data))
        return num

    # Construccion de la ventana del juego

    sg.theme("LightBlue")
    gen_font = 'Verdana', 12

    # ********************* cracion de columna izquierda(categoria, resultado parcial y abandonar partida) **********
    col_resultado_parcial = [
        [sg.Text(f"{user}")],
        [sg.Text("1- "), sg.Image(path_notcheckpng, size=(15, 15))],
        [sg.Text("2- "), sg.Image(path_notcheckpng, size=(15, 15))],
        [sg.Text("3- "), sg.Image(path_checkpng, size=(15, 15))],
        [sg.Text("4- "), sg.Image(path_notcheckpng, size=(15, 15))],
        [sg.Text("5- "), sg.Image(path_checkpng, size=(15, 15))],
        [sg.Text("6- ")],
        [sg.Text("7- ")],
        [sg.Text("8- ")],
        [sg.Text("9- ")],
        [sg.Text("10- ")]

    ]

    col_left = [

        [sg.Push(), sg.Text(f"-{clave_al}-"), sg.Push()],
        [sg.Image(dicc_paths[clave_al][1], size=(220, 100))],
        [sg.Frame(f'{"Resultado Parcial"}', [[sg.Column(layout=col_resultado_parcial)]],
                  font=("Verdana", 12))],
        [sg.Button("Abandonar Partida", font=gen_font, border_width=2, size=(20, 1), key="-VOLVER-")]

    ]

    # *************** Creacion columna derecha(dificultad, tiempo, box de tarjeta) *********************

    def datos_tarjeta():
        """retorna la cantidad de pistas con las que se haya configurado"""
        match (config['Cant_pistas'][dificultad]):
            case 1:
                return [[sg.Text(f"{header[0]}: {data[num_carta][0]}", font=gen_font)]]
            case 2:
                return [[sg.Text(f"{header[0]}: {data[num_carta][0]}", font=gen_font)],
                        [sg.Text(f"{header[1]}: {data[num_carta][1]}", font=gen_font)]]
            case 3:
                return [[sg.Text(f"{header[0]}: {data[num_carta][0]}", font=gen_font)],
                        [sg.Text(f"{header[1]}: {data[num_carta][1]}", font=gen_font)],
                        [sg.Text(f"{header[2]}: {data[num_carta][2]}", font=gen_font)]]
            case 4:
                return [[sg.Text(f"{header[0]}: {data[num_carta][0]}", font=gen_font)],
                        [sg.Text(f"{header[1]}: {data[num_carta][1]}", font=gen_font)],
                        [sg.Text(f"{header[2]}: {data[num_carta][2]}", font=gen_font)],
                        [sg.Text(f"{header[3]}: {data[num_carta][3]}", font=gen_font)]]
            case 5:
                return [[sg.Text(f"{header[0]}: {data[num_carta][0]}", font=gen_font)],
                        [sg.Text(f"{header[1]}: {data[num_carta][1]}", font=gen_font)],
                        [sg.Text(f"{header[2]}: {data[num_carta][2]}", font=gen_font)],
                        [sg.Text(f"{header[3]}: {data[num_carta][3]}", font=gen_font)],
                        [sg.Text(f"{header[4]}: {data[num_carta][4]}", font=gen_font)]]

    box_tarjeta = [

        [sg.Column(layout=datos_tarjeta())],  # box de cantidad de pistas
        [sg.Text(f"{header[5]}: ")],
        [sg.Push(), sg.Button(f'{data[otras_cartas(num_carta)][5]}', font=gen_font, border_width=2, size=(20, 0),
                              key="-OP1-"), sg.Push()],
        [sg.Push(), sg.Button(f'{data[num_carta][5]}', font=gen_font, border_width=2, size=(20, 0), key="-OP2-"),
         sg.Push()],
        [sg.Push(), sg.Button(f'{data[otras_cartas(num_carta)][5]}', font=gen_font, border_width=2, size=(20, 0),
                              key="-OP3-"), sg.Push()],
        [sg.Push(), sg.Button(f'{data[otras_cartas(num_carta)][5]}', font=gen_font, border_width=2, size=(20, 0),
                              key="-OP4-"), sg.Push()],
        [sg.Push(), sg.Button(f'{data[otras_cartas(num_carta)][5]}', font=gen_font, border_width=2, size=(20, 0),
                              key="-OP5-"), sg.Push()],
        [sg.Push(), sg.Button("Pasar >", font=gen_font, border_width=2, size=(10, 0), key="-PASAR-")]

    ]

    col_right = [

        [sg.Text(f'Nivel: {dificultad}')],  # -> determinar la dificultad
        [sg.Text(f'Tiempo total: {10}min', justification="right", font=("Verdana", 12))],
        # -> determinar el tiempo segun la dificultad o configuracion
        [sg.Push(), sg.Text("00:00", justification="center", key="-Timer-", text_color='#ff0055', font=("Verdana", 12)),
         sg.Push()],
        [sg.Frame(f'Tarjeta {"1"}', [[sg.Column(layout=box_tarjeta)]], font=("Verdana", 12))]

    ]

    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Column(col_left), sg.Push(), sg.Column(col_right), sg.Push()],
        [sg.VPush()]
    ]
    window = sg.Window("FiguRace *-* ¡A jugar!", layout, resizable=True, size=(600, 800), auto_size_buttons=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-VOLVER-':
            window.close()
