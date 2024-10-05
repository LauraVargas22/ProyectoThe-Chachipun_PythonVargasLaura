'''
Funciones a implementar para la validación de respuestas
'''

def validateData (message:str):
    global isAllow
    flagFunction = True
    opciones = ('N','S')
    accion = input (f'{message}').upper()
    if (accion not in opciones):
        print ('La opción ingresada no es válida...')
        validateData()
    elif (accion == 'N'):
        flagFunction = True
    elif ((accion) == 'S'):
        flagFunction = False
    return flagFunction

def validateAnswer (message:str):
    global isAllow
    flagFunction = True
    opciones = ('N', 'S')
    accion = input (f'{message}').upper()
    if (accion not in opciones):
        print ('La opción ingresada no es válida...')
        validateAnswer()
    elif(accion == 'N'):
        flagFunction = False
    elif ((accion)== 'S'):
        flagFunction = True
    return flagFunction