import PySimpleGUI as sg
import json, os


def getting_path():
    return os.path.join(os.getcwd(), 'users', 'users.json')


def creating_user_file(values):
    """Genero un diccionario con los valores y lo pongo dentro de una lista"""
    user_dict = [{"Nickname": values['-NICK-'], "Edad": values['-EDAD-'], "Genero": values['-GENERO-']}]
    with open(getting_path(), 'w') as users:
        # Agrego la lista al json
        json.dump(user_dict, users, indent=4)


def create_new_user(values):
    """Recibo los valores del usuario nuevo y lo almaceno en un diccionario"""
    new_user = {"Nickname": values['-NICK-'], "Edad": values['-EDAD-'], "Genero": values['-GENERO-']}
    with open(getting_path(), 'r') as users:
        # Cargo el json
        users_list = json.load(users)
    # Y lo agrego a la lista de dicciorios que hay en el json
    users_list.append(new_user)
    with open(getting_path(), 'w') as users:
        # Actualizo el contenido del json
        json.dump(users_list, users, indent=4)


def modify_user(values):
    with open(getting_path(), 'r') as users:
        # Abro el json
        users_list = json.load(users)
    for elem in users_list:
        # Obtengo la ubicaion de la lista del usuario que deseo modificar
        if elem['Nickname'] == values['-NICK-']:
            # Una vez que lo encuentro reemplazo el contenido con el nuevo
            elem['Edad'] = values['-EDAD-']
            elem['Genero'] = values['-GENERO-']
            break
    with open(getting_path(), 'w') as users:
        # Actualizo el contenido del json con la lista modificada
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
        # Verifico si existe el usuario si no se cumple la excepcion anterior
        found = False
        for user in users:
            if values['-NICK-'] == user['Nickname']:
                found = True
                break
        if found:
            # Si encuentro el usuario lo modifico
            modify_user(values)
        else:
            # Sino lo genero y lo inserto en el json
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
    gen_font = 'Verdana', 12

    # Creacion de LayOut
    layout = [
        [sg.Text('Creacion/Edicion de perfil', pad=(41, 0), font=('Any 25'))],
        [sg.Text("Nickname", pad=padding_text, font=gen_font), sg.Input(key='-NICK-', size=size_input)],
        [sg.Text("Género", pad=padding_text, font=gen_font), sg.Combo(generos, pad=(26, 0), size=(10, 1), key='-GENERO-')],
        [sg.Text("Edad", pad=padding_text, font=gen_font),
         sg.Spin([i for i in range(1, 110)], initial_value=0, size=(5, 1), key='-EDAD-', pad=(44, 0))],
        [sg.VPush()],
        [sg.Button('Volver', font=gen_font, border_width=2, size=size_button, button_color=('black', 'white'),
                   pad=spc_btw_button, key='-VOLVER-'),
         sg.Button('Borrar', font=gen_font, border_width=2, size=size_button, button_color=('black', 'white'),
                   pad=spc_btw_button, key='-BORRAR-'),
         sg.Button('Aceptar', font=gen_font, border_width=2, size=size_button, pad=spc_btw_button, key='-ACEPTAR-')]
    ]
    window = sg.Window("FiguRace *-* Perfiles", layout, resizable=False, margins=(20, 20), size=(600, 200),
                       auto_size_buttons=True)
    while True:
        # Inicio la ventana
        event, values = window.read()
        if event == '-ACEPTAR-':
            # Verifico que los campos no esten vacios.
            if (values['-NICK-'] == '' or values['-EDAD-'] == 0 or values['-GENERO-'] == ''):
                sg.popup('Por favor complete todos los campos', title='Error')
            else:
                # Verifico que no sea el valor predeterminado
                if (values['-NICK-'] == 'Usuarios'):
                    sg.popup('Nickname invalido', title='Error')
                    window['-NICK-'].update('')
                else:
                    # Verifico si el genero es valido ya que se puedes escribir en esa casilla
                    if values['-GENERO-'] in generos:
                        check_profile(values)
                        sg.popup('Perfil creado/modificado con exito')
                    else:
                        sg.popup('Por favor seleccione un genero valido', title='Error')
                        window['-GENERO-'].update('')
        elif event == '-BORRAR-':
            # Actualizo el contenido de todos los espacios para que no contengan nada.
            window['-NICK-'].update('')
            window['-EDAD-'].update(0)
            window['-GENERO-'].update('')
        elif event == '-VOLVER-':
            window.close()
            break
        elif event == sg.WIN_CLOSED:
            break
