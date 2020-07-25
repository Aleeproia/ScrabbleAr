import PySimpleGUI as sg
import json
import NivelFacil
import NivelNormal
import NivelDificil
import CargarPartida

sg.theme('DarkBlue')

Instrucciones = open('./txts/instrucciones.txt', 'r', encoding='utf8')
Instrucciones = Instrucciones.read()
reglas = open('./txts/reglas.txt', 'r', encoding='utf8')
reglas = reglas.read()
ReglasJuego = r'./Images/Reglas_De_Juego.png'
imagen_Salir = r'./Images/Salir.png'
imagen_Facil = r'./Images/Facil.png'
imagen_Normal = r'./Images/Normal.png'
imagen_Dificil = r'./Images/Dificil.png'
imagen_Juego = r'./Images/Jugar.png'
imagen_Adjetivos = r'./Images/Adjetivos.png'
imagen_Verbos = r'./Images/Verbos.png'
imagen_Sustantivos = r'./Images/Sustantivos.png'
imagen_CargarPartida = r'./Images/Cargar_Partida.png'
imagen_5minutos = r'./Images/5min.png'
imagen_7minutos = r'./Images/7min.png'
imagen_10minutos = r'./Images/10min.png'
Salir = ' '
Reglas_Juego = '  '
Facil = '   '
Normal = '    '
Dificil = '     '
Jugar = '      '
Adjetivos = '       '
Verbos = '        '
Sustantivos = '         '
Cargar_Partida = '          '
Cinco_Minutos = '           '
Siete_Minutos = '            '
Diez_Minutos = '             '


def boton_facil(name): return sg.popup_no_buttons(name, no_titlebar=True, text_color='#71B8A8',
                                                  auto_close=True, auto_close_duration=1, font=("Courier New", 20, 'bold'), background_color='Black')


def boton_normal(name): return sg.popup_no_buttons(name, no_titlebar=True, text_color='#71B8A8',
                                                   auto_close=True, auto_close_duration=1, font=("Courier New", 20, 'bold'), background_color='Black')


def boton_dificil(name): return sg.popup_no_buttons(name, no_titlebar=True, text_color='#71B8A8',
                                                    auto_close=True, auto_close_duration=1, font=("Courier New", 20, 'bold'), background_color='Black')


layout_dif = [[sg.Text('Modo de juego', text_color=('#D8C99B'), size=(17, 1), font=("Courier New", 10))],
              [sg.Button(button_text=Adjetivos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Adjetivos, key='Adjetivos', border_width=0)]+[sg.Button(button_text=Verbos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Verbos, key='Verbos', border_width=0)]+[sg.Button(button_text=Sustantivos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Sustantivos, key='Sustantivos', border_width=0)]]


layout_t = [[sg.Text('Tiempo de juego', text_color=('#D8C99B'), size=(17, 1), font=("Courier New", 10))],
            [sg.Button(button_text=Cinco_Minutos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_5minutos, key='5 minutos', border_width=0)]+[sg.Button(button_text=Siete_Minutos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_7minutos, key='7 minutos', border_width=0)]+[sg.Button(button_text=Diez_Minutos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_10minutos, key='10 minutos', border_width=0)]]

layout = [[sg.Text('                                                                                                                             ')]+[sg.Button(button_text=Salir, pad=(1, 1), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Salir, border_width=0)],
          [sg.Image(r'./AleScrabble500x278Recortado.png', pad=((27), 1))],
          [sg.Text(Instrucciones, text_color=(
              '#D8C99B'), justification=('center'))],
          [sg.Button(button_text=Reglas_Juego, pad=(201, 8), button_color=(sg.theme_background_color(
          ), sg.theme_background_color()), image_filename=ReglasJuego, border_width=0)],
          [sg.Text('Nombre de jugador', text_color=('#D8C99B'), size=(17, 1), font=(
              "Courier New", 20)), sg.Input(key='nombre', background_color='Black', size=(29, 1))],
          [sg.Text('Dificultad', text_color=('#D8C99B'), size=(17, 1), font=("Courier New", 20))]+[sg.Button(button_text=Facil, key='Facil', pad=(1, 7), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Facil, border_width=0)]+[sg.Button(button_text=Normal, key='Normal',
                                                                                                                                                                                                                                                                                           pad=(1, 7), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Normal, border_width=0)]+[sg.Button(button_text=Dificil, key='Dificil', pad=(1, 7), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Dificil, border_width=0)],
          [sg.Button(button_text=Jugar, pad=(50, 15), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Juego, border_width=0)]+[sg.Button(button_text=Cargar_Partida, pad=(0, 7), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_CargarPartida, border_width=0)]]

