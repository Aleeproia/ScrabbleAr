from Funciones import *
from Maquina import *
def main(nombre,tiempo, Letras):
    import  PySimpleGUI as sg
    import time
    import random
    sg.theme('DarkBlue')

    letras_totales=contar_letras(Letras)
    lista_puntajes=[]
    for l in Letras.keys():
        lista_puntajes.append(l+': '+ str(Letras[l][0]))
    
    #-------------------------config atril jugador--------------------------------
    atril=dar_letras(Letras,7)
    letras_totales=letras_totales-7
    BotonAtril=r'./Images/Boton_Atril.png'
    A1=sg.Button(atril[0],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A1',pad=(6,1))
    A2=sg.Button(atril[1],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A2',pad=(6,1))
    A3=sg.Button(atril[2],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A3',pad=(6,1))
    A4=sg.Button(atril[3],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A4',pad=(6,1))
    A5=sg.Button(atril[4],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A5',pad=(6,1))
    A6=sg.Button(atril[5],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A6',pad=(6,1))
    A7=sg.Button(atril[6],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A7',pad=(6,1))
    atril_k=['A1','A2','A3','A4','A5','A6','A7']

    #--------------------------config atril maquina---------------------------------
    atril_m=dar_letras(Letras,7)
    letras_totales=letras_totales-7
    BotonAtrilNegro=r'./Images/Boton_Atril_Negro.png'
    Letra_M=r'./Images/Letra_M.png'
    Letra_A=r'./Images/Letra_A.png'
    Letra_Q=r'./Images/Letra_Q.png'
    Letra_U=r'./Images/Letra_U.png'
    Letra_i=r'./Images/Letra_i.png'
    Letra_N=r'./Images/Letra_N.png'
    BM1=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_M,border_width=0,pad=(7,1))
    BM2=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_A,border_width=0,pad=(7,1))
    BM3=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_Q,border_width=0,pad=(7,1))
    BM4=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_U,border_width=0,pad=(7,1))
    BM5=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_i,border_width=0,pad=(7,1))
    BM6=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_N,border_width=0,pad=(7,1))
    BM7=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_A,border_width=0,pad=(7,1))

    #--------------------------config general/declaracion de var---------------------------------
    puntaje_j=0
    puntaje_c=0    
    cant_cambios=0
    turno=random.randrange(0,1)
    palabra='' 
    coordenadas=[]
    key_letras=[]
    coor_rojos=[]
    coor_celeste=[] 
    coor_azul=[]
    coor_naranja=[]
    Tablero=[] 
    tiempo_juego=True
    coor_y=False
    coor_x=False
    Check_button = lambda x: window.FindElement(x).Update(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtrilNegro)
    Uncheck_button = lambda x: window.FindElement(x).Update(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtril)
    top_10jugadores=leer_top()

    #--------------------------config layouts---------------------------------
        #declaro botones
    TERMINAR=r'./Images/TERMINAR.png'
    COMPROBAR=r'./Images/COMPROBAR.png'
    Guardar_Partida=r'./Images/Guardar_Partida.png'
    Cambiar_Turno=r'./Images/Cambiar_Turno.png'
    Cambiar_Fichas=r'./Images/Cambiar_Fichas.png'
    COMENZAR=r'./Images/Comenzar.png'
    GuardarPartida=' '
    Terminar='  '
    CAMBIARFICHAS='   '
    Comprobar='    '
    CAMBIARTURNO='     '
    Comenzar='      '

    Botones_Tablero= lambda name : sg.Button(name,button_color=('#12947f','#12947f'),size=(3,1),pad=((0),0),border_width=(2),key=name)

    puntajes=[[sg.Text('PUNTAJE COMPUTADORA',text_color=('#D8C99B'),size=(19,1), font=("Courier New", 12))],
              [sg.Text('{}'.format(str(puntaje_c)),size=(16,5),font=("Helvetica"),key=('puntaje_c'))],
              [sg.Text('PUNTAJE {}'.format(nombre.upper()),text_color=('#D8C99B'),font=("Courier New",12))],
              [sg.Text('{}'.format(str(puntaje_j)),size=(16,5),font=("Helvetica"),key=('puntaje_j'))],
              [sg.Text('VALOR POR LETRA',text_color=('#D8C99B'),size=(16,1),font=("Courier New", 15))],
              [sg.Listbox(lista_puntajes,pad=(5,5),size=(15,10), no_scrollbar=True, text_color=('#D8C99B'))]]

    top10=[[sg.Text('TOP 10 JUGADORES',text_color=('#D8C99B'),justification='center',size=(16,1),font=("Courier New", 15))],
           [sg.Listbox(top_10jugadores,pad=(5,5),size=(28,12), no_scrollbar=True, text_color=('#D8C99B'))],
           [sg.Button(button_text=GuardarPartida,pad=(18,8),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Guardar_Partida,border_width=0)],
           [sg.Button(button_text=Terminar,size=(15,1),pad=(50,5), button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=TERMINAR,border_width=0)],
           [sg.Text('   TIEMPO',text_color=('#D8C99B'),justification='right',size=(12,1),font=("Courier New", 12))],
           [sg.Text('       ')]+[sg.Text(' ',text_color=('#D8C99B'), size=(8, 2), font=('Courier New', 12), justification='right', key='time')],
           [sg.Text('  TURNO',text_color=('#D8C99B'),justification='right',size=(12,1),font=("Courier New", 12))],
           [sg.Text('   ',text_color=('#D8C99B'),justification='right',size=(12,1),font=("Courier New", 12),key='turno')]]

    layout = [[sg.Image(r'./Images/AleScrabble3.png',pad=((5),1))]+[(BM1),(BM2),(BM3),(BM4),(BM5),(BM6),(BM7)]+[sg.Image(r'./Images/AleScrabble3.png',pad=((1),1))],
             [sg.Column(puntajes),sg.Frame(layout=[[Botones_Tablero((col,fila))for col in range(15)] for fila in range(15)],border_width=(20),title='',pad=(0,7), relief=sg.RELIEF_SUNKEN,background_color=('#D8973C')),sg.Column(top10)],
             [sg.Text('{}'.format(nombre.upper()),text_color='#D8C99B',font=("Courier New", 20))]+[sg.Text('                    '),A1,A2,A3,A4,A5,A6,A7],
             [sg.Text('                                        ')]+[sg.Button(button_text=Comenzar,pad=(5,8),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=COMENZAR,border_width=0)]+[sg.Button(button_text=Comprobar,pad=(5,8),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=COMPROBAR,border_width=0)]+[sg.Button(button_text=CAMBIARTURNO, button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Cambiar_Turno,border_width=0)]+[sg.Button(button_text=CAMBIARFICHAS,button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Cambiar_Fichas,border_width=0)]]

   
    
    window = sg.Window('ScrabbleAr',no_titlebar=True).Layout(layout).Finalize()

    #--------------------------config tablero premios y descuentos---------------------------------
    for i in range(15):
        for j in range(15): 
            Tablero.append((i,j))
            if((i==0)&(j==0))|((i==14)&(j==0))|((i==0)&(j==14))|((i==14)&(j==14))|((i==7)&(j==0))|((i==7)&(j==14))|((i==0)&(j==7))|((i==14)&(j==7)):
                window.find_element((i,j)).update(button_color=('black','#C34C47'),text='Px2')
                coor_rojos.append((i,j))
            if((i==3)&(j==0))|((i==11)&(j==0))|((i==6)&(j==2))|((i==8)&(j==2))|((i==0)&(j==3))|((i==7)&(j==3))|((i==14)&(j==3))|((i==2)&(j==6))|((i==6)&(j==6))|((i==8)&(j==6))|((i==12)&(j==6))|((i==3)&(j==7))|((i==11)&(j==7))|((i==2)&(j==8))|((i==6)&(j==8))|((i==8)&(j==8))|((i==12)&(j==8))|((i==0)&(j==11))|((i==7)&(j==11))|((i==14)&(j==11))|((i==6)&(j==12))|((i==8)&(j==12))|((i==3)&(j==14))|((i==11)&(j==14)):
                window.find_element((i,j)).update(button_color=('black','#98d6ea'),text='P-2')#c
                coor_celeste.append((i,j))
            if((i==5)&(j==1))|((i==9)&(j==1))|((i==1)&(j==5))|((i==5)&(j==5))|((i==9)&(j==5))|((i==13)&(j==5))|((i==1)&(j==9))|((i==5)&(j==9))|((i==9)&(j==9))|((i==13)&(j==9))|((i==5)&(j==13))|((i==9)&(j==13)):
                window.find_element((i,j)).update(button_color=('black','#2A9AAD'), text='Lx3')#a
                coor_azul.append((i,j))
            if((i==1)&(j==1))|((i==2)&(j==2))|((i==3)&(j==3))|((i==4)&(j==4))|((i==13)&(j==1))|((i==12)&(j==2))|((i==11)&(j==3))|((i==10)&(j==4))|((i==7)&(j==7))|((i==1)&(j==13))|((i==2)&(j==12))|((i==3)&(j==11))|((i==4)&(j==10))|((i==13)&(j==13))|((i==12)&(j==12))|((i==11)&(j==11))|((i==10)&(j==10)):
                window.find_element((i,j)).update(button_color=('black','#ffb385'),text='P-3')#n
                coor_naranja.append((i,j))
   
    #--------------------------config jugabilidad---------------------------------
    while True:
        event, values = window.read(timeout=10)
        if event in (None,Terminar):
            break
        start_time = int(round(time.time() * 100))
        if event == Comenzar:
          while tiempo_juego and letras_totales > 7:
                event, values = window.read(timeout=10)
                current_time = int(round(time.time() * 100)) - start_time
                window['time'].update('{:02d}:{:02d}'.format((current_time//100) // 60, (current_time // 100) % 60))
                
                tiempo_jugada = '{:02d}:{:02d}'.format((current_time//100) // 60,(current_time // 100) % 60)
                if tiempo_jugada==tiempo:
                 tiempo_juego=False
                if event in (None,Terminar):
                    tiempo_juego=False
                if turno== 1:
                    window.find_element('turno').update('{}'.format(nombre.upper()))
                    if event in atril_k:
                            Check_button(event)
                            letra_key=event
                            palabra+=window.find_element(letra_key).get_text()
                            ultima_letra=window.find_element(letra_key).get_text()
                            key_letras.append(event)
                            event,values=window.read()
                            if event in Tablero and len(palabra)==1 and (window.find_element(event).get_text() not in Letras.keys()):
                                coordenadas.append(event)
                                window[event].update(window.find_element(letra_key).get_text(), button_color=('Black','#D8C99B'))
                                window[letra_key].update(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtrilNegro)
                            elif event in atril_k:
                                Uncheck_button(event)
                            else:#codigo que comprueba que las letras siguientes a la primera no sean en diagonal y que una vez puesta la segunda letra sigan el mismo orden (horizontal o vertical)
                                if event in Tablero and len(palabra)>1 and (window.find_element(event).get_text() not in Letras.keys()): 
                                    coordenada=coordenadas[len(palabra)-2]
                                    if (event[0] == (coordenada[0]+1))and(event[1] == coordenada[1]) and len(palabra)==2 and (window.find_element(event).get_text() not in Letras.keys()):
                                        coor_y=True #pone en true para verificar que la palabra es en vertical
                                        coordenadas.append(event)
                                        window[event].update(window.find_element(letra_key).get_text(), button_color=('Black','#D8C99B'),)
                                        window[letra_key].update(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtrilNegro)
                                    elif (event[0]==coordenada[0]) and(event[1] == (coordenada[1]+1)) and len(palabra)==2 and (window.find_element(event).get_text() not in Letras.keys()):
                                        coor_x=True #pone en true para verificar que la palabra es en horizontal
                                        coordenadas.append(event)
                                        window[event].update(window.find_element(letra_key).get_text(), button_color=('Black','#D8C99B'),)
                                        window[letra_key].update(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtrilNegro)
                                    elif (event[0]==(coordenada[0]+1)) and(event[1] == (coordenada[1]+1)) and len(palabra)==2 and (window.find_element(event).get_text() in Letras.keys()):
                                        palabra=movimiento_incorrecto(window,palabra,ultima_letra,key_letras,BotonAtril)
                                    else:
                                        if coor_y:
                                            if (event[1] == coordenada[1]) and (window.find_element(event).get_text() not in Letras.keys()):
                                                coordenadas.append(event)
                                                window[event].update(window.find_element(letra_key).get_text(), button_color=('Black','#D8C99B'),)
                                                window[letra_key].update(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtrilNegro)
                                            else:
                                                palabra=movimiento_incorrecto(window,palabra,ultima_letra,key_letras,BotonAtril)
                                        elif coor_x:
                                            if(event[0]==coordenada[0]) and (window.find_element(event).get_text() not in Letras.keys()):
                                                coordenadas.append(event)
                                                window[event].update(window.find_element(letra_key).get_text(), button_color=('Black','#D8C99B'),)
                                                window[letra_key].update(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtrilNegro)
                                            else:
                                                palabra=movimiento_incorrecto(window,palabra,ultima_letra,key_letras,BotonAtril)
                    if event == Comprobar: #se comprueba si la palabra es valida, si lo es se actualiza el puntaje si no lo es se avisa y se devuelven las letras al atril
                        if len(palabra)>2 and comprobar_palabra(palabra,'Facil'):
                            puntaje_j+=comprobar_puntaje(palabra,coordenadas,Letras,coor_rojos,coor_naranja,coor_azul,coor_celeste,'Facil')
                            window.find_element('puntaje_j').update(str(puntaje_j))
                            cambiar_letras(window,key_letras,Letras,BotonAtril,'Palabra Correcta','Jugador',atril)
                            letras_totales=letras_totales-len(palabra)
                            turno=0
                        else:
                            sg.popup_no_buttons('Palabra no permitida',no_titlebar=True,text_color='#D8C99B',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='#1a2835')
                            palabra_incorrecta(window,palabra,key_letras,coor_azul,coor_celeste,coor_naranja,coor_rojos,coordenadas,'Facil',BotonAtril)     
                        puntaje_palabra=comprobar_puntaje(palabra,coordenadas,Letras,coor_rojos,coor_naranja,coor_azul,coor_celeste,'Facil')
                        puntaje_j+=puntaje_palabra
                        window['puntaje_j'].update(str(puntaje_j))
                        cambiar_letras(window,key_letras,Letras,BotonAtril,'Palabra Correcta','Jugador',atril)
                        palabra=''
                        key_letras=[]
                        coordenadas=[]
                        coor_y=False
                        coor_x=False
                    if event == CAMBIARFICHAS:
                            if (cant_cambios == 7)|(cant_cambios > 7):
                                devolver_l=0
                                sg.popup_no_buttons('Ya utilizo todos sus cambios',no_titlebar=True,text_color='#D8C99B',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='#1a2835')
                                for k in key_letras:
                                    window.find_element(k).update(text=palabra[devolver_l],button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtril)
                                    devolver_l+=1
                            else:
                                cambiar_letras(window,key_letras,Letras,BotonAtril,'Cambio Fichas','Jugador',atril)
                                palabra=''
                                key_letras=[]
                                cant_cambios+=1
                                turno=0
                    if event == CAMBIARTURNO:
                     turno=0
                    if event == GuardarPartida:
                        Tablero_Guardado=[]
                        Atril_jugador=[]
                        for t in Tablero:
                            Tablero_Guardado.append(window.find_element(t).get_text())
                        for l in atril_k:
                            Atril_jugador.append(window.find_element(l).get_text())
                        tiempo_guardado=int(round(time.time() * 100))
                        guardar_partida(nombre,'Facil',Tablero_Guardado,Atril_jugador,atril_m,Letras,letras_totales,puntaje_c,puntaje_j,'',tiempo,tiempo_guardado,start_time)
                        sg.popup_no_buttons('Partida Guardada',no_titlebar=True,text_color='#D8C99B',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='#1a2835')
                if turno == 0:        #turno maquina  
                    window.find_element('turno').update('MAQUINA')  
                    lista_palabras=generar_palabras(atril_m,'Facil','')
                    cant=0
                    if lista_palabras:
                        palabra_c=lista_palabras[random.randrange(0,len(lista_palabras))]
                        coordenadas_c=buscar_espacio(window,palabra_c,Tablero,Letras,'Facil')
                        for l in palabra_c:
                            window[coordenadas_c[cant]].update(l.upper(), button_color=('Black','#D8C99B'))
                            cant+=1
                        puntaje_c+=comprobar_puntaje(palabra_c.upper(),coordenadas_c,Letras,coor_rojos,coor_naranja,coor_azul,coor_celeste,'Facil')
                        window['puntaje_c'].update(str(puntaje_c))
                        cambiar_letras(window,palabra_c.upper(),Letras,BotonAtril,'Palabra Correcta','Computadora',atril_m)
                        letras_totales=letras_totales-len(palabra_c)
                        turno=1
                    else:
                        cant_letras=random.randrange(1,7)#si la lista devuelta por la maquina es vacia se cambian letras al azar del atril porque sino no puede funcionar
                        letras_cambio=atril_m[0:cant_letras]
                        cambiar_letras(window,letras_cambio,Letras,BotonAtril,'Cambio Fichas','Computadora',atril_m)
          sg.popup_no_buttons('Juego Terminado',no_titlebar=True,text_color='#D8C99B',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='#1a2835')
          ver_puntajeFinal(puntaje_c,puntaje_j,atril_m,atril_k,window,Letras,nombre)
          cargar_jugador(nombre,puntaje_j,'Facil')
    window.close()
