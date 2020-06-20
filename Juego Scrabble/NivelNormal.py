def clasificar(palabra):
    from pattern.es import verbs, tag, spelling, lexicon
    import string

    if palabra != 'q':
     if not palabra.lower() in verbs:
         if not palabra.lower() in spelling:
             if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
                 return ('No existe esa palabra')
             else:
                 return tag(palabra, tokenize=True, encoding='utf-8') #sustantivos
         else:
             return tag(palabra, tokenize=True, encoding='utf-8') #adjetivos
     else:
         return tag(palabra, tokenize=True, encoding='utf-8') #verbos

def comprobar_palabra(palabra):
    clasificacion = clasificar(palabra)
    if clasificacion == 'No existe esa palabra':
        return False
    else: 
        if clasificacion[0][1]=='NN': #pregunta si es un sustantivo
            return False
        elif clasificacion[0][1]== 'JJ': # pregunta si es un adjetivo
            return True
        elif clasificacion[0][1]== 'VB': #pregunta si es un verbo
            return True
        else:
            return False #si la palabra no es ninguno de esos da falso ya que pattern devuelve otros tipos de palabra

def comprobar_puntaje(palabra,coordenadas,Letras,coor_rojos,coor_naranja,coor_azul,coor_celeste):
    puntaje=0
    valor_letra=0
    for l in range(0,len(palabra)):
        if coordenadas[l] in coor_azul:
            valor_letra=Letras[palabra[l].lower()][0]*2
            puntaje+=valor_letra
        if coordenadas[l] in coor_celeste:
            puntaje=puntaje-2
        if coordenadas[l] in coor_naranja:
            puntaje=puntaje-5
        if coordenadas[l] in coor_rojos:
            valor_letra=Letras[palabra[l].lower()][0]*2
            puntaje+=valor_letra
        else:
            puntaje+=Letras[palabra[l].lower()][0]
    return puntaje

def dar_letras(Letras,cant):
    import random
    lista_letras=[]
    l=[]
    for x in Letras.keys():
        l.append(x.upper())
    for a in range(cant):
        lista_letras.append(l[random.randint(0,len(l)-1)])
    return lista_letras

def cambiar_letras(window,key_letras,Letras,BotonAtril): 
    import PySimpleGUI as sg
    nuevas_letras=dar_letras(Letras,len(key_letras)) 
    cant=0
    for l in nuevas_letras:
         window.find_element(key_letras[cant]).update(text=l,button_color=('#D8C99B', sg.theme_background_color()),image_filename=BotonAtril)
         cant+=1

def leer_top():
    import json
    lista_top10=[]
    archivo='top.txt'
    with open(archivo,'r') as f:
         dicc_top10=json.load(f)
         for jugador in dicc_top10.keys():
             lista_top10.append(jugador.upper())
             datos=str(dicc_top10[jugador])
             lista_top10.append(datos.strip('{}'))

    return lista_top10

