'''
Desarrollo del juego en el modo Uno versus Máquina
'''
import os
import json
import random
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

def UnoVersusMaquina (JUEGO_BASE:str):
    juego = cargarJuego(JUEGO_BASE)
    print ('Sr.Jugador usted se enfrentará a nuestra maquina')
    isPlayMaquina = True
    while (isPlayMaquina):
        nomJugador = input("Sr. Jugador, ingrese su nombre: ").title()
        if (nomJugador in juego):
            break
        else:
            print (f"El jugador {nomJugador} no ha sido registrado. Inténtelo de nuevo.")
            c.pausarPantalla()

    rondaGanadaUser = 0
    rondaGanadaIA = 0
    partidaPerdidaIA = juego[nomJugador].get('Partida Perdida IA', 0)
    partidaGanadaIA = juego[nomJugador].get('Partida Ganada IA', 0)
    puntosUser = juego[nomJugador].get('Puntos Usuario', 0)
    puntosIA = 0
    jugador = {
        'Nombre': nomJugador,
        'Nickname': juego[nomJugador].get('Nickname', ''),
        'Puntos Usuario': puntosUser,
        'Partida Ganada IA': partidaGanadaIA,
        'Partida Perdida IA': partidaPerdidaIA,
        'Partida Ganada Uno': 0,
        'Partida Perdida Uno': 0
    }
    maquina = {
        "Jugadores Perdieron": juego.get("maquina",{}).get('Jugadores Perdieron',[]),
        "Puntos IA": puntosIA
    }
    while (rondaGanadaUser < 3) and (rondaGanadaIA < 3):
        opciones = ("piedra", "papel", "tijera")
        jugadaUser = input('Ingrese su elección (piedra, papel o tijera): ').casefold()
        c.borrarPantalla()
        if (jugadaUser in opciones):
            jugadaIA = random.choice(opciones)
            print (f'Usuario: {jugadaUser}')
            print (f'Máquina: {jugadaIA}')

            if (jugadaUser == jugadaIA):
                print ("EMPATE")
            elif (jugadaUser == "piedra" and jugadaIA == "tijera") or (jugadaUser == "tijera" and jugadaIA == "papel") or (jugadaUser == "papel" and jugadaIA == "piedra"):
                print ('Sr Usuario ha GANADO')
                puntosUser += 2
                jugador["Puntos Usuario"] = puntosUser
                rondaGanadaUser += 1
                print (f'Usuario {rondaGanadaUser} Máquina {rondaGanadaIA}')
                if (rondaGanadaUser == 2):
                    print (f'{nomJugador} ha recibido un ESCUDO')
                if (rondaGanadaUser == 3):
                    print (f'{nomJugador} ha GANADO el juego')
                    partidaGanadaIA += 1
                    jugador['Partida Ganada IA'] = partidaGanadaIA
                    juego[nomJugador] = jugador
                    guardarJuego (juego,JUEGO_BASE)
                    c.pausarPantalla()
                    break
            else: 
                print (f'La máquina ha GANADO, {nomJugador} ha perdido')
                puntosIA += 2
                maquina["Puntos IA"] = puntosIA
                rondaGanadaIA += 1
                print (f'Usuario {rondaGanadaUser} Máquina {rondaGanadaIA}')
                if (rondaGanadaIA == 2):
                    print ("La maquina ha recibido un ESCUDO")
                if (rondaGanadaIA == 3):
                    print ("La maquina ha GANADO el juego")
                    partidaPerdidaIA += 1
                    jugador["Partida Perdida IA"] = partidaPerdidaIA
                    if nomJugador not in maquina["Jugadores Perdieron"]:
                        maquina['Jugadores Perdieron'].append(nomJugador)
                        print (f'El jugador {nomJugador} ha PERDIDO') 
                    else:
                        print (f'{nomJugador}, la máquina le ha ganado nuevamente')

                    juego[nomJugador] = jugador
                    juego['maquina'] = maquina
                    guardarJuego (juego,JUEGO_BASE)
                    c.pausarPantalla()
                    break
            print (f'{nomJugador} ha conseguido {puntosUser} puntos por rondas ganadas.')
            print (f'Maquina ha conseguido {puntosIA} puntos por rondas ganadas')
        else:
            print ("Error en la opción seleccionada")



