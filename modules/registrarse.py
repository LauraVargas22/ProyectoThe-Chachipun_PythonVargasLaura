'''
Desarrollo de función para el registro de jugadores.
'''
import os
import json
import modules.customs as c
import modules.salir as s
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

def addJugadores (JUEGO_BASE: str):
    juego = cargarJuego(JUEGO_BASE)

    isaddJugadores = True
    while (isaddJugadores):
        c.borrarPantalla()
        nomJugador = input('Sr.Usuario, ingrese su nombre completo:\n ').title()
        if (nomJugador in juego):
            print ("Ya se encuentra registrado")
            c.pausarPantalla()
        else:
            nickname = input(f'Sr {nomJugador}, ingrese un nickname:\n ').casefold()
            if (nickname in juego):
                print ("Nickname ocupado ingrese otro: ").casefold()

            jugador = {
                'Nombre': nomJugador,
                'Nickname': nickname,
                'Puntos': 0,
                'Partida Ganada IA': 0,
                'Partida Perdida IA': 0,
                'Partida Ganada Uno': 0,
                'Partida Perdida Uno': 0
            }
            juego[nomJugador] = jugador
            juego[nickname] = nomJugador
            guardarJuego (juego, JUEGO_BASE)
            print (f'Se ha registrado a {nomJugador}, su nickname es {nickname}')
            c.pausarPantalla()
            isaddJugadores = s.validateData ('¿Desea salir del menú de registro S(Si) N(No)?')