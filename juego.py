'''
Programa para el desarrollo del juego 
By Mariana Vargas
'''
if (__name__=='__main__'):

    import modules.customs as c
    import modules.menu as m
    import modules.titles as t


    isActive = True
    while (isActive):
        try:
            c.borrarPantalla()
            print (t.title1)
            print (m.menu1)
            opcMenuP = int(input('Seleccione:_'))

            match opcMenuP:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case _:
                    pass
        except ValueError:
            pass