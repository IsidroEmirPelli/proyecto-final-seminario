<<<<<<< HEAD

from csv import reader
=======
import pandas as pd
from csv import reader

>>>>>>> b16d1997ffcc2348dad35bdb806b18d306d14222
import PySimpleGUI as sg
import os
import pandas as pd


def build():
    """Construye la ventana de las puntuaciones"""
    sg.theme("LightBlue")

    path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'scores'))
    path_scores = os.path.join(path_csv, 'scores.csv')

    scores_dicctionary = {'facil': [], 'normal': [], 'dificil': []}

<<<<<<< HEAD

    headings_array = ["facil", "normal", "dificil"]
=======
    headings_array = ["facil", "normal", "dificil", "experto"]
>>>>>>> b16d1997ffcc2348dad35bdb806b18d306d14222

    # function that reads the csv file and return a dicctionary compose of key: difficulty and value: list of name and score tuple
    def load_score_dicctionary():
        with open(path_scores, 'r') as csv_file:
            csv_reader = reader(csv_file, delimiter=',')
            for row in csv_reader:
                scores_dicctionary[row[1]].append((row[0], row[2]))
<<<<<<< HEAD
                
        return scores_dicctionary       
    
    load_score_dicctionary()

    #function that sorts the scores in the dicctionary
    def sort_scores(dicctionary):
        for key in dicctionary:
            dicctionary[key].sort(key=lambda tup: int(tup[1]), reverse=True)
        return dicctionary
    
    sort_scores(scores_dicctionary)



=======
                scores_dicctionary[row[1]].sort(key=lambda tup: tup[1], reverse=True)
        return scores_dicctionary

    load_score_dicctionary()

>>>>>>> b16d1997ffcc2348dad35bdb806b18d306d14222
    # convert all the tuples in the dictionary to a list of strings
    def convert_touple_to_string():
        for key in scores_dicctionary:
            scores_dicctionary[key] = [str(tup[0]) + " : " + str(tup[1]) for tup in scores_dicctionary[key]]
        return scores_dicctionary

    convert_touple_to_string()
<<<<<<< HEAD
 
    #convert the dictionary to a dataframe
    df = pd.DataFrame(scores_dicctionary.values())
    
    #rotate the dataframe and show the best 20 scores of each difficulty
    result2 = [list(x) for x in zip(*df.values)][0:20]
=======

    df = pd.DataFrame(scores_dicctionary)
>>>>>>> b16d1997ffcc2348dad35bdb806b18d306d14222

    
    layout = [
<<<<<<< HEAD
        [sg.Push(),sg.Button("Volver", font="Verdana 12", border_width=2, size=(10,1), key="-MENU-")],
       
        [sg.Push(),sg.Table(values=result2, headings=headings_array,
                    # background_color='light blue',
                    auto_size_columns=False,
                    
                    display_row_numbers=False,
                    justification='center',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    
                    row_height=35),sg.Push()]
        ]
       
    
    
=======
        [sg.Push(), sg.Button("Volver", font="Verdana 12", border_width=2, size=(10, 1), key="-VOLVER-")],

        [sg.Push(), sg.Table(values=df, headings=headings_array,
                             # background_color='light blue',
                             auto_size_columns=False,

                             display_row_numbers=False,
                             justification='center',
                             num_rows=20,
                             alternating_row_color='lightyellow',
                             key='-TABLE-',

                             row_height=35), sg.Push()]
    ]

>>>>>>> b16d1997ffcc2348dad35bdb806b18d306d14222
    window = sg.Window("FiguRace *-* Puntajes", layout, resizable=True, size=(500, 600), auto_size_text=True,
                       keep_on_top=False, finalize=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-VOLVER-":
            window.hide()
            break
    return window
