'''
Desarrolló del juego en el modo Uno versus Máquina
'''
import os
import json
import random
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
    print ('****** UNO VERSUS MAQUINA ******')
    print ('Sr@ Jugador usted se enfrentara a nuestra maquina')
    nickname = ("Sr@ Jugador, ingrese su nickname: ").casefold()
    if (nickname in juego):
        rondas = 0
        rondaGanada = 0
        rondaPerdida = 0
        opciones = ["piedra", "papel", "tijera"]
        jugadaUser = input("Ingrese su elección (piedra, papel o tijera): ").casefold()
        if (jugadaUser != opciones):
            print ("Error en la opción seleccionada")
        else:
            jugadaIA = random.choice(opciones)

            print (f'Usuario: {jugadaUser}')
            print (f'Máquina: {jugadaIA}')

            if (jugadaUser == jugadaIA):
                print ("EMPATE")
            elif (jugadaUser == "piedra" and jugadaIA == "tijera") or (jugadaUser == "tijera" and jugadaIA == "papel") or (jugadaUser == "papel" and jugadaIA == "pierda"):
                print (f'{nickname} ha GANADO')
            else: 
                print ('La máquina ha GANADO')
    else:
        print (f"El nickname {nickname} ingresado no ha sido registrado")
