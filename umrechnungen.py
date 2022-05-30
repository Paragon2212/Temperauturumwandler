def convert_CtoK(C):
    tempk = C + 273.15
    print('In Grad Kelvin sind das ' + str(tempk)+' Kelvin')

def convert_CtoF(C):
    tempF = int(C)
    tempF = tempF*(9/5)+32
    print('In Grad Fahrenheit sind das ' + str(tempF) + ' °F')

def convert_FtoC(F):
    tempC =int(F)
    tempC = (tempC - 32) * (5/9)
    print('In Grad Celsius sind das ' + str(tempC) + ' °C')

def convert_FtoK(F):
    tempK =int(F)
    tempK = (tempK - 32) * (5/9) + 273.15
    print('In Grad Kelvin sind das ' + str(tempK) + ' Kelvin')

def convert_KtoC(K):
    tempC =int(K)
    tempC = tempC - 273.15
    print('In Grad Celsius sind das ' + str(tempC) + ' °C')

def convert_KtoF(K):
    tempF =int(K)
    tempF = (tempF - 273.15) * (9/5) + 32
    print('In Grad Fahrenheit sind das ' + str(tempF) + ' °F')