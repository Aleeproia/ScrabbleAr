def comprobar_puntaje(palabra,coordenadas,Letras,coor_rojos,coor_naranja,coor_azul,coor_celeste):
    puntaje=0
    valor_letra=0
    resta_pal=0
    multip=0
    for l in range(0,len(palabra)):
        if coordenadas[l] in coor_azul:
            valor_letra=Letras[palabra[l].lower()][0]**2
            puntaje+=valor_letra
        if coordenadas[l] in coor_celeste:
            valor_letra=Letras[palabra[l].lower()][0]-1
            puntaje+=valor_letra
        if coordenadas[l] in coor_naranja:
            resta_pal+=2
        if coordenadas[l] in coor_rojos:
            multip+=2
        else:
            puntaje+=Letras[palabra[l].lower()][0]
    if multip > 0:
        puntaje= puntaje**multip
    puntaje= puntaje - resta_pal

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

def cambiar_letras(window,key_letras,Letras): 
    nuevas_letras=dar_letras(Letras,len(key_letras)) 
    cant=0
    for l in nuevas_letras:
         window.find_element(key_letras[cant]).update(text=l,button_color=('Black','#D8973C'))
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
    from string import ascii_uppercase as up
    from random import choice,randint

    sg.theme('DarkBlue')

    top=open('top.txt', 'r', encoding='utf8')
    top=top.read()

    Letras={'a':[1,11],'b':[3,3],'c':[2,4],'d':[2,4],'e':[1,11],'f':[4,2],'g':[2,2],'h':[4,2],'i':[1,6],'j':[6,2],'k':[8,1],'l':[1,4],'m':[3,3],'n':[1,6],'o':[1,8],'p':[3,2],'q':[8,1],'r':[1,4],'s':[1,7],'t':[1,4],'u':[1,6],'v':[4,2],'w':[8,2],'x':[8,2],'y':[4,2],'z':[10,1]}
    coor_rojos=[]
    coor_celeste=[] 
    coor_azul=[]
    coor_naranja=[]
    atril=dar_letras(Letras,7)
    A1=sg.Button(atril[0],button_color=('Black','#D8973C'),size=(6,3),pad=(0,0),border_width=(3),key='A1')
    A2=sg.Button(atril[1],button_color=('Black','#D8973C'),size=(6,3),pad=(0,0),border_width=(3),key='A2')
    A3=sg.Button(atril[2],button_color=('Black','#D8973C'),size=(6,3),pad=(0,0),border_width=(3),key='A3')
    A4=sg.Button(atril[3],button_color=('Black','#D8973C'),size=(6,3),pad=(0,0),border_width=(3),key='A4')
    A5=sg.Button(atril[4],button_color=('Black','#D8973C'),size=(6,3),pad=(0,0),border_width=(3),key='A5')
    A6=sg.Button(atril[5],button_color=('Black','#D8973C'),size=(6,3),pad=(0,0),border_width=(3),key='A6')
    A7=sg.Button(atril[6],button_color=('Black','#D8973C'),size=(6,3),pad=(0,0),border_width=(3),key='A7')
    atril_k=['A1','A2','A3','A4','A5','A6','A7']
    puntaje_j=0
    puntaje_c=0

    top_10jugadores=leer_top()

    botones_c= lambda name: sg.Button(name,button_color=('#D8973C','black'),size=(6,3),pad=((0),0),border_width=(3))
    button_j= lambda name : sg.Button(name,button_color=('#12947f','#12947f'),size=(3,1),pad=((0),0),border_width=(2),key=name)

    puntajes=[[sg.Text('PUNTAJE COMPUTADORA',text_color=('#D8C99B'),size=(19,1), font=("Courier New", 12))],
              [sg.Text('{}'.format(str(puntaje_c)),size=(16,5),font=("Helvetica"),key=('puntaje_c'))],
              [sg.Text('PUNTAJE {}'.format(nombre.upper()),text_color=('#D8C99B'),font=("Courier New",12))],
              [sg.Text('{}'.format(str(puntaje_j)),size=(16,5),font=("Helvetica"),key=('puntaje_j'))],
              [sg.Button('CAMBIAR TURNO',size=(15,1),pad=(25,20),button_color=('#A4243B','#D8973C'),border_width=(5),font=("Fixedsys",16))],
              [sg.Button('CAMBIAR FICHAS',size=(15,1),pad=(25,1),button_color=('#A4243B','#D8973C'),border_width=(5),font=("Fixedsys",16))]]

    
    top10=[[sg.Text('TOP 10 JUGADORES',text_color=('#D8C99B'),size=(16,1),font=("Courier New", 20))],
           [sg.Listbox(top_10jugadores,pad=(28,5),size=(30,12), no_scrollbar=True, text_color=('#D8C99B'))],
           [sg.Button('GUARDAR PARTIDA',size=(15,1),pad=(67,20),button_color=('#A4243B','#D8973C'),border_width=(5),font=("Fixedsys",16))],
           [sg.Button('TERMINAR',size=(15,1),pad=(67,1),button_color=('#A4243B','#D8973C'),border_width=(5),font=("Fixedsys",16))]]

    layout = [[sg.Text('COMPUTADORA     ',text_color='#D8C99B',font=("Courier New", 20))]+[botones_c('?') for i in atril],
             [sg.Column(puntajes),sg.Frame(layout=[[button_j((col,fila))for col in range(15)] for fila in range(15)],border_width=(20),title='',pad=(0,7), relief=sg.RELIEF_SUNKEN,background_color=('#D8973C')),sg.Column(top10)],
             [sg.Text('{}         '.format(nombre.upper()),text_color='#D8C99B',font=("Courier New", 20))]+[A1,A2,A3,A4,A5,A6,A7],
             [sg.Button('COMPROBAR',size=(15,1),button_color=('#A4243B','#D8973C'),border_width=(5),font=("Fixedsys",16))]]

   
    
    window = sg.Window('ScrabbleAr',grab_anywhere=True,no_titlebar=True).Layout(layout).Finalize()


    for i in range(15):
        for j in range(15):
            if((i==0)&(j==0))|((i==14)&(j==0))|((i==0)&(j==14))|((i==14)&(j==14))|((i==7)&(j==0))|((i==7)&(j==14))|((i==0)&(j==7))|((i==14)&(j==7)):
                window.find_element((i,j)).update(button_color=('black','#C34C47'),text='Px2')
                coor_rojos.append((i,j))
            if((i==3)&(j==0))|((i==11)&(j==0))|((i==6)&(j==2))|((i==8)&(j==2))|((i==0)&(j==3))|((i==7)&(j==3))|((i==14)&(j==3))|((i==2)&(j==6))|((i==6)&(j==6))|((i==8)&(j==6))|((i==12)&(j==6))|((i==3)&(j==7))|((i==11)&(j==7))|((i==2)&(j==8))|((i==6)&(j==8))|((i==8)&(j==8))|((i==12)&(j==8))|((i==0)&(j==11))|((i==7)&(j==11))|((i==14)&(j==11))|((i==6)&(j==12))|((i==8)&(j==12))|((i==3)&(j==14))|((i==11)&(j==14)):
                window.find_element((i,j)).update(button_color=('black','#98d6ea'),text='L-2')#c
                coor_celeste.append((i,j))
            if((i==5)&(j==1))|((i==9)&(j==1))|((i==1)&(j==5))|((i==5)&(j==5))|((i==9)&(j==5))|((i==13)&(j==5))|((i==1)&(j==9))|((i==5)&(j==9))|((i==9)&(j==9))|((i==13)&(j==9))|((i==5)&(j==13))|((i==9)&(j==13)):
                window.find_element((i,j)).update(button_color=('black','#2A9AAD'), text='Lx2')#a
                coor_azul.append((i,j))
            if((i==1)&(j==1))|((i==2)&(j==2))|((i==3)&(j==3))|((i==4)&(j==4))|((i==13)&(j==1))|((i==12)&(j==2))|((i==11)&(j==3))|((i==10)&(j==4))|((i==7)&(j==7))|((i==1)&(j==13))|((i==2)&(j==12))|((i==3)&(j==11))|((i==4)&(j==10))|((i==13)&(j==13))|((i==12)&(j==12))|((i==11)&(j==11))|((i==10)&(j==10)):
                window.find_element((i,j)).update(button_color=('black','#ffb385'),text='P-5')#n
                coor_naranja.append((i,j))

    palabra=''
    coordenadas=[]
    key_letras=[]
    
    Check_button = lambda x: window.FindElement(x).Update(button_color=('#D8973C','black'))
    Uncheck_button = lambda x: window.FindElement(x).Update(button_color=('Black','#D8973C'))
    current_Check_button = ''
    button_selected = False
    current_button_selected = ''
    
    while True:
        event, values = window.read()
        if event in (None, 'TERMINAR'):
            break
        if event in atril:
            Check_button(event)
            if button_selected:
                if event == current_button_selected:
                 Uncheck_button(event)
                 button_selected = False
                 current_button_selected = ''
                else:
                 Check_button(event)
                 button_selected = True
                 current_button_selected = event
            letra_key=event
            palabra+=window.find_element(letra_key).get_text()
            key_letras.append(event)
            event,values=window.read()
            coordenadas.append(event)
            window[event].update(window.find_element(letra_key).get_text(), button_color=('Black','#D8973C'))
            window[letra_key].update(button_color=('black','black'))
        if event == 'COMPROBAR':
            print(palabra,coordenadas)
            puntaje_j+=comprobar_puntaje(palabra,coordenadas,Letras,coor_rojos,coor_naranja,coor_azul,coor_celeste)
            window.find_element('puntaje_j').update(str(puntaje_j))
            cambiar_letras(window,key_letras,Letras)
            palabra=''
            key_letras=[]
            coordenadas=[]

    window.close()

if __name__ == '__main__':
    main('jugador')
