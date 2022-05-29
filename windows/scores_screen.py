
import pandas as pd
from csv import reader




import PySimpleGUI as sg
import os




def build():
    """Construye la ventana de las puntuaciones"""
    sg.theme("LightBlue")
 


    path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data_sets'))
    path_scores = os.path.join(path_csv, 'scores.csv')

    scores_dicctionary = {'facil': [], 'normal': [], 'dificil': [], 'experto': []}


    headings_array = ["facil", "normal", "dificil", "experto"]

    # function that reads the csv file and return a dicctionary compose of key: difficulty and value: list of name and score tuple
    def load_score_dicctionary():
        with open(path_scores, 'r') as csv_file:
            csv_reader = reader(csv_file,delimiter=',')
            for row in csv_reader:
                scores_dicctionary[row[1]].append((row[0], row[2]))
                scores_dicctionary[row[1]].sort(key=lambda tup: tup[1], reverse=True)
        return scores_dicctionary       
    
    load_score_dicctionary()
    # convert all the tuples in the dictionary to a list of strings
    def convert_touple_to_string():
        for key in scores_dicctionary:
            scores_dicctionary[key] = [str(tup[0]) + ": " + str(tup[1]) for tup in scores_dicctionary[key]]
        return scores_dicctionary
    
    convert_touple_to_string()
   
    df = pd.DataFrame(scores_dicctionary)
    

    layout = [
        [sg.Push(),sg.Button("Volver", font="Verdana 12", border_width=2, size=(10,1), key="-MENU-")],
       
        [sg.Push(),sg.Table(values=df, headings=headings_array,
                    # background_color='light blue',
                    auto_size_columns=False,
                    
                    display_row_numbers=False,
                    justification='center',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    
                    row_height=35),sg.Push()]
        ]
       

       
                    
    
        
    
    window = sg.Window("FiguRace *-* Puntajes", layout, resizable=True, size=(500, 600), auto_size_text=True,
                        keep_on_top=False, finalize=True)

    return window
                
        




    

    



    

   

    