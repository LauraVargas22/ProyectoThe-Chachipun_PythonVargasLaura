'''
Programa para el desarrollo del juego 
By Mariana Vargas
'''
if (__name__=='__main__'):

    import modules.customs as c
    import modules.menu as m
    import modules.titles as t
    import modules.mensajes as msg
    import modules.salir as s


    isActive = True
    while (isActive):
        try:
            c.borrarPantalla()
            print (t.title1)
            print (m.menu1)
            opcMenuP = int(input('Seleccione:_'))

            match opcMenuP:
                case 1:
                    print (t.subtitle1)
                    isPlayUno = True
                    while (isPlayUno):
                        try:
                            c.borrarPantalla()
                            print (m.menu1a)
                            opcMenu1a = int(input('Seleccione:_'))
                        except ValueError:
                            print (msg.msgExcept)
                            c.pausarPantalla()
                            continue
                        else:
                            match opcMenu1a:
                                case 1:
                                    pass
                                case 2:
                                    pass
                                case 3:
                                    pass
                                case 4:
                                    isPlayUno =s.validateData(msg.msgRegresar)
                                case _:
                                    print (msg.msgCase)
                                    c.pausarPantalla()
                case 2:
                    print (t.subtitle2)
                    isPlayMaquina = True
                    while (isPlayMaquina):
                        try:
                            c.pausarPantalla()
                            print (m.menu2a)
                            opcMenu2a= int(input('Seleccione:_'))
                        except ValueError:
                            print (msg.msgExcept)
                            c.pausarPantalla()
                            continue
                        else: 
                            match opcMenu2a:
                                case 1:
                                    pass
                                case 2:
                                    pass
                                case 3:
                                    pass
                                case 4:
                                    isPlayMaquina = s.validateData(msg.msgRegresar)
                                case _:
                                    print (msg.msgCase)
                                    c.pausarPantalla()
                case 3:
                    isActive = s.validateData(msg.msgInfo)
                case _:
                    print (m.msgCase)
                    c.pausarPantalla()
        except ValueError:
            print (msg.msgExcept)
            c.pausarPantalla()
            continue