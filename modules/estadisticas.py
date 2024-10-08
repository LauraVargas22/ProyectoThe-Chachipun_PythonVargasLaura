'''
Muestra de estadisticas teniendo en cuenta algunos aspectos
'''
import os
import json
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

def estadisticas (JUEGO_BASE: str):
    juego = cargarJuego(JUEGO_BASE)

    puntosPorJugador = {}

    print ("        PODIO JUGADORES        ")
    for jugador in juego.items():
        for nomJugador, puntosUser in puntosPorJugador.items():
            print (f'{nomJugador}: {puntosUser}')
