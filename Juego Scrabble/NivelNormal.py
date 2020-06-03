def main():
    import  PySimpleGUI as sg
    from string import ascii_uppercase as up
    from random import choice,randint
    sg.theme('DarkBlue')
    letrasRandom = lambda : [choice(up) for i in range(7)] #Esto se va a modificar,(solo es de prueba)
    a=letrasRandom()
    color_button = ('Black','#D8973C')
    button = lambda name : sg.Button(name,button_color=color_button,size=(6,3),pad=((0),0),border_width=(3))
    button_j= lambda name : sg.Button(name,button_color=('#12947f','#12947f'),size=(3,1),pad=((0),0),border_width=(3),key=name)
    layout = [[button_j((col,fila)) for col in range(15)] for fila in range(15)]

    layout.append([button(i) for i in a])

    #layout.append([sg.Button('empezar', key='empezar'),sg.Button('asd', key='asd')]) (Botones que usariamos en algun futuro)
    
    window = sg.Window('ScrabbleAr',size=(900,500)).Layout(layout).Finalize()


    for i in range(15):
        for j in range(15):
            if((i==0)&(j==0))|((i==14)&(j==0))|((i==0)&(j==14))|((i==14)&(j==14))|((i==7)&(j==0))|((i==7)&(j==14))|((i==0)&(j==7))|((i==14)&(j==7)):
                window.find_element((i,j)).update(button_color=('#C34C47','#C34C47'))
            if((i==3)&(j==0))|((i==11)&(j==0))|((i==6)&(j==2))|((i==8)&(j==2))|((i==0)&(j==3))|((i==7)&(j==3))|((i==14)&(j==3))|((i==2)&(j==6))|((i==6)&(j==6))|((i==8)&(j==6))|((i==12)&(j==6))|((i==3)&(j==7))|((i==11)&(j==7))|((i==2)&(j==8))|((i==6)&(j==8))|((i==8)&(j==8))|((i==12)&(j==8))|((i==0)&(j==11))|((i==7)&(j==11))|((i==14)&(j==11))|((i==6)&(j==12))|((i==8)&(j==12))|((i==3)&(j==14))|((i==11)&(j==14)):
                window.find_element((i,j)).update(button_color=('#98d6ea','#98d6ea'))
            if((i==5)&(j==1))|((i==9)&(j==1))|((i==1)&(j==5))|((i==5)&(j==5))|((i==9)&(j==5))|((i==13)&(j==5))|((i==1)&(j==9))|((i==5)&(j==9))|((i==9)&(j==9))|((i==13)&(j==9))|((i==5)&(j==13))|((i==9)&(j==13)):
                window.find_element((i,j)).update(button_color=('#2A9AAD','#2A9AAD'))
            if((i==1)&(j==1))|((i==2)&(j==2))|((i==3)&(j==3))|((i==4)&(j==4))|((i==13)&(j==1))|((i==12)&(j==2))|((i==11)&(j==3))|((i==10)&(j==4))|((i==7)&(j==7))|((i==1)&(j==13))|((i==2)&(j==12))|((i==3)&(j==11))|((i==4)&(j==10))|((i==13)&(j==13))|((i==12)&(j==12))|((i==11)&(j==11))|((i==10)&(j==10)):
                window.find_element((i,j)).update(button_color=('#ffb385','#ffb385'))
                
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        #window[event].update('etra', button_color=('white','black'))

    window.close()

if __name__ == '__main__':
    main()