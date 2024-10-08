'''
Muestra de estadisticas teniendo en cuenta algunos aspectos
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

def estadisticas (JUEGO_BASE: str):
    juego = cargarJuego(JUEGO_BASE)

    nomJugador = juego.get("jugador",{}).get('Nombre', '')
    puntosUser = juego.get("jugador",{}).get('Puntos Usuario', '')

    listPodio = list(nomJugador,puntosUser)

    print (listPodio)


    print ("        PODIO JUGADORES        ")



    print ("        ÚLTIMO RANKING        ")


    

    print ("    JUGADORES QUE HAN PERDIDO CONTRA LA MÁQUINA    ")
    jugadoresPerdieron = juego.get("maquina",{}).get('Jugadores Perdieron',[]) #Obtener lista de jugadores que perdieron
    #Contador de la lista
    contarjP = {} 
    for jugador in jugadoresPerdieron:
        if jugador in contarjP: 
            contarjP[jugador] += 1 
        else: 
            contarjP[jugador] = 1
    #Recorrer la cantidad de veces que el jugador se repite
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

    print ("        JUGADORES QUE HAN GANADO CONTRA LA MÁQUINA        ")
    #Diccionario máquina
    maquina = {
        "Jugadores Perdieron": juego.get("maquina",{}).get('Jugadores Perdieron',[]),
        "Jugadores Ganaron": juego.get("maquina",{}).get('Jugadores Ganaron',[]),
        "Partidas Jugadas": juego.get("maquina",{}).get("Partidas Jugadas", 0),
        "Puntos IA": juego.get("maquina",{}).get("Puntos IA", 0),
    }
    #Contar el número de jugadores en la lista
    jugadoresGanaron = juego.get("maquina",{}).get('Jugadores Ganaron',[])
    numGanadores = len(jugadoresGanaron)
    print (jugadoresGanaron)

    partidasJugadas = maquina.get("Partidas Jugadas", 0)
    
    if (partidasJugadas > 0):
        promedioGanaron = (numGanadores/partidasJugadas) #Operación para determinar el promedio
        print (f'El promedio de jugadores que han ganado contra la IA es {promedioGanaron}')
    else:
        print ("No se ha jugado en contra de la máquina")

    c.pausarPantalla()