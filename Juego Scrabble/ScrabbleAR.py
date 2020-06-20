import PySimpleGUI as sg
import json
import NivelFacil
import NivelNormal
import NivelDificil
import os 


sg.theme('DarkBlue')

Instrucciones = open('instrucciones.txt', 'r', encoding='utf8')
Instrucciones=Instrucciones.read()

reglas=open('reglas.txt', 'r', encoding='utf8')
reglas=reglas.read()
ReglasJuego=r'./Reglas_De_Juego.png'
imagen_Salir=r'./Salir.png'
imagen_Facil=r'./Facil.png'
imagen_Normal=r'./Normal.png'
imagen_Dificil=r'./Dificil.png'
imagen_Juego=r'./Jugar.png'
Salir=' '
Reglas_Juego='  '
Facil='   '
Normal='    '
Dificil='     '
Jugar='      '

boton_facil=lambda name:sg.popup_no_buttons(name,no_titlebar=True,text_color='#71B8A8',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='Black')
boton_normal=lambda name:sg.popup_no_buttons(name,no_titlebar=True,text_color='#71B8A8',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='Black')
boton_dificil=lambda name:sg.popup_no_buttons(name,no_titlebar=True,text_color='#71B8A8',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='Black')

layout=[[sg.Text('                                                                                                                       ')]+[sg.Button(button_text=Salir,pad=(1,1),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=imagen_Salir,border_width=0)],     
        [sg.Image(r'./AleScrabble500x278Recortado.png',pad=((27),1))],
        #[sg.Text('¡Bienvenidos a ScrabbleAR!', size=(30, 1), justification='center', font=('Helvetica', 22))],   
        [sg.Text(Instrucciones,text_color=('#D8C99B'),justification=('center'))],
        [sg.Button(button_text=Reglas_Juego,pad=(201,8),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=ReglasJuego,border_width=0)],
        [sg.Text('Nombre de jugador',text_color=('#D8C99B'),size=(17, 1), font=("Courier New", 20)),sg.Input(key='nombre',background_color='Black',size=(29,1))],
        [sg.Text('Dificultad',text_color=('#D8C99B'),size=(17, 1), font=("Courier New", 20))]+[sg.Button(button_text=Facil,pad=(1,7),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=imagen_Facil,border_width=0)]+[sg.Button(button_text=Normal,pad=(1,7),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=imagen_Normal,border_width=0)]+[sg.Button(button_text=Dificil,pad=(1,7),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=imagen_Dificil,border_width=0)],          
        [sg.Button(button_text=Jugar,pad=(119,15),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=imagen_Juego,border_width=0)]]
        
window= sg.Window('Juego ScrabbleAR',layout,icon=True,grab_anywhere=True,border_depth=(5),no_titlebar=True)

while True:
    event, values = window.read()
    if event in (None, Salir):
         break
    if event in ('_'):
         window.Minimize()    
    if event == Reglas_Juego:
        sg.popup_scrolled(reglas,title=' ',text_color='#BFA558',background_color='Black',font=("Calibri", 14),no_titlebar=True,size=(100,20))
    if event == Facil:
        boton_facil('¡JUGABILIDAD FÁCIL CARGADA!')
        jugada='FÁCIL'
    if event == Normal:
        boton_normal('¡JUGABILIDAD NORMAL CARGADA!')
        jugada='NORMAL'
    if event == Dificil:
        boton_dificil('¡Jugabilidad dificil cargada!')
        jugada='DIFÍCIL'
    if event == Jugar:
        try:
            if jugada == 'FÁCIL':
                NivelFacil.main(values['nombre'])         
            else:
                if jugada=='NORMAL':
                    NivelNormal.main(values['nombre'])
                else:
                    if jugada=='DIFÍCIL':
                        NivelDificil.main(values['nombre'])
        except:
            sg.popup('No has elegido la dificultad',no_titlebar=True,font=("Calibri", 15,'bold'),custom_text=("          OK          "),background_color='black',text_color='#D8C99B',button_color=('#1A2835','#D8973C'))
window.close()
