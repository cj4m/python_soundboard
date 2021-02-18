import keyboard
from playsound import playsound

print('''
                   NUMPAD MACRO
            **************************
            *    Sounds available:   *
            *    0 = BABA BOOEY      *
            *    1 = Law&Order       *
            *    2 = DDDDUEL         *
            *    3 = Price Wrong     *
            *    4 = Pretty good     *
            *    y = nothing         *
            *    a = nothing         *
            *    s = nothing         *
            *    d = nothing         *
            *    f = nothing         *
            *    = = break           *
            *                        *
            **************************
''')
#scan codes for numpad :)
#num 0 = 82
#num 1 = 79
#num 2 = 80
#num 3 = 81
#num 4 = 75
#num 5 = 76
#num 6 = 77
#num 7 = 71
#num 8 = 72
#num 9 = 73
def macropad():
    while True:
        try:
            if keyboard.is_pressed(82):
                playsound('bababooey.mp3')
                print('bababooey')
                continue
            elif keyboard.is_pressed(79):
                playsound('lawandorder.mp3')
                print('dun dun')
                continue
            elif keyboard.is_pressed(80):
                playsound('dddduel.mp3')
                print('yugioh')
                continue
            elif keyboard.is_pressed(81):
                playsound('wompwomp.mp3')
                print('price is wrong')
                continue
            elif keyboard.is_pressed(75):
                playsound('prettygood.mp3')
                print('hey thatts pretty good')
                continue
#            elif keyboard.is_pressed('+'):
#                keyboard.hook()
            elif keyboard.is_pressed('='):
                break
        except:
            break

macropad()


# import keyboard  # using module keyboard
# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#             print('You Pressed A Key!')
#         break  # finishing the loop
#     except:
#         break    