window = sg.Window('Juego ScrabbleAR', layout, icon=True,
                   grab_anywhere=True, border_depth=(5), no_titlebar=True)

while True:
    event, values = window.read()
    if event in (None, Salir):
        break
    if event in ('_'):
        window.Minimize()
    if event == Reglas_Juego:
        sg.popup_scrolled(reglas, title=' ', text_color='#BFA558', background_color='Black', font=(
            "Calibri", 14), no_titlebar=True, size=(100, 20))
    if event == 'Facil':
        jugada = 'FACIL'
        boton_facil('¡JUGABILIDAD FÁCIL CARGADA!')
    if event == 'Normal':
        boton_normal('¡JUGABILIDAD NORMAL CARGADA!')
        jugada = 'NORMAL'
    if event == 'Dificil':
        window2 = sg.Window('elegir modo de juego', layout_dif,
                            border_depth=(5), no_titlebar=True)
        event_d, values_d = window2.read()
        boton_dificil('¡Jugabilidad dificil cargada!')
        if event_d == 'Adjetivos':
         eleccion = 'JJ'
        elif event_d == 'Sustantivos':
         eleccion = 'NN'
        else:
         eleccion = 'VB'
        jugada = 'DIFÍCIL'
        window2.close()
    if event == Jugar:
       if values['nombre'] == '':
           sg.popup('Por favor ingrese su nombre', no_titlebar=True, font=("Calibri", 15, 'bold'), custom_text=(
               "          OK          "), background_color='#1a2835', text_color='#D8C99B', button_color=('#1A2835', '#D8973C'))
       else:
         try:
             if jugada == 'FACIL':
                 window3 = sg.Window('elegir tiempo de juego',
                                     layout_t, border_depth=(5), no_titlebar=True)
                 event_t, values_t = window3.read()
                 tiempo = event_t
                 NivelFacil.main(values['nombre'], tiempo)
             elif jugada == 'NORMAL':
                 window3 = sg.Window('elegir tiempo de juego',
                                     layout_t, border_depth=(5), no_titlebar=True)
                 event_t, values_t = window3.read()
                 tiempo = event_t
                 NivelNormal.main(values['nombre'], tiempo)
             elif jugada == 'DIFÍCIL':
                 window3 = sg.Window('elegir tiempo de juego',
                                     layout_t, border_depth=(5), no_titlebar=True)
                 event_t, values_t = window3.read()
                 tiempo = event_t
                 window3.close()
                 NivelDificil.main(values['nombre'], tiempo, eleccion)
         except NameError:
             sg.popup('No has elegido la dificultad', no_titlebar=True, font=("Calibri", 15, 'bold'), custom_text=(
                 "          OK          "), background_color='#1a2835', text_color='#D8C99B', button_color=('#1A2835', '#D8973C'))
    if event == Cargar_Partida:
        try:
         Partida_Guardada = './txts/Partida Guardada.txt'
         with open(Partida_Guardada, 'r') as f:
             Datos_guardados = json.load(f)
         CargarPartida.main(Datos_guardados)
        except FileNotFoundError:
           sg.popup('No hay partida guardada', no_titlebar=True, font=("Calibri", 15, 'bold'), custom_text=(
               "          OK          "), background_color='#1a2835', text_color='#D8C99B', button_color=('#1A2835', '#D8973C'))
window.close()

