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
    #Inicializar lista de podio
    listaPodio = []
    #Recorrer cada jugador resgistrado en juego
    for jugador, datos in juego.items():
        #Obtener el nombre y los puntos de cada uno
        nomJugador = datos.get('Nombre','')
        puntosUser = datos.get('Puntos Usuario',0)
        #Añadir los datos obtenido anteriormente a la lista inicializada
        listaPodio.append([nomJugador,puntosUser])
    #Ordenar la lista creada en orden descendente
    listaPodio.sort(key=lambda x: x[1], reverse = True) #x toma el valor del primer elemento y x[1] el segundo de cada sublista
    #Imprimir el podio de los jugadores de acuerdo a su posición en la lista
    print ("        PODIO JUGADORES        ")
    print (f'Jugador 1: {listaPodio[0]}')
    print (f'Jugador 2: {listaPodio[1]}')
    print (f'Jugador 3: {listaPodio[3]}')
    #Imprimir el último jugador de acuerdo a la última posición
    print ("        ÚLTIMO RANKING        ")
    print (f'Último Jugador: {listaPodio[-1]}')

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
    if (numGanadores > 0):
        promedioGanaron = (numGanadores/partidasJugadas) #Operación para determinar el promedio
        print (f'El promedio de jugadores que han ganado contra la máquina es {promedioGanaron}')
    else:
        print ("No le han ganada a la máquina")

    c.pausarPantalla()