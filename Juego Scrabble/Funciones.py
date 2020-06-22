#modulo con todas las funciones que usan los distintos niveles
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
def comprobar_palabra(palabra,nivel):
    clasificacion = clasificar(palabra)
    if clasificacion == 'No existe esa palabra':
     return False
    elif nivel=='Normal': 
         if clasificacion[0][1]=='NN': #pregunta si es un sustantivo
             return False
         elif clasificacion[0][1]== 'JJ': # pregunta si es un adjetivo
             return True
         elif clasificacion[0][1]== 'VB': #pregunta si es un verbo
             return True
         else:
             return False #si la palabra no es ninguno de esos da falso ya que pattern devuelve otros tipos de palabra

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

def comprobar_puntaje(palabra,coordenadas,Letras,coor_rojos,coor_naranja,coor_azul,coor_celeste,nivel):
    puntaje=0
    valor_letra=0
    if nivel == 'Normal':
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

def cargar_jugador(nombre,puntaje,nivel):
    import json
    archivo='top.txt'
    with open(archivo,'r') as f:
         dicc_top10=json.load(f)
         jugador={'puntaje':puntaje, 'nivel':nivel}
         dicc_top10.setdefault(nombre,jugador)
    with open(archivo,'w') as f:
        json.dump(dicc_top10,f)


