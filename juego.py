'''
Programa para el desarrollo del juego 
By Mariana Vargas
'''
if (__name__=='__main__'):

    JUEGO_BASE = 'data/juego.json'

    import modules.customs as c
    import modules.menu as m
    import modules.titles as t
    import modules.mensajes as msg
    import modules.salir as s
    import modules.registrarse as re
    import modules.unovsmaquina as ia
    isActive = True
    while (isActive):
        try:
            c.borrarPantalla()
            print (t.title1)
            print (m.menu1)
            opcMenuP = int(input('Seleccione:_'))

            match opcMenuP:
                case 1:
                    print (t.subtitle1) #Registrarse
                    re.addJugadores (JUEGO_BASE)
                    c.pausarPantalla()
                case 2:
                    print (t.subtitle2)
                    isPlay = True
                    while (isPlay):
                        try:
                            c.borrarPantalla()
                            print (m.menu2)
                            opcMenu2 = int(input('Seleccione:_'))
                        except ValueError:
                            print (msg.msgExcept)
                            c.pausarPantalla()
                            continue
                        else:
                            match opcMenu2:
                                case 1:
                                    print (t.subtitle2)
                                    #Uno versus uno
                                    c.pausarPantalla()
                                case 2:
                                    print (t.subtitle3)
                                    ia.UnoVersusMaquina(JUEGO_BASE)
                                    c.pausarPantalla()
                                case 3:
                                    isPlay = s.validateData(msg.msgInfo)
                                case _:
                                    print (msg.msgCase)
                                    c.pausarPantalla()
                case 3:
                    pass #Estadísticas
                case 4:
                    isActive = s.validateData(msg.msgInfo)
                case _:
                    print (msg.msgCase)
                    c.pausarPantalla()
        except ValueError:
            print (msg.msgExcept)
            c.pausarPantalla()
            continue