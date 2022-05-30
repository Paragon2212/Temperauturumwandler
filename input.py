from ast import Continue

def Hauptmenü():
    selection = input ('Tippe "exit" zum verlassen\nKonvertieren von [Celsius, Kelvin, Fahrenheit]:  ')
    if selection == str('Celsius'):
        s = 1
        return s
    elif selection == str('Kelvin'):
        s = 2
        return s
    elif selection == str('Fahrenheit'):
        s = 3
        return s
    elif selection == str('exit'):
        s = 4
        return s

def Submenü():
    selection = input ('Konvertieren nach [Celsius, Kelvin, Fahrenheit]:  ')
    if selection == str('Celsius'):
        s = 1
        return s
    elif selection == str('Kelvin'):
        s = 2
        return s
    elif selection == str('Fahrenheit'):
        s = 3
        return s
    elif selection == str('exit'):
        s = 4
        return s


def get_input_C():
    while True:
        temp = input ('Temperatur in Grad Celsius:  ')
        try:
           C =  float(temp)
           return C
        except ValueError:
            print('Das ist keine gültige Angabe für eine Temperatur')
            '''string_anderes = temp
            return string_anderes
            continue'''

def get_input_F():
    while True:
        temp = input ('Temperatur in Grad Fahrenheit:  ')
        try:
           F =  float(temp)
           return F
        except ValueError:
            print('Das ist keine gültige Angabe für eine Temperatur')
            '''string_anderes = temp
            return string_anderes
            continue'''

def get_input_K():
    while True:
        temp = input ('Temperatur in Grad Kelvin:  ')
        try:
           K =  float(temp)
           return K
        except  ValueError:
            print('Das ist keine gültige Angabe für eine Temperatur')
            '''string_anderes = temp
            return string_anderes
            continue'''
