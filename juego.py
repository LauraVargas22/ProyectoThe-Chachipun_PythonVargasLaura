'''
Programa para el desarrollo del juego 
By Mariana Vargas
'''
if (__name__=='__main__'):
    #Archivo JSON con su ruta.
    JUEGO_BASE = 'data/juego.json'
    #Importación de módulos usados en el desarrollo del juego
    import modules.customs as c
    import modules.menu as m
    import modules.titles as t
    import modules.mensajes as msg
    import modules.salir as s
    import modules.registrarse as re
    import modules.unovsmaquina as ia
    import modules.unovsuno as uno
    import modules.estadisticas as es

    isActive = True
    while (isActive):
        try:
            c.borrarPantalla()
            print (t.title1)
            print (m.menu1) #Mnenú principal
            opcMenuP = int(input('Seleccione:_')) #Selección de opciones

            match opcMenuP:
                case 1:
                    print (t.subtitle1) #Registrarse
                    re.addJugadores (JUEGO_BASE) #Modulo de registro de jugadores
                    c.pausarPantalla()
                case 2:
                    print (t.subtitle2)
                    isPlay = True
                    while (isPlay):
                        try:
                            c.borrarPantalla()
                            print (m.menu2) #Menú con opciones de modo de juego
                            opcMenu2 = int(input('Seleccione:_')) #
                        except ValueError:
                            print (msg.msgExcept)
                            c.pausarPantalla()
                            continue
                        else:
                            match opcMenu2:
                                case 1:
                                    print (t.subtitle2)
                                    uno.unoVersusUno(JUEGO_BASE) #Modo de juego Uno versus Uno
                                    c.pausarPantalla()
                                case 2:
                                    print (t.subtitle3)
                                    ia.UnoVersusMaquina(JUEGO_BASE) #Modo de juego Uno versus Máquina
                                    c.pausarPantalla()
                                case 3:
                                    isPlay = s.validateData(msg.msgInfo) #Salir menú 2
                                case _:
                                    print (msg.msgCase) #Opción en caso que la opción ingresada no coincida
                                    c.pausarPantalla()
                case 3:
                    es.estadisticas(JUEGO_BASE) #Visualizar estadísticas del juego
                case 4:
                    isActive = s.validateData(msg.msgInfo) #Salir menú principal
                case _:
                    print (msg.msgCase) #Opción en caso que la opción ingresada no coincida
                    c.pausarPantalla()
        except ValueError:
            print (msg.msgExcept)
            c.pausarPantalla()
            continue