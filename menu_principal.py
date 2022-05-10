# create a menu with 4 buttons : play ,configuration, scores and profile in PySimpleGUI and a new window for each button empty
#also create a dropdow menu called difficulty with 3 buttons : easy, medium and hard




import PySimpleGUI as sg


def play():
    sg.Popup("play")


def configuration():
    sg.Popup("configuration")


def scores():
    sg.Popup("scores")


def profile():
    sg.Popup("profile")


layout_center = [

    
    [ sg.Stretch(),sg.Button("play"),sg.Stretch()],
    [ sg.Stretch(),sg.Button("configuration"),sg.Stretch()],
    [ sg.Stretch(),sg.Button("scores"),sg.Stretch()],
    [ sg.Stretch(),sg.Button("profile"),sg.Stretch()]
    
]

layout_right = [[sg.Stretch(),sg.OptionMenu(['Easy', 'Medium', 'Hard'], key='difficulty')],
                [sg.Stretch(),sg.OptionMenu(['Jose', 'Maria', 'Pepe','Ana'], key='user')]

]

layout = [layout_right , layout_center]


window = sg.Window("menu", layout, resizable=True, size=(500, 500),auto_size_buttons=True,keep_on_top=True)


while True:
    event, values = window.Read()
    if event == "play":
        play()
    elif event == "configuration":
        configuration()
    elif event == "scores":
        scores()
    elif event == "profile":
        profile()
    elif event == sg.WIN_CLOSED:
        break
window.Close()
