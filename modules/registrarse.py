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
        nomJugador = input('Sr.Usuario, ingrese su nombre completo:\n ').title().strip() #Registrar nombre de jugador, validando mayúsculas en iniciales y espacios de inicio y fin
        if (nomJugador in juego):
            print ("Ya se encuentra registrado") 
            c.pausarPantalla()
            continue
        else:
            nickname = input(f'Sr {nomJugador}, ingrese un nickname:\n ').casefold().strip() #Registrar nickname validando mayúsculas y minúsculas
            if (nickname in juego):
                nickname = input("Nickname ocupado ingrese otro: ").casefold().strip()
            #Formato diccionario por jugador
            jugador = {
                'Nombre': nomJugador,
                'Nickname': nickname,
                'Puntos Usuario': 0,
                'Partida Ganada IA': 0,
                'Partida Perdida IA': 0,
                'Partida Ganada Uno': 0,
                'Partida Perdida Uno': 0
            }
            juego[nomJugador] = jugador
            print (f'Se ha registrado {nomJugador}, su nickname es {nickname}')
            guardarJuego (juego, JUEGO_BASE)
            c.pausarPantalla()
            isaddJugadores = s.validateData ('¿Desea salir del menú de registro S(Si) N(No)?')