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
config=False
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
imagen_configuracion=r'./Images/Configuracion.png'
imagen_GuardarConfig=r'./Images/Guardar_Config.png'
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
Configuracion='              '
Guardar_Config='               '

def slider_puntaje(valor_porDefecto, clave): 
    return sg.Slider(range=(1,10),orientation='h',key=clave,default_value=valor_porDefecto,enable_events=True,size=(5,15),text_color=('#D8C99B'))

def slider_cantidad(valor_porDefecto, clave):
    return sg.Slider(range=(1,15), orientation='h',key=clave,default_value=valor_porDefecto,enable_events=True,size=(5,15),text_color=('#D8C99B'))

def boton_facil(name): return sg.popup_no_buttons(name, no_titlebar=True, text_color='#71B8A8',
                                                  auto_close=True, auto_close_duration=1, font=("Courier New", 20, 'bold'), background_color='Black')


def boton_normal(name): return sg.popup_no_buttons(name, no_titlebar=True, text_color='#71B8A8',
                                                   auto_close=True, auto_close_duration=1, font=("Courier New", 20, 'bold'), background_color='Black')


def boton_dificil(name): return sg.popup_no_buttons(name, no_titlebar=True, text_color='#71B8A8',
                                                    auto_close=True, auto_close_duration=1, font=("Courier New", 20, 'bold'), background_color='Black')

#-------------------------layout de eleccion de tipos de palabra--------------------------------
layout_dif = [[sg.Text('Modo de juego', text_color=('#D8C99B'), size=(17, 1), font=("Courier New", 10))],
              [sg.Button(button_text=Adjetivos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Adjetivos, key='Adjetivos', border_width=0)]+[sg.Button(button_text=Verbos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Verbos, key='Verbos', border_width=0)]+[sg.Button(button_text=Sustantivos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Sustantivos, key='Sustantivos', border_width=0)]]

#-------------------------layout de configuracion para el usuario--------------------------------
layout_c = [[sg.Text('Configuracion Letras', text_color=('#D8C99B'))],
            [sg.Text('Puntaje slider izquierdo, cantidad slider derecho', text_color=('#D8C99B'))],
            [sg.Text('A: ', text_color=('#D8C99B'))]+[slider_puntaje(1,'AP')]+[slider_cantidad(11,'AC')]+[sg.Text('B: ',text_color=('#D8C99B'))]+[slider_puntaje(3,'BP')]+[slider_cantidad(3,'BC')]+[sg.Text('C: ',text_color=('#D8C99B'))]+[slider_puntaje(2,'CP')]+[slider_cantidad(4,'CC')],
            [sg.Text('D: ',text_color=('#D8C99B'))]+[slider_puntaje(2,'DP')]+[slider_cantidad(4,'DC')]+[sg.Text('E: ',text_color=('#D8C99B'))]+[slider_puntaje(1,'EP')]+[slider_cantidad(11,'EC')]+[sg.Text('F: ',text_color=('#D8C99B'))]+[slider_puntaje(4,'FP')]+[slider_cantidad(2,'FC')],
            [sg.Text('G: ',text_color=('#D8C99B'))]+[slider_puntaje(2,'GP')]+[slider_cantidad(2,'GC')]+[sg.Text('H: ',text_color=('#D8C99B'))]+[slider_puntaje(4,'HP')]+[slider_cantidad(2,'HC')]+[sg.Text('I: ',text_color=('#D8C99B'))]+[slider_puntaje(1,'IP')]+[slider_cantidad(11,'IC')],
            [sg.Text('J: ',text_color=('#D8C99B'))]+[slider_puntaje(6,'JP')]+[slider_cantidad(2,'JC')]+[sg.Text('K: ',text_color=('#D8C99B'))]+[slider_puntaje(8,'KP')]+[slider_cantidad(1,'KC')]+[sg.Text('L: ',text_color=('#D8C99B'))]+[slider_puntaje(6,'LP')]+[slider_cantidad(2,'LC')],
            [sg.Text('M: ',text_color=('#D8C99B'))]+[slider_puntaje(3,'MP')]+[slider_cantidad(3,'MC')]+[sg.Text('N: ',text_color=('#D8C99B'))]+[slider_puntaje(1,'NP')]+[slider_cantidad(6,'NC')]+[sg.Text('Ñ: ',text_color=('#D8C99B'))]+[slider_puntaje(6,'ÑP')]+[slider_cantidad(3,'ÑC')],
            [sg.Text('O: ',text_color=('#D8C99B'))]+[slider_puntaje(1,'OP')]+[slider_cantidad(8,'OC')]+[sg.Text('P: ',text_color=('#D8C99B'))]+[slider_puntaje(3,'PP')]+[slider_cantidad(2,'PC')]+[sg.Text('Q: ',text_color=('#D8C99B'))]+[slider_puntaje(8,'QP')]+[slider_cantidad(1,'QC')],
            [sg.Text('R: ',text_color=('#D8C99B'))]+[slider_puntaje(6,'RP')]+[slider_cantidad(2,'RC')]+[sg.Text('S: ',text_color=('#D8C99B'))]+[slider_puntaje(1,'SP')]+[slider_cantidad(7,'SC')]+[sg.Text('T: ',text_color=('#D8C99B'))]+[slider_puntaje(1,'TP')]+[slider_cantidad(4,'TC')],
            [sg.Text('U: ',text_color=('#D8C99B'))]+[slider_puntaje(6,'UP')]+[slider_cantidad(2,'UC')]+[sg.Text('V: ',text_color=('#D8C99B'))]+[slider_puntaje(4,'VP')]+[slider_cantidad(2,'VC')]+[sg.Text('W: ',text_color=('#D8C99B'))]+[slider_puntaje(8,'WP')]+[slider_cantidad(2,'WC')],
            [sg.Text('X: ',text_color=('#D8C99B'))]+[slider_puntaje(6,'XP')]+[slider_cantidad(2,'XC')]+[sg.Text('Y: ',text_color=('#D8C99B'))]+[slider_puntaje(4,'YP')]+[slider_cantidad(2,'YC')]+[sg.Text('Z: ',text_color=('#D8C99B'))]+[slider_puntaje(10,'ZP')]+[slider_cantidad(1,'ZC')],
            [sg.Text('Tiempo de juego', text_color=('#D8C99B'), size=(17, 1), font=("Courier New", 10))],
            [sg.Button(button_text=Cinco_Minutos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_5minutos, key='05:00', border_width=0)]+[sg.Button(button_text=Siete_Minutos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_7minutos, key='07:00', border_width=0)]+[sg.Button(button_text=Diez_Minutos, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_10minutos, key='10:00', border_width=0)],
            [sg.Text('                ')]+[sg.Button(button_text=Guardar_Config,pad=(5,8),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=imagen_GuardarConfig,border_width=0)]]

