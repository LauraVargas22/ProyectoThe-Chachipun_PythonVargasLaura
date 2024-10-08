'''
Desarrollo del juego en el modo Uno vs Uno
'''
import os
import json
import modules.customs as c    
JUEGO_BASE = None

def cargarJuego (JUEGO_BASE: str):
    if os.path.isfile(JUEGO_BASE):
        with open(JUEGO_BASE, 'r') as file:
            return json.load(file)
    else:
        return{}
    
def guardarJuego (juego: dict, JUEGO_BASE: str):
    with open(JUEGO_BASE, 'w') as file:
        json.dump(juego, file, indent=4)

def unoVersusUno (JUEGO_BASE: str):
    juego = cargarJuego(JUEGO_BASE)
    
    isPlayUno = True
    while (isPlayUno):
        #Ingreso de nicknames jugadores
        nicknameJ1 = input("Ingrese su nickname: ").casefold().strip()
        nicknameJ2 = input("Ingrese su nickname: ").casefold().strip()

        jugador1 = None
        jugador2 = None
        #Buscar nickname en cada jugador que esté registrado
        for jugador, datos in juego.items():
            if datos.get('Nickname') == nicknameJ1:
                jugador1 = jugador
            if datos.get('Nickname') == nicknameJ2:
                jugador2 = jugador
        #Continua el juego si ambos están registrados
        if (jugador1) and (jugador2):
            break
        else: #Correción de nicknames en caso de no estar registrados
            if not (jugador1):
                print (f"El nickname {nicknameJ1} no ha sido registrado")
            if not (jugador2):
                print (f"El nickname {nicknameJ2} no ha sido registrado")
            c.pausarPantalla()
    
    #Inicialización variables
    rondaGanadaUser1 = 0
    rondaGanadaUser2 = 0
    partidaGanadaUno1 = juego.get('jugador',{}).get('Partida Ganada Uno',0)
    partidaPerdidaUno1 = juego.get('jugador',{}).get('Partida Perdida Uno', 0)
    puntosUser1 =juego.get('jugador',{}).get('Puntos Usuario',0)
    partidaGanadaUno2 = juego.get('jugador',{}).get('Partida Ganada Uno',0)
    partidaPerdidaUno2 = juego.get('jugador',{}).get('Partida Perdida Uno', 0)
    puntosUser2 =juego.get('jugador',{}).get('Puntos Usuario',0)
    #Bucle para determinar fin del juego al tener 3 partidas ganadas uno de los jugadores.
    while (rondaGanadaUser1 < 3) and (rondaGanadaUser2 < 3):
        #Ingreso de opciones a jugar
        opciones = ("piedra", "papel", "tijera")
        jugadaUser1 = input (f'{nicknameJ1} Ingrese su elección (piedra, papel o tijera): ').casefold().strip()
        jugadaUser2 = input (f'{nicknameJ2} Ingrese su elección (piedra, papel o tijera): ').casefold().strip()
        c.borrarPantalla()
        if (jugadaUser1 in opciones) and (jugadaUser2 in opciones): #Validación de opciones ingresadas por el usuario
            print (f'{nicknameJ1}: {jugadaUser1}')
            print (f'{nicknameJ2}: {jugadaUser2}')

            if (jugadaUser1 == jugadaUser2): #Condiciones de empate 
                print ("EMPATE")
            #Condiciones para ganar jugador 1
            elif (jugadaUser1 == "piedra" and jugadaUser2 == "tijera") or (jugadaUser1 == "tijera" and jugadaUser2 == "papel") or (jugadaUser1 == "papel" and jugadaUser2 == "piedra"):
                print (f'{nicknameJ1} ha GANADO')
                puntosUser1 += 2 #Sumar puntos por partida ganada
                juego[jugador1]['Puntos Usuario'] = puntosUser1
                rondaGanadaUser1 += 1 #Sumar ronda ganada
                print (f'Jugador 1 {nicknameJ1}:{rondaGanadaUser1} Jugador 2 {nicknameJ2}:{rondaGanadaUser2}') #Marcador
                if (rondaGanadaUser1 == 2): #Otorgar escudo jugador 1
                    print (f'{nicknameJ1} ha recibido un ESCUDO')
                if (rondaGanadaUser1 == 3): #Si gana el jugador 1
                    print (f'{nicknameJ1} ha GANADO el juego')
                    partidaGanadaUno1 += 1 #Sumar partida ganada jugador 1
                    juego[jugador1]['Partida Ganada Uno'] = partidaGanadaUno1
                    partidaPerdidaUno2 += 1 #Sumar partida perdida jugador 2
                    juego[jugador2]['Partida Perdida Uno'] = partidaPerdidaUno2
                    guardarJuego(juego,JUEGO_BASE)
                    c.pausarPantalla()
                    break
            else: #Condiciones para ganar jugador 2
                print (f'{nicknameJ2} ha GANADO')
                puntosUser2 += 2 #Sumar puntos por ronda ganada jugador 2
                juego[jugador2]['Puntos Usuario'] = puntosUser2
                rondaGanadaUser2 += 1 #Sumar ronda ganada jugador 2
                print (f'Jugador 1 {nicknameJ1}:{rondaGanadaUser1} Jugador 2 {nicknameJ2}:{rondaGanadaUser2}') #Marcador
                if (rondaGanadaUser2 == 2): #Escudo jugador 2
                    print (f'{nicknameJ2} ha recibido un ESCUDO')
                if (rondaGanadaUser2 == 3): #Si gana jugador 2
                    print (f'{nicknameJ2} ha GANADO el juego')
                    partidaGanadaUno2 += 1 #Sumar partida ganada jugador 2
                    juego[jugador2]['Partida Ganada Uno'] = partidaGanadaUno2
                    partidaPerdidaUno1 += 1 #Sumar partida perdida jugador 1
                    juego[jugador1]['Partida Perdida Uno'] = partidaPerdidaUno1
                    guardarJuego(juego,JUEGO_BASE)
                    c.pausarPantalla()
                    break
            #Impresión de puntos conseguidos por jugador
            print (f'{nicknameJ1} ha conseguido {puntosUser1} puntos por ronda ganadas')
            print (f'{nicknameJ2} ha conseguido {puntosUser2} puntos por rondas ganadas')
        else:
            print ("Error en la opción seleccionada")