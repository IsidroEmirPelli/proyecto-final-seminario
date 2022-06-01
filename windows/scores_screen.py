from csv import reader
import pandas as pd
import PySimpleGUI as sg
import os


def build():
    """Construye la ventana de las puntuaciones"""
    sg.theme("LightBlue")

    path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'users'))
    
    
    path_scores = os.path.join(path_csv, 'scores.csv')

    
    scores_dicctionary = {'facil': [], 'normal': [], 'dificil': []}

    
    headings_array = ["FACIL", "NORMAL", "DIFICIL"]

   
    def load_score_dicctionary():
        """ funion que lee el archivo csv y devuelve un diccionario con key: dificultad y value: lista de tuplas """
        with open(path_scores, 'r') as csv_file:
            csv_reader = reader(csv_file, delimiter=',')
            for row in csv_reader:
                scores_dicctionary[row[1]].append((row[0], row[2]))
        return scores_dicctionary


    load_score_dicctionary()


    # function that sorts the scores in the dicctionary
    def sort_scores(dicctionary):
        """ funcion que ordena los scores de mayor a menor en el dicionario"""
        for key in dicctionary:
            dicctionary[key].sort(key=lambda tup: int(tup[1]), reverse=True)
        return dicctionary


    sort_scores(scores_dicctionary)


    # convert all the tuples in the dictionary to a list of strings
    def convert_touple_to_string():
        """ funcion que convierte todas las tuplas en strings en el diccionario"""
        for key in scores_dicctionary:
            scores_dicctionary[key] = [str(tup[0]) + " : " + str(tup[1]) for tup in scores_dicctionary[key]]
        return scores_dicctionary


    convert_touple_to_string()


    # usando pandas se convierte el diccionario en un dataframe
    df = pd.DataFrame(scores_dicctionary.values())


    # se rotan solamente los primeros 20 elementos de cada lista
    result2 = [list(x) for x in zip(*df.values)][0:20]


    layout = [
        [sg.Push(), sg.Table(values=result2, headings=headings_array,
                             # background_color='light blue',
                             auto_size_columns=False,
                             display_row_numbers=False,
                             justification='center',
                             num_rows=20,
                             alternating_row_color='lightyellow',
                             key='-TABLE-',
                             row_height=35), sg.Push()],
        [sg.Push(), sg.Button("Volver", font="Verdana 12", border_width=2, size=(10, 1), key="-VOLVER-")]
    ]


    window = sg.Window("FiguRace *-* Puntajes", layout, resizable=True, size=(600, 800), auto_size_text=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-VOLVER-":
            window.close()
            break
