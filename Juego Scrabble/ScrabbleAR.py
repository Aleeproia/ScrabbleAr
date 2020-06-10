import PySimpleGUI as sg
import json
import NivelFacil
import NivelNormal
import NivelDificil

sg.theme('DarkBlue')

Instrucciones = open('instrucciones.txt', 'r', encoding='utf8')
Instrucciones=Instrucciones.read()

reglas=open('reglas.txt', 'r', encoding='utf8')
reglas=reglas.read()

boton_facil=lambda name:sg.popup_no_buttons(name,no_titlebar=True,text_color='#71B8A8',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='Black')
boton_normal=lambda name:sg.popup_no_buttons(name,no_titlebar=True,text_color='#71B8A8',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='Black')
boton_dificil=lambda name:sg.popup_no_buttons(name,no_titlebar=True,text_color='#71B8A8',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='Black')

layout=[[sg.Button('Salir',size=(5,1),border_width=(2),button_color=('#A4243B','#D8973C'),font=("Fixedsys",10,"bold"),pad=((2), 5))],     
        #[sg.Image(r'C:\Users\Ale\Pictures\AleScrabble500x278Recortado.png',pad=((27),1))],
        [sg.Text('¡Bienvenidos a ScrabbleAR!', size=(30, 1), justification='center', font=('Helvetica', 22))],   
        [sg.Text(Instrucciones,text_color=('#D8C99B'),justification=('center'   ))],
        [sg.Button('REGLAS DE JUEGO',size=(15,1),pad=((200),1),button_color=('#A4243B','#D8973C'),border_width=(8),font=("Fixedsys",16))],
        [sg.Text('Nombre de jugador',text_color=('#D8C99B'),size=(17, 1), font=("Courier New", 20)),sg.Input(key='nombre',background_color='Black',size=(29,1))],
        [sg.Text('Dificultad',text_color=('#D8C99B'),size=(17, 1), font=("Courier New", 20)),sg.Button('FÁCIL',button_color=('#A4243B','#D8973C'),border_width=(4),font=(("Fixedsys",16))),sg.Button('NORMAL',button_color=('#A4243B','#D8973C'),border_width=(4),font=(("Fixedsys",16))),sg.Button('DIFÍCIL',button_color=('#A4243B','#D8973C'),border_width=(4),font=(("Fixedsys",16)))],    
        [sg.Button('JUGAR',size=(15,1),font=(("Fixedsys",25,"bold")),pad=((81), 30),button_color=('#A4243B','#D8973C'),border_width=(10))]]
        
window= sg.Window('Juego ScrabbleAR',layout,no_titlebar=True,icon=True,grab_anywhere=True,)

while True:
    event, values = window.read()
    if event in (None, 'Salir'):
         break
    if event in ('_'):
         window.Minimize()    
    if event == 'REGLAS DE JUEGO':
        sg.popup_scrolled(reglas,title=' ',text_color='#BFA558',background_color='Black',font=("Calibri", 14),no_titlebar=True,size=(100,20))
    if event == 'FÁCIL':
        boton_facil('¡JUGABILIDAD FÁCIL CARGADA!')
        jugada='FÁCIL'
    if event == 'NORMAL':
        boton_normal('¡JUGABILIDAD NORMAL CARGADA!')
        jugada='NORMAL'
    if event == 'DIFÍCIL':
        boton_dificil('¡Jugabilidad dificil cargada!')
        jugada='DIFÍCIL'
    if event == 'JUGAR':
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
