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
    nickname = input("Sr. Jugador, ingrese su nickname: ").casefold()
    if (nickname not in juego):
        print (f"El nickname {nickname} ingresado no ha sido registrado")
    else:
        rondaGanadaUser = 0
        rondaGanadaIA = 0
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
                    rondaGanadaUser += 1
                    print ('Usuario {rondaGanadaUser} Máquina {rondaGanadaIA}')
                    if (rondaGanadaUser == 2):
                        print (f'{nickname} ha recibido un ESCUDO')
                        if (rondaGanadaUser == 3):
                            print (f'{nickname} ha GANADO el juego')
                            c.pausarPantalla()
                else: 
                    print (f'La máquina ha GANADO, {nickname} ha perdido')
                    rondaGanadaIA += 1
                    print ('Usuario {rondaGanadaUser} Máquina {rondaGanadaIA}')
                    if (rondaGanadaIA == 2):
                        print ("La maquina ha recibido un ESCUDO")
                    if (rondaGanadaIA == 3):
                        print ("La maquina ha GANADO el juego")
                        c.pausarPantalla()
            else:
                print ("Error en la opción seleccionada")


