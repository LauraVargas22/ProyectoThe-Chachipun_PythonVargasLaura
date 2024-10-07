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
        nicknameJ1 = input("Ingrese su nickname: ").casefold().strip()
        nicknameJ2 = input("Ingrese su nickname: ").casefold().strip()

        jugador1 = None
        jugador2 = None

        for jugador, datos in juego.items():
            if datos['Nickname'] == nicknameJ1:
                jugador1 = jugador
            if datos['Nickname'] == nicknameJ2:
                jugador2 = jugador

        if (jugador1) and (jugador2):
            break
        else:
            if not (jugador1):
                print (f"El nickname {nicknameJ1} no ha sido registrado")
            if not (jugador2):
                print (f"El nickname {nicknameJ2} no ha sido registrado")
            c.pausarPantalla()
    
    
    rondaGanadaUser1 = 0
    rondaGanadaUser2 = 0
    partidaGanadaUno1 = juego[jugador1].get('Partida Ganada Uno',0)
    partidaPerdidaUno1 = juego[jugador1].get('Partida Perdida Uno', 0)
    puntosUser1 =juego[jugador1].get('Puntos Usuario',0)
    partidaGanadaUno2 = juego[jugador2].get('Partida Ganada Uno',0)
    partidaPerdidaUno2 = juego[jugador2].get('Partida Perdida Uno', 0)
    puntosUser2 =juego[jugador2].get('Puntos Usuario',0)
    
    while (rondaGanadaUser1 < 3) and (rondaGanadaUser2 < 3):
        opciones = ("piedra", "papel", "tijera")
        jugadaUser1 = input (f'{nicknameJ1} Ingrese su elección (piedra, papel o tijera): ').casefold().strip()
        jugadaUser2 = input (f'{nicknameJ2} Ingrese su elección (piedra, papel o tijera): ').casefold().strip()
        c.borrarPantalla()
        if (jugadaUser1 in opciones) and (jugadaUser2 in opciones):
            print (f'{nicknameJ1}: {jugadaUser1}')
            print (f'{nicknameJ2}: {jugadaUser2}')

            if (jugadaUser1 == jugadaUser2):
                print ("EMPATE")
            elif (jugadaUser1 == "piedra" and jugadaUser2 == "tijera") or (jugadaUser1 == "tijera" and jugadaUser2 == "papel") or (jugadaUser1 == "papel" and jugadaUser2 == "piedra"):
                print (f'{nicknameJ1} ha GANADO')
                puntosUser1 += 2
                juego[jugador1]['Puntos Usuario'] = puntosUser1
                rondaGanadaUser1 += 1
                print (f'Jugador 1 {nicknameJ1}:{rondaGanadaUser1} Jugador 2 {nicknameJ2}:{rondaGanadaUser2}')
                if (rondaGanadaUser1 == 2):
                    print (f'{nicknameJ1} ha recibido un ESCUDO')
                if (rondaGanadaUser2 == 3):
                    print (f'{nicknameJ1} ha GANADO el juego')
                    partidaGanadaUno1 += 1
                    juego[jugador1]['Partida Ganada Uno'] = partidaGanadaUno1
                    partidaPerdidaUno2 += 1
                    juego[jugador2]['Partida Perdida Uno'] = partidaPerdidaUno2
                    guardarJuego(juego,JUEGO_BASE)
                    c.pausarPantalla()
                    break
            else:
                print (f'{nicknameJ2} ha GANADO')
                puntosUser2 += 2
                juego[jugador2]['Puntos Usuario'] = puntosUser2
                rondaGanadaUser2 += 1
                print (f'Jugador 1 {nicknameJ1}:{rondaGanadaUser1} Jugador 2 {nicknameJ2}:{rondaGanadaUser2}')
                if (rondaGanadaUser2 == 2):
                    print (f'{nicknameJ2} ha recibido un ESCUDO')
                if (rondaGanadaUser2 == 3):
                    print (f'{nicknameJ2} ha GANADO el juego')
                    partidaGanadaUno2 += 1
                    juego[jugador2]['Partida Ganada Uno'] = partidaGanadaUno2
                    partidaPerdidaUno1 += 1
                    juego[jugador1]['Partida Perdida Uno'] = partidaPerdidaUno1
                    guardarJuego(juego,JUEGO_BASE)
                    c.pausarPantalla()
                    break
            print (f'{nicknameJ1} ha conseguido {puntosUser1} puntos por ronda ganadas')
            print (f'{nicknameJ2} ha conseguido {puntosUser2} puntos por rondas ganadas')
        else:
            print ("Error en la opción seleccionada")