def main(nombre):
    import  PySimpleGUI as sg

    sg.theme('DarkBlue')

    top=open('top.txt', 'r', encoding='utf8')
    top=top.read()

    #El primer valor de la lista es PUNTAJE ,el segundo valor CANTIDAD
    Letras={'a':[1,11],'b':[3,3],'c':[2,4],'d':[2,4],'e':[1,11],'f':[4,2],'g':[2,2],'h':[4,2],'i':[1,6],'j':[6,2],'k':[8,1],'l':[1,4],'m':[3,3],'n':[1,6],'o':[1,8],'p':[3,2],'q':[8,1],'r':[1,4],'s':[1,7],'t':[1,4],'u':[1,6],'v':[4,2],'w':[8,2],'x':[8,2],'y':[4,2],'z':[10,1]}
    coor_rojos=[]
    coor_celeste=[] 
    coor_azul=[]
    coor_naranja=[]
    atril=dar_letras(Letras,7)
    BotonAtril=r'./Boton_Atril.png'
    BotonAtrilNegro=r'./Boton_Atril_Negro.png'
    A1=sg.Button(atril[0],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A1',pad=(6,1))
    A2=sg.Button(atril[1],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A2',pad=(6,1))
    A3=sg.Button(atril[2],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A3',pad=(6,1))
    A4=sg.Button(atril[3],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A4',pad=(6,1))
    A5=sg.Button(atril[4],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A5',pad=(6,1))
    A6=sg.Button(atril[5],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A6',pad=(6,1))
    A7=sg.Button(atril[6],button_color=('#D8C99B', sg.theme_background_color()),font=("Courier New",20),image_filename=BotonAtril,border_width=0,key='A7',pad=(6,1))
    atril_k=['A1','A2','A3','A4','A5','A6','A7']

    Letra_M=r'./Letra_M.png'
    Letra_A=r'./Letra_A.png'
    Letra_Q=r'./Letra_Q.png'
    Letra_U=r'./Letra_U.png'
    Letra_i=r'./Letra_i.png'
    Letra_N=r'./Letra_N.png'
    BM1=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_M,border_width=0,pad=(7,1))
    BM2=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_A,border_width=0,pad=(7,1))
    BM3=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_Q,border_width=0,pad=(7,1))
    BM4=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_U,border_width=0,pad=(7,1))
    BM5=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_i,border_width=0,pad=(7,1))
    BM6=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_N,border_width=0,pad=(7,1))
    BM7=sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Letra_A,border_width=0,pad=(7,1))

    puntaje_j=0
    puntaje_c=0
    TERMINAR=r'./TERMINAR.png'
    COMPROBAR=r'./COMPROBAR.png'
    Guardar_Partida=r'./Guardar_Partida.png'
    Cambiar_Turno=r'./Cambiar_Turno.png'
    Cambiar_Fichas=r'./Cambiar_Fichas.png'
    GuardarPartida=' '
    Terminar='  '
    CAMBIARFICHAS='   '
    Comprobar='    '
    CAMBIARTURNO='     '
    top_10jugadores=leer_top()

    Botones_Tablero= lambda name : sg.Button(name,button_color=('#12947f','#12947f'),size=(3,1),pad=((0),0),border_width=(2),key=name)

    puntajes=[[sg.Text('PUNTAJE COMPUTADORA',text_color=('#D8C99B'),size=(19,1), font=("Courier New", 12))],
              [sg.Text('{}'.format(str(puntaje_c)),size=(16,5),font=("Helvetica"),key=('puntaje_c'))],
              [sg.Text('PUNTAJE {}'.format(nombre.upper()),text_color=('#D8C99B'),font=("Courier New",12))],
              [sg.Text('{}'.format(str(puntaje_j)),size=(16,5),font=("Helvetica"),key=('puntaje_j'))],
              [sg.Text('VALOR POR LETRA',text_color=('#D8C99B'),size=(16,1),font=("Courier New", 15))],
              [sg.Image(r'./PuntosPorLetra.png',pad=((1),1))]]

    top10=[[sg.Text('TOP 10 JUGADORES',text_color=('#D8C99B'),justification='center',size=(16,1),font=("Courier New", 15))],
           [sg.Listbox(top_10jugadores,pad=(5,5),size=(28,12), no_scrollbar=True, text_color=('#D8C99B'))],
           [sg.Button(button_text=GuardarPartida,pad=(18,8),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Guardar_Partida,border_width=0)],
           [sg.Button(button_text=Terminar,size=(15,1),pad=(50,5), button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=TERMINAR,border_width=0)],
           [sg.Text('TIEMPO',text_color=('#D8C99B'),justification='center',size=(16,1),font=("Courier New", 15))]]

    layout = [[sg.Image(r'./AleScrabble3.png',pad=((5),1))]+[(BM1),(BM2),(BM3),(BM4),(BM5),(BM6),(BM7)]+[sg.Image(r'./AleScrabble3.png',pad=((1),1))],
             [sg.Column(puntajes),sg.Frame(layout=[[Botones_Tablero((col,fila))for col in range(15)] for fila in range(15)],border_width=(20),title='',pad=(0,7), relief=sg.RELIEF_SUNKEN,background_color=('#D8973C')),sg.Column(top10)],
             [sg.Text('{}'.format(nombre.upper()),text_color='#D8C99B',font=("Courier New", 20))]+[sg.Text('                    '),A1,A2,A3,A4,A5,A6,A7],
             [sg.Text('                                                         ')]+[sg.Button(button_text=Comprobar,pad=(5,8),button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=COMPROBAR,border_width=0)]+[sg.Button(button_text=CAMBIARTURNO, button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Cambiar_Turno,border_width=0)]+[sg.Button(button_text=CAMBIARFICHAS,button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=Cambiar_Fichas,border_width=0)]]

   
    
    window = sg.Window('ScrabbleAr',no_titlebar=True).Layout(layout).Finalize()

    Tablero=[]
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
                window.find_element((i,j)).update(button_color=('black','#2A9AAD'), text='Lx2')#a
                coor_azul.append((i,j))
            if((i==1)&(j==1))|((i==2)&(j==2))|((i==3)&(j==3))|((i==4)&(j==4))|((i==13)&(j==1))|((i==12)&(j==2))|((i==11)&(j==3))|((i==10)&(j==4))|((i==7)&(j==7))|((i==1)&(j==13))|((i==2)&(j==12))|((i==3)&(j==11))|((i==4)&(j==10))|((i==13)&(j==13))|((i==12)&(j==12))|((i==11)&(j==11))|((i==10)&(j==10)):
                window.find_element((i,j)).update(button_color=('black','#ffb385'),text='P-5')#n
                coor_naranja.append((i,j))

    palabra=''
    cant_cambios=0
    coordenadas=[]
    key_letras=[]
    
    Check_button = lambda x: window.FindElement(x).Update(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtrilNegro)
    Uncheck_button = lambda x: window.FindElement(x).Update(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtril)
  
    while True:
        event, values = window.read()
        print (event)
        if event in (None,Terminar):
            break
        if event in atril_k:
            Check_button(event)
            letra_key=event
            palabra+=window.find_element(letra_key).get_text()
            key_letras.append(event)
            event,values=window.read()
            if event in Tablero:
                coordenadas.append(event)
                window[event].update(window.find_element(letra_key).get_text(), button_color=('Black','#D8C99B'),)
                window[letra_key].update(button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtrilNegro)
            elif event in atril_k:
                Uncheck_button(event)
        if event == Comprobar:
            print(palabra)
            comprobacion=comprobar_palabra(palabra)
            if comprobacion:
             puntaje_j+=comprobar_puntaje(palabra,coordenadas,Letras,coor_rojos,coor_naranja,coor_azul,coor_celeste)
             window.find_element('puntaje_j').update(str(puntaje_j))
             cambiar_letras(window,key_letras,Letras,BotonAtril)
            else:
                sg.popup_no_buttons('Palabra no permitida',no_titlebar=True,text_color='#D8C99B',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='#1a2835')
                devolver_l=0
                for k in key_letras:
                 window.find_element(k).update(text=palabra[devolver_l],button_color=('#D8C99B', sg.theme_background_color()),image_filename=BotonAtril)
                 if coordenadas[devolver_l] in coor_rojos:
                     window.find_element(coordenadas[devolver_l]).update(button_color=('black','#C34C47'),text='Px2')
                 elif coordenadas[devolver_l] in coor_celeste:
                     window.find_element(coordenadas[devolver_l]).update(button_color=('black','#98d6ea'),text='L-2')
                 elif coordenadas[devolver_l] in coor_azul:
                     window.find_element(coordenadas[devolver_l]).update(button_color=('black','#2A9AAD'), text='Lx2')
                 elif coordenadas[devolver_l] in coor_naranja:
                     window.find_element(coordenadas[devolver_l]).update(button_color=('black','#ffb385'),text='P-5')
                 else:
                     window.find_element(coordenadas[devolver_l]).update(button_color=('#12947f','#12947f'))
                 devolver_l+=1
            palabra=''
            key_letras=[]
            coordenadas=[]
            puntaje_palabra=comprobar_puntaje(palabra,coordenadas,Letras,coor_rojos,coor_naranja,coor_azul,coor_celeste)
            puntaje_j+=puntaje_palabra
            print(puntaje_palabra)
            window.find_element('puntaje_j').update(str(puntaje_j))
            cambiar_letras(window,key_letras,Letras,BotonAtril)
            palabra=''
            key_letras=[]
            coordenadas=[]
        if event == CAMBIARFICHAS:
            if (cant_cambios == 3)|(cant_cambios > 3):
                devolver_l=0
                sg.popup_auto_close('Ya uso todos sus cambios',auto_close_duration=2,no_titlebar=True,font=("Calibri", 15,'bold'),background_color='black',text_color='#D8C99B',button_color=('#1A2835','#D8973C'))
                for k in key_letras:
                    window.find_element(k).update(text=palabra[devolver_l],button_color=(sg.theme_background_color(), sg.theme_background_color()),image_filename=BotonAtril)
                    devolver_l+=1
            else:
                cambiar_letras(window,key_letras,Letras,BotonAtril)
                palabra=''
                key_letras=[]
                cant_cambios+=1

    window.close()

if __name__ == '__main__':
    main('jugador')
