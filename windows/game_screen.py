import csv

import PySimpleGUI as sg
import os
from random import randrange



def build():

    #Futuros parametros

    path_images = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))
    path_fifapng = os.path.join(path_images, 'FIFA21.png')
    path_erupcionespng = os.path.join(path_images, 'Erupciones-volcanicas.png')
    path_spotifypng = os.path.join(path_images, 'Spotify_2.png')
    path_checkpng = os.path.join(path_images, 'check.png')
    path_notcheckpng = os.path.join(path_images, 'not_check.png')



    path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data_sets'))
    path_spotifycsv = os.path.join(path_csv, 'New-Spotify-2010-2019-Top-100.csv')
    path_erupcionescsv = os.path.join(path_csv, 'new-significant-volcanic-eruption-database.csv')
    path_fifacsv = os.path.join(path_csv, 'New-FIFA-21-Complete.csv')

    list_paths = [(path_erupcionescsv, path_erupcionespng), (path_fifacsv, path_fifapng),
                  (path_spotifycsv, path_spotifypng)]

    tema_a_jugar = list_paths[randrange(len(list_paths))]

    #randrange(len(list_paths))

    reader = csv.reader(open(tema_a_jugar[0], 'r', encoding='utf-8'), delimiter=',')
    header, data = next(reader), list(reader)


    num_carta = randrange(len(data))    #obento carta a jugar aleatoriamente

    #retorna "cartas" aleatoria que no sea la que se esta jugando
    def otras_cartas(num_car) -> int: #------------------------------------> pasa como parametro??
        num = randrange(len(data))
        while num == num_car:
            randrange(len(data))
        return num

    """Funcion que construye la ventana del juego"""
    sg.theme("LightBlue")

    #********************* cracion de columna izquierda(categoria, resultado parcial y abandonar partida) **********
    col_resultado_parcial= [
        [sg.Text("[nombre Usuario]")],        #->vincular con el json
        [sg.Text("1- "), sg.Image(path_notcheckpng, size=(15, 15))],          #-> crear box por tamaño en la configuracion
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

        [sg.Push(), sg.Text('-Catergoria-'), sg.Push()],
        [sg.Image(tema_a_jugar[1], size=(220, 100))],        #->crear funcion para determinar que imagen poner
        [sg.Frame(f'{"Resultado Parcial"}', [[sg.Column(layout=col_resultado_parcial)]],
            font=("Verdana", 12))],
        [sg.Button("Abandonar Partida", font=("Verdana", 12), border_width=2, size=(20, 1), key="-MENU-")]

    ]

    #*************** Creacion columna derecha(dificultad, tiempo, box de tarjeta) *********************



    box_tarjeta = [

        [sg.Text(f"{header[0]}: {data[num_carta][0]}")],
        [sg.Text(f"{header[1]}: {data[num_carta][1]}")],
        [sg.Text(f"{header[2]}: {data[num_carta][2]}")],
        [sg.Text(f"{header[3]}: {data[num_carta][3]}")],
        [sg.Text(f"{header[4]}: {data[num_carta][4]}")],
        [sg.Text(f"{header[5]}: {data[num_carta][5]}-Adivine Doc-")],
        [sg.Push(), sg.Button(f'{data[otras_cartas(num_carta)][5]}', font=("Verdana", 12), border_width=2, size=(20, 0), key="-OP1-"), sg.Push()],
        [sg.Push(), sg.Button(f'{data[num_carta][5]}', font=("Verdana", 12), border_width=2, size=(20, 0), key="-OP2-"), sg.Push()],
        [sg.Push(), sg.Button(f'{data[otras_cartas(num_carta)][5]}', font=("Verdana", 12), border_width=2, size=(20, 0), key="-OP3-"), sg.Push()],
        [sg.Push(), sg.Button(f'{data[otras_cartas(num_carta)][5]}', font=("Verdana", 12), border_width=2, size=(20, 0), key="-OP4-"), sg.Push()],
        [sg.Push(), sg.Button(f'{data[otras_cartas(num_carta)][5]}', font=("Verdana", 12), border_width=2, size=(20, 0), key="-OP5-"), sg.Push()],
        [sg.Push(), sg.Button("OK", font=("Verdana", 12), border_width=2, size=(8, 0), key="-OP5-"),
         sg.Button("Pasar >", font=("Verdana", 12), border_width=2, size=(8, 0), key="-OP5-"), sg.Push()]

    ]

    col_right = [

        [sg.Text(f'Nivel: {"facil"}')],   #-> determinar la dificultad
        [sg.Text(f'Tiempo total: {10}min', justification="right", font=("Verdana", 12))],
        #-> determinar el tiempo segun la dificultad o configuracion
        [sg.Push(), sg.Text("00:00", justification="center", key="-Timer-", text_color='#ff0055',font=("Verdana", 12)),
            sg.Push()],
        [sg.Frame(f'trajeta {"1"}', [[sg.Column(layout=box_tarjeta)]], font=("Verdana", 12))]

    ]

    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Column(col_left), sg.Push(), sg.Column(col_right), sg.Push()],
        [sg.VPush()]
    ]

    window = sg.Window("FiguRace *-* ¡A jugar!", layout, resizable=True, size=(500, 500), auto_size_buttons=True,
                       keep_on_top=False, finalize=True)

    return window

