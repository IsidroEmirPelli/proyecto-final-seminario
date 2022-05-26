import random
import string
import PySimpleGUI as sg



def build():
    """Construye la ventana de las puntuaciones"""
    sg.theme("LightBlue")

    test_array = [
        ["pepe 10","pepe 10","pepe 10","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 100","pepe 100","pepe 100","pepe 10"],
        ["pepe 400","pepe 400","pepe 400","pepe 10"]
    ]


    headings_array = ["facil", "normal", "dificil", "experto"]


   


    layout = [
        [sg.Push(),sg.Button("Volver", font="Verdana 12", border_width=2, size=(10,1), key="-MENU-")],
       
        [sg.Push(),sg.Table(values=test_array, headings=headings_array,
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
                    
        




    

    



    

   

    