#-------------------------layout de pantalla principal--------------------------------
layout = [[sg.Text('                                                                                                                             ')]+[sg.Button(button_text=Salir, pad=(1,1), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_Salir, border_width=0)],
          [sg.Image(r'./AleScrabble500x278Recortado.png', pad=((27), 1))],
          [sg.Text(Instrucciones, text_color=(
              '#D8C99B'), justification=('center'))],
          [sg.Button(button_text=Reglas_Juego, pad=(70, 8), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=ReglasJuego, border_width=0)]+[sg.Button(button_text=Configuracion, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=imagen_configuracion, border_width=0)],
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
    if event == Reglas_Juego:
        sg.popup_scrolled(reglas, title=' ', text_color='#D8C99B', background_color='#1A2835', font=(
            "Calibri", 14), no_titlebar=True, size=(100, 20))
    if event == Configuracion:
      window3 = sg.Window('elegir tiempo de juego',layout_c, border_depth=(5), no_titlebar=True)
      while True:
            event_c, values_c = window3.read()
            tiempo = event_c
            Letras={'A':[values_c['AP'],values_c['AC']],'B':[values_c['BP'],values_c['BC']],'C':[values_c['CP'],values_c['CC']],'D':[values_c['DP'],values_c['DC']],'E':[values_c['EP'],values_c['EC']],'F':[values_c['EP'],values_c['EC']],'G':[values_c['GP'],values_c['GC']],
                    'H':[values_c['HP'],values_c['HC']],'I':[values_c['IP'],values_c['IC']],'J':[values_c['JP'],values_c['JC']],'K':[values_c['KP'],values_c['KC']],'L':[values_c['LP'],values_c['LC']],'M':[values_c['MP'],values_c['MC']],'N':[values_c['NP'],values_c['NC']],'Ñ':[values_c['ÑP'],values_c['ÑC']],'O':[values_c['OP'],values_c['OC']],'P':[values_c['PP'],values_c['PC']],
                    'Q':[values_c['QP'],values_c['QC']],'R':[values_c['RP'],values_c['RC']],'S':[values_c['SP'],values_c['SC']],'T':[values_c['TP'],values_c['TC']],'U':[values_c['UP'],values_c['UC']],'V':[values_c['VP'],values_c['VC']],'W':[values_c['WP'],values_c['WC']],'X':[values_c['XP'],values_c['XC']],'Y':[values_c['YP'],values_c['YC']],'Z':[values_c['ZP'],values_c['ZC']]}
            if event_c == Guardar_Config:
             sg.popup_no_buttons('Configuracion Guardada!',no_titlebar=True,text_color='#D8C99B',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='#1a2835')
             config=True
             break
      window3.close()
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
       elif config == False:
           sg.popup('Por favor configure el juego', no_titlebar=True, font=("Calibri", 15, 'bold'), custom_text=(
               "          OK          "), background_color='#1a2835', text_color='#D8C99B', button_color=('#1A2835', '#D8973C'))      
       else:
         try:
             if jugada == 'FACIL':
                 NivelFacil.main(values['nombre'], tiempo,Letras)
             elif jugada == 'NORMAL':
                 NivelNormal.main(values['nombre'], tiempo,Letras)
             elif jugada == 'DIFÍCIL':
                 NivelDificil.main(values['nombre'], tiempo,eleccion,Letras)
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

