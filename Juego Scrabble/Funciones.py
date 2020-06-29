#modulo con todas las funciones que usan los distintos niveles
import PySimpleGUI as sg
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
def comprobar_palabra(palabra,nivel,Eleccion=''):
    clasificacion = clasificar(palabra)
    if clasificacion == 'No existe esa palabra':
     return False
    elif nivel == 'Facil':
         if clasificacion[0][1]=='NN': #pregunta si es un sustantivo
             return True
         elif clasificacion[0][1]== 'JJ': # pregunta si es un adjetivo
             return True
         elif clasificacion[0][1]== 'VB': #pregunta si es un verbo
             return True
         else:
             return False #si la palabra no es ninguno de esos da falso ya que pattern devuelve otros tipos de palabra
    elif nivel=='Normal': 
         if clasificacion[0][1]=='NN':
             return False
         elif clasificacion[0][1]== 'JJ':
             return True
         elif clasificacion[0][1]== 'VB':
             return True
         else:
             return False
    elif nivel == 'Dificil':
        if clasificacion[0][1]==Eleccion:
            return True
        else:
            return False

def dar_letras(Letras,cant):
    import random
    lista_letras=[]
    l=[]
    for x in Letras.keys():
        l.append(x)
    for a in range(cant):
        letra=l[random.randint(0,len(l)-1)]
        while Letras[letra][1] == 0:
            letra=l[random.randint(0,len(l)-1)]
        Letras[letra][1]=Letras[letra][1]-1
        lista_letras.append(letra)
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
    archivo='./txts/top.txt'
    with open(archivo,'r') as f:
         dicc_top10=json.load(f)
         for jugador in dicc_top10.keys():
             lista_top10.append(jugador.upper())
             datos=['Puntaje:{}'.format(dicc_top10[jugador]['puntaje']),'Nivel:','{}'.format(dicc_top10[jugador]['nivel'])]
             lista_top10.append(datos)
    return lista_top10

def comprobar_puntaje(palabra,coordenadas,Letras,coor_rojos,coor_naranja,coor_azul,coor_celeste,nivel):
    puntaje=0
    valor_letra=0 
    if nivel == 'Normal':
        for l in range(0,len(palabra)):
         if coordenadas[l] in coor_azul:
             valor_letra=Letras[palabra[l]][0]*2
             puntaje+=valor_letra
         if coordenadas[l] in coor_celeste:
             puntaje=puntaje-2
         if coordenadas[l] in coor_naranja:
             puntaje=puntaje-5
         if coordenadas[l] in coor_rojos:
             valor_letra=Letras[palabra[l]][0]*2
             puntaje+=valor_letra
         else:
             puntaje+=Letras[palabra[l]][0]
    else:
        if nivel == 'Facil':
            for l in range(0,len(palabra)):
             if coordenadas[l] in coor_azul:
                 valor_letra=Letras[palabra[l]][0]*3
                 puntake+=valor_letra
             if coordenadas[l] in coor_celeste:
                 puntaje=puntaje-2
             if coordenadas[l] in coor_rojos:
                 puntaje=puntaje+5
             if coordeandas[l] in coor_naranja:
                 puntaje=puntaje-3
             else:
                 puntaje+=Letras[palabra[l]][0]
        else:
            if nivel == 'Dificil':
                for l in range(0,len(palabra)):
                 if coordenadas[l] in coor_azul:
                     valor_letra=Letras[palabra[l]][0]
                     puntaje=puntaje - valor_letra
                 if coordenadas[l] in coor_rojo:
                     puntaje=puntaje-5
                 if coordenadas[l] in coor_naranja:
                     puntaje=puntaje+4
                 if coordenadas[l] in coor_celeste:
                     puntaje=puntaje+2
                 else:
                     puntaje+=Letras[palabra[l]][0]
    return puntaje

def cargar_jugador(nombre,puntaje,nivel):
    import json
    archivo='./txts/top.txt'
    with open(archivo,'r') as f:
         dicc_top10=json.load(f)
         jugador={'puntaje':puntaje, 'nivel':nivel}
         dicc_top10.setdefault(nombre,jugador)
    with open(archivo,'w') as f:
        json.dump(dicc_top10,f)

def palabra_incorrecta(window,palabra,key_letras,coor_azul,coor_celeste,coor_naranja,coor_rojos,coordenadas,nivel,BotonAtril):
    devolver_l=0
    if nivel == 'Facil':
        rojo='P+5'
        celeste='P-2'
        azul='Lx3'
        naranja='P-3'
    elif nivel == 'Normal':
        rojo='Px2'
        celeste='L-2'
        azul='Lx2'
        naranja='P-5'
    else:
        rojo='P-5'
        celeste='L+2'
        azul='-LI'
        naranja='P+4'
    for k in key_letras:
     window.find_element(k).update(text=palabra[devolver_l],button_color=('#D8C99B', sg.theme_background_color()),image_filename=BotonAtril)
     if coordenadas[devolver_l] in coor_rojos:
         window.find_element(coordenadas[devolver_l]).update(button_color=('black','#C34C47'),text=rojo)
     elif coordenadas[devolver_l] in coor_celeste:
         window.find_element(coordenadas[devolver_l]).update(button_color=('black','#98d6ea'),text=celeste)
     elif coordenadas[devolver_l] in coor_azul:
         window.find_element(coordenadas[devolver_l]).update(button_color=('black','#2A9AAD'), text=azul)
     elif coordenadas[devolver_l] in coor_naranja:
         window.find_element(coordenadas[devolver_l]).update(button_color=('black','#ffb385'),text=naranja)
     else:
         window.find_element(coordenadas[devolver_l]).update(button_color=('#12947f','#12947f'),text=coordenadas[devolver_l])
     devolver_l+=1 

def movimiento_incorrecto(window,palabra,ultima_letra,key_letras,BotonAtril):
    sg.popup_no_buttons('Movimiento no permitido',no_titlebar=True,text_color='#D8C99B',auto_close=True,auto_close_duration=1,font=("Courier New", 20,'bold'),background_color='#1a2835')
    palabra=palabra.strip(ultima_letra)
    window.find_element(key_letras[-1]).update(text=ultima_letra,button_color=('#D8C99B', sg.theme_background_color()),image_filename=BotonAtril)
    key_letras.remove(key_letras[-1])
    return palabra
