import json
import csv
from random import choice, randrange
import PySimpleGUI as sg
from scripts.gamescreen.constant import *


def get_config():
    """ Obtiene la información de configuración del usuario. """

    try:
        with open(PATH_CONFIG, 'r') as j:
            config = json.load(j)
        return config
    except FileNotFoundError:
        sg.PopupError("No se encontró el archivo de configuración.")

def select_csv():
    """ Selecciona un Data set aleatoriamente si esta en True"""

    config = get_config()
    return choice(list({key: value for key, value in config['Datasets'].items() if value}))

def get_card_data():
    """ Obtiene los headers y data del CSV seleccionado. """
    csv_selected = select_csv()
    with open(PATHS[csv_selected][0], 'r', encoding='utf-8') as reader:
        reader = csv.reader(reader, delimiter=',')
        header, data = next(reader), list(reader)

    return csv_selected, header, data

def create_col_result(clave_al, user):
    """ Creacion de columna izquierda(categoria, resultado parcial y abandonar partida) """
    
    check = [[sg.Text(f'{index}- ', size=(4, 1)), sg.Image('', size=(15, 15), key=f'-IMG_{index}-')] for index in range(1, 11)]
    col_resultado_parcial = [
        [sg.Text(f"{user}")],
        [sg.Column(check)],
    ]

    col_left = [
        [sg.Text(f"-{clave_al}-", key='-TEXTO_DATA-', pad=((65, 0), (0, 0)), font=GEN_FONT)],
        [sg.Image(PATHS[clave_al][1], key='-IMGDATA-')],
        [sg.Frame(f'{"Resultado Parcial"}', [[sg.Column(col_resultado_parcial)]],pad=((22,0),(0,0)), font=GEN_FONT)],
        [sg.Button("Abandonar", font=GEN_FONT, border_width=2, size=(18, 1), key="-VOLVER-")]
    ]

    return col_left


def otras_cartas(num_car, data) -> int:
    """retorna "cartas" aleatoria que no sea la que se esta jugando"""
    
    act_cards = []
    while len(act_cards) != 5:
        num = randrange(len(data))
        if num not in act_cards and num != num_car:
            act_cards.append(num)

    return act_cards

def select_randomly(opciones):
    """ Mezcla las cartas de forma aleatoria """

    rtas= []
    for i in range(5):
        index = choice(range(len(opciones)))
        rtas.append(opciones[index])
        del opciones[index]
    return rtas

def create_right_col(header, data, dificultad, num_carta):


    def datos_tarjeta(header, data, dificultad, num_carta):
        """ Retorna la cantidad de pistas con las que se haya configurado """

        config = get_config()
        cant = config['Cant_pistas'][dificultad]

        return [[sg.Text(f"{header[index]}: {data[num_carta][index]}", font=GEN_FONT, key=f'-HINT_{index}-')] for index in range(cant)]


    def generating_box(data, num_carta):
        """ Genero el box con las otras cartas """

        other_cards = otras_cartas(num_carta, data)
        cards = [[sg.Push(), sg.Button(f'{data[other_cards[index]][5]}', font=GEN_FONT, border_width=2, size=(20, 0), key=f'-CARTA_{index}-'),
            sg.Push()] for index in range(1, 5)] + [[sg.Push(), sg.Button(f'{data[num_carta][5]}', font=GEN_FONT, border_width=2, size=(20, 0), key='-CARTA_5-'), sg.Push()]]
        return select_randomly(cards)


    box_tarjeta = [
        [sg.Column(datos_tarjeta(header, data, dificultad, num_carta), size=(800, 150))],  # box de cantidad de pistas
        [sg.Text(f"{header[5]}: ")],
        [sg.Column(generating_box(data, num_carta))],  # box de pistas
        [sg.Push(), sg.Button("Pasar >", font=GEN_FONT, border_width=2, size=(10, 0), key="-PASAR-")]
    ]

    col_right = [
        [sg.Text(f'Nivel: {dificultad}')],  # -> determinar la dificultad
        [sg.Text(f'Tiempo total: {10}min', justification="right", font=GEN_FONT)],
        # -> determinar el tiempo segun la dificultad o configuracion
        [sg.Push(), sg.Text("00:00", justification="center", key="-Timer-", text_color='#ff0055', font=("Verdana", 12)),
         sg.Push()],
        [sg.Frame(f'Tarjeta {"1"}', [[sg.Column(layout=box_tarjeta)]], font=GEN_FONT)],
    ]

    return col_right


def window_update(window, dificultad):
    """ Actualiza la ventana con la información de la carta actual """

    config = get_config()
    cant = config['Cant_pistas'][dificultad]
    
    csv_selected, header, data = get_card_data()
    num_carta = randrange(len(data))  # obtengo carta a jugar aleatoriamente
    otras_cards = otras_cartas(num_carta, data)

    cartas = [f'{data[otras_cards[index]][5]}' for index in range(len(otras_cards))]
    cartas.append(f'{data[num_carta][5]}')

    cartas = select_randomly(cartas)
    
    window['-TEXTO_DATA-'].update(f"-{csv_selected}-")
    window['-IMGDATA-'].update(PATHS[csv_selected][1])
    for index in range(cant):
        window[f'-HINT_{index}-'].update(f"{header[index]}: {data[num_carta][index]}")
    
    for index in range(1, 6):
        window[f'-CARTA_{index}-'].update(f'{cartas[index-1]}')

    return num_carta