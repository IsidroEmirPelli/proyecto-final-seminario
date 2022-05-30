import PySimpleGUI as sg
import json, os


def getting_path():
    return os.path.join(os.getcwd(), 'users', 'users.json')


def creating_user_file(values):
    user_dict = [{"Nickname": values['-NICK-'], "Edad": values['-EDAD-'], "Genero": values['-GENERO-']}]
    print(user_dict)
    with open(getting_path(), 'w') as users:
        json.dump(user_dict, users, indent=4)


def create_new_user(values):
    new_user = {"Nickname": values['-NICK-'], "Edad": values['-EDAD-'], "Genero": values['-GENERO-']}
    with open(getting_path(), 'r') as users:
        users_list = json.load(users)
    users_list.append(new_user)
    with open(getting_path(), 'w') as users:
        json.dump(users_list, users, indent=4)


def modify_user(values):
    new_user = {"Nickname": values['-NICK-'], "Edad": values['-EDAD-'], "Genero": values['-GENERO-']}
    with open(getting_path(), 'r') as users:
        users_list = json.load(users)
    for i in range(len(users_list)):
        if users_list[i]['Nickname'] == values['-NICK-']:
            users_list[i] = new_user
            break
    with open(getting_path(), 'w') as users:
        json.dump(users_list, users, indent=4)


def check_profile(values):
    """Verifico si existe el nickname
    En caso de que no exista el archivo va a saltar la excepcion y va a crear el archivo con los datos ingresados"""
    try:
        archivo = open(getting_path(), 'r')
        users = json.load(archivo)
        archivo.close()
    except FileNotFoundError:
        creating_user_file(values)
    else:
        """Verifico si existe el usuario si no se cumple la excepcion anterior"""
        found = False
        for user in users:
            if values['-NICK-'] == user['Nickname']:
                found = True
                break
        if found:
            modify_user(values)
        else:
            create_new_user(values)


def build():
    """Construye la ventana de las perfiles"""
    # Variables utilizadas para tamaños
    generos = ['Masculino', 'Femenino', 'Otro']
    size_button = (8, 1)
    size_input = (38, 1)
    spc_btw_button = (40, 2)
    padding_text = (40, 0)
    sg.theme("LightBlue")

    """Creacion de LayOut"""
    layout = [
        [sg.Text('Creacion/Edicion de perfil', pad=(41, 0), font=('Any 25'))],
        [sg.Text("Nickname", pad=padding_text), sg.Input(key='-NICK-', size=size_input)],
        [sg.Text("Género", pad=padding_text), sg.Combo(generos, pad=(21, 0), key='-GENERO-')],
        [sg.Text("Edad", pad=padding_text),
         sg.Spin([i for i in range(1, 110)], initial_value=0, size=(3, 1), key='-EDAD-', pad=(32, 0))],
        [sg.Button('Aceptar', size=size_button, pad=spc_btw_button, key='-ACEPTAR-'),
         sg.Button('Borrar', size=size_button, pad=spc_btw_button, key='-BORRAR-'),
         sg.Button('Volver', size=size_button, pad=spc_btw_button, key='-VOLVER-')]
    ]
    window = sg.Window("FiguRace *-* Perfiles", layout, resizable=False, margins=(20, 20), size=(500, 200),
                       auto_size_buttons=True, keep_on_top=False, finalize=True)
    while True:
        """Inicio la ventana"""
        event, values = window.read()
        if event == '-ACEPTAR-':
            if (values['-NICK-'] == '' or values['-EDAD-'] == 0 or values['-GENERO-'] == ''):
                sg.popup('Por favor complete todos los campos', title='Error')
            else:
                if (values['-NICK-'] == 'Usuarios'):
                    sg.popup('Nickname invalido', title='Error')
                    window['-NICK-'].update('')
                else:
                    if values['-GENERO-'] in generos:
                        check_profile(values)
                        sg.popup('Perfil creado/modificado con exito')
                    else:
                        sg.popup('Por favor seleccione un genero valido', title='Error')
                        window['-GENERO-'].update('')
        elif event == '-BORRAR-':
            window['-NICK-'].update('')
            window['-EDAD-'].update(0)
            window['-GENERO-'].update('')
        elif event == '-VOLVER-':
            window.close()
            break
        elif event == sg.WIN_CLOSED:
            break
