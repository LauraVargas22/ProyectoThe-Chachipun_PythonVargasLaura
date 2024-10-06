'''
Desarrolló del juego en el modo Uno versus Máquina
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
    nomJugador = input("Sr. Jugador, ingrese su nombre: ").title()
    if (nomJugador not in juego):
        print (f"El jugador {nomJugador} ingresado no ha sido registrado")
    else:
        rondaGanadaUser = 0
        rondaGanadaIA = 0
        partidaPerdidaIA = 0
        partidaGanadaIA = 0
        puntosUser = 0
        puntosIA = 0
        jugador = {
            'Nombre': nomJugador,
            'Nickname': '',
            'Puntos': puntosUser,
            'Partida Ganada IA': partidaGanadaIA,
            'Partida Perdida IA': partidaPerdidaIA
        }
        maquina = {
            "Jugadores Perdieron": [],
            "Puntos": puntosIA
        }
        while (rondaGanadaUser < 3) and (rondaGanadaIA < 3):
            opciones = ("piedra", "papel", "tijera")
            jugadaUser = input('Ingrese su elección (piedra, papel o tijera): ').casefold()
            if (jugadaUser in opciones):
                jugadaIA = random.choice(opciones)
                print (f'Usuario: {jugadaUser}')
                print (f'Máquina: {jugadaIA}')

                if (jugadaUser == jugadaIA):
                    print ("EMPATE")
                elif (jugadaUser == "piedra" and jugadaIA == "tijera") or (jugadaUser == "tijera" and jugadaIA == "papel") or (jugadaUser == "papel" and jugadaIA == "piedra"):
                    print ('Sr Usuario ha GANADO')
                    puntosUser += 2
                    jugador["Puntos"] = puntosUser
                    rondaGanadaUser += 1
                    print (f'Usuario {rondaGanadaUser} Máquina {rondaGanadaIA}')
                    if (rondaGanadaUser == 2):
                        print (f'{nomJugador} ha recibido un ESCUDO')
                        if (rondaGanadaUser == 3):
                            print (f'{nomJugador} ha GANADO el juego')
                            partidaGanadaIA += 1
                            jugador['Partida Ganada IA'] = partidaGanadaIA
                            guardarJuego (juego,JUEGO_BASE)
                            c.pausarPantalla()
                            break
                else: 
                    print (f'La máquina ha GANADO, {nomJugador} ha perdido')
                    puntosIA += 2
                    maquina["Puntos"] = puntosIA
                    rondaGanadaIA += 1
                    print (f'Usuario {rondaGanadaUser} Máquina {rondaGanadaIA}')
                    if (rondaGanadaIA == 2):
                        print ("La maquina ha recibido un ESCUDO")
                    if (rondaGanadaIA == 3):
                        print ("La maquina ha GANADO el juego")
                        partidaPerdidaIA += 1
                        jugador["Partida Perdida IA"] = partidaPerdidaIA
                        nomJugador = nomJugador
                        juego[nomJugador] = maquina
                        print (f'El jugador {nomJugador} ha PERDIDO')
                        guardarJuego (juego,JUEGO_BASE)
                        c.pausarPantalla()
                        break
                print (f'{nomJugador} ha conseguido {puntosUser} por ronda ganada.')
                print (f'Maquina ha conseguido {puntosIA} puntos por ronda ganada')
            else:
                print ("Error en la opción seleccionada")


