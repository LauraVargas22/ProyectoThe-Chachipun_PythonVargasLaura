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

    print ("        PODIO JUGADORES        ")



    print ("        ÚLTIMO RANKING        ")


    

    print ("    JUGADORES QUE HAN PERDIDO CONTRA LA IA    ")
    jugadoresPerdieron = juego.get("maquina",{}).get('Jugadores Perdieron',[])
    contarjP = {}
    for jugador in jugadoresPerdieron:
        if jugador in contarjP: 
            contarjP[jugador] += 1
        else: 
            contarjP[jugador] = 1
    maxPerdidas = 0
    maxVecesP = None
    for jugador, frecuencia in contarjP.items():
        if frecuencia > maxPerdidas:
            maxPerdidas = frecuencia
            maxVecesP = jugador
    
    if (maxVecesP):
        print (f'El jugador que más ha perdido es: {maxVecesP} con {maxPerdidas}')
    else:
        print (f'Ningún jugador ha perdido contra la máquina')

    print ("        JUGADORES QUE HAN GANADO CONTRA LA IA        ")

    jugadoresGanaron = juego.get("maquina",{}).get('Jugadores Ganaron',[])
    jugadoresGanaron = len(maquina["Jugadores Ganaron"])
    print (jugadoresGanaron)
    
    promedioGanaron = jugadoresGanaron/partidasjugadas
    print (f'El promedio de jugadores que han ganado contra la IA es {promedioGanaron})