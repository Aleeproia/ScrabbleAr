    #recorro la lista Tablero hasta encontrar un espacio valido
    #una vez encontrado veo que la palabra entre horizontalmente, sino se puede trato de ponerla verticalmente
    #si no se puede poner de ninguna de las dos formas busco otro lugar para poner la palabra
def buscar_espacio(window,palabra,Tablero,Letras, nivel): #busca un lugar valido en el tablero para que pueda poner la palabra
    import random
    import PySimpleGUI as sg
    encontro=False
    coordenadas_c=[]
    while not encontro:
       coordenada_c=Tablero[random.randrange(0,len(Tablero)-1)]
       try: 
            if (coordenada_c[0]+len(palabra) <14) or (coordenada_c[0]+len(palabra) == 14):#horizontal
                cant_coor=0
                for l in palabra:
                    if window.find_element((coordenada_c[0]+cant_coor,coordenada_c[1])).get_text() not in Letras.keys():
                       if nivel == 'Facil': #en cada nivel la maquina va tener restricciones o no de uso de premios
                         if (window.find_element((coordenada_c[0]+cant_coor,coordenada_c[1])).get_text() != 'Px2') and (window.find_element((coordenada_c[0]+cant_coor,coordenada_c[1])).get_text() != 'Lx3'):
                             coordenadas_c.append((coordenada_c[0]+cant_coor,coordenada_c[1]))
                             cant_coor+=1
                         else:
                             raise NameError
                       elif nivel == 'Normal':
                         if (window.find_element((coordenada_c[0]+cant_coor,coordenada_c[1])).get_text() != 'Px2'):
                             coordenadas_c.append((coordenada_c[0]+cant_coor,coordenada_c[1]))
                             cant_coor+=1   
                         else:
                             raise NameError 
                       elif  nivel== 'Dificil':
                          coordenadas_c.append((coordenada_c[0]+cant_coor,coordenada_c[1]))
                          cant_coor+=1                 
                    else:
                     raise NameError
                encontro=True
            elif (coordenada_c[1]+len(palabra) <14) or (coordenada_c[1]+len(palabra) == 14):#vertical
                cant_coor=0
                for l in palabra:
                    if window.find_element((coordenada_c[0]+cant_coor,coordenada_c[1])).get_text not in Letras.keys():
                     if nivel == 'Facil':
                          if (window.find_element((coordenada_c[0]+cant_coor,coordenada_c[1])).get_text() != 'Px2') and (window.find_element((coordenada_c[0]+cant_coor,coordenada_c[1])).get_text() != 'Lx3'):
                             coordenadas_c.append((coordenada_c[0]+cant_coor,coordenada_c[1]))
                             cant_coor+=1
                          else:
                              raise NameError
                     elif nivel == 'Normal':
                         if (window.find_element((coordenada_c[0]+cant_coor,coordenada_c[1])).get_text() != 'Px2'):
                             coordenadas_c.append((coordenada_c[0]+cant_coor,coordenada_c[1]))
                             cant_coor+=1   
                         else:
                             raise NameError 
                     elif  nivel== 'Dificil':
                         coordenadas_c.append((coordenada_c[0]+cant_coor,coordenada_c[1]))
                         cant_coor+=1                 
                    else:
                     raise NameError
                encontro=True
            else:
                coordenadas_c=[]
                encontro=False
       except NameError: #si ocurre este error es porque la maquina encontro posiciones donde no tiene permitido poner una letra
         coordenadas_c=[]
         encontro= False
       except TypeError: #este error ocurre cuando la maquina quiere poner letras fuera del tablero
         coordenadas_c=[]
         encontro= False
    return coordenadas_c
#-------------------------------------generacion de palabras --------------------------------------------------------------

def generar_palabras(atril,nivel,eleccion):
    from itertools import permutations
    import pattern.es
    '''este programa genera todas las combinaciones posibles con las letras que recibe en una lista'''

    #tipos de palabras que admite
    tipo_pal = {'adj': ["AO", "JJ", "AQ", "DI", "DT"],

            'verb': ["VAG", "VBG", "VAI", "VAN", "MD", "VAS", "VMG", "VMI", "VB", "VMM", "VMN", "VMP", "VBN", "VMS", "VSG",
                    "VSI", "VSN", "VSP", "VSS"],
            'sust': ['NN']}

    if nivel == 'Facil': #se configura el tipo de palabra valido segun el nivel que haya sido elegido
        opcion=tipo_pal 
    elif nivel == 'Normal':
        opcion={'adj':tipo_pal['adj'],'verb':tipo_pal['verb']}
    elif nivel == 'Dificil':
        if eleccion == 'VB':
            opcion={'verb':tipo_pal['verb']}
        elif eleccion == 'NN':
            opcion={'sust':tipo_pal['sust']}
        else:
            opcion={'adj':tipo_pal['adj']}
    def clasifico(palabra, clasificacion): #se clasifican las palabras segun el tipo de palabra pedido, si no esta en el tipo pedido la palabra no se agrega
        s = (pattern.es.parse(palabra)).split()
        for cada in s:
            for c in cada:
                for tipo in clasificacion:
                    if c[1] in clasificacion[tipo]:
                        return True


    def es_pal(pal): #verifica que sea una palabra valida.
        if pal in pattern.es.lexicon:
            if pal in pattern.es.spelling and len(pal)>2:

                return True
        return False


    def armo_palabra(atril): #recibe el atril de la maquina y con esas letras arma posibles combinaciones
        letras = ''
        for letra in atril:
            letras += letra.lower()
        palabras = set()
        for i in range(2, len(letras) + 1):
            palabras.update((map("".join, permutations(letras, i))))
        return (palabras)
    lista_palabras = armo_palabra(atril)

    palabras_tipos= []
    palabras_validas = []
    for pal in lista_palabras:
        if es_pal(pal):
            palabras_validas.append(pal)
            if clasifico(pal, opcion):
                palabras_tipos.append(pal) #agrego las palabras con los tipos de palabras validos
    return palabras_validas
