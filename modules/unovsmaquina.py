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
        nickname = input("Sr. Jugador, ingrese su nickname: ").casefold().strip() #Verificar el nombre del jugador
        if (nickname in juego):
            break
        else:
            print (f"El jugador {nickname} no ha sido registrado. Inténtelo de nuevo.")
            c.pausarPantalla()
    #Inicialización de datos necesarios para el desarrollo del juego
    rondaGanadaUser = 0
    rondaGanadaIA = 0
    partidaPerdidaIA = juego.get("jugador",{}).get('Partida Perdida IA', 0)
    partidaGanadaIA = juego.get("jugador",{}).get('Partida Ganada IA', 0)
    puntosUser = juego.get("jugador",{}).get('Puntos Usuario', 0)
    partidaJugada = juego.get('maquina',{}).get('Partidas Jugadas', 0)
    puntosIA = 0
    #Formato de diccionario del jugador y máquina
    jugador = {
        'Nombre': juego[nickname].get('Nombre', ''),
        'Nickname': nickname,
        'Puntos Usuario': puntosUser,
        'Partida Ganada IA': partidaGanadaIA,
        'Partida Perdida IA': partidaPerdidaIA,
        'Partida Ganada Uno': 0,
        'Partida Perdida Uno': 0
    }
    maquina = {
        "Jugadores Perdieron": juego.get("maquina",{}).get('Jugadores Perdieron',[]),
        "Jugadores Ganaron": juego.get("maquina",{}).get('Jugadores Ganaron',[]),
        "Partidas Jugadas": partidaJugada,
        "Puntos IA": puntosIA
    }
    partidaJugada += 1
    maquina['Partidas Jugadas'] = partidaJugada
    #Bucle para determinar 3 partidas ganadas por maquina o jugador.
    while (rondaGanadaUser < 3) and (rondaGanadaIA < 3):
        opciones = ("piedra", "papel", "tijera")
        jugadaUser = input('Ingrese su elección (piedra, papel o tijera): ').casefold()
        c.borrarPantalla()
        if (jugadaUser in opciones): #Jugar si las opciones coinciden
            jugadaIA = random.choice(opciones)
            print (f'Usuario: {jugadaUser}')
            print (f'Máquina: {jugadaIA}')
            #Parámetros del juego en caso de empate
            if (jugadaUser == jugadaIA):
                print ("EMPATE")
            #Parámetros del juego en caso de ganar el jugador
            elif (jugadaUser == "piedra" and jugadaIA == "tijera") or (jugadaUser == "tijera" and jugadaIA == "papel") or (jugadaUser == "papel" and jugadaIA == "piedra"):
                print ('Sr Usuario ha GANADO')
                puntosUser += 2 #Sumar puntos por ronda ganada
                jugador["Puntos Usuario"] = puntosUser
                rondaGanadaUser += 1 #Sumar ronda ganada
                print (f'Usuario {rondaGanadaUser} Máquina {rondaGanadaIA}') #Marcador
                if (rondaGanadaUser == 2): #Escudo al tener dos rondas ganadas
                    print (f'{nickname} ha recibido un ESCUDO')
                if (rondaGanadaUser == 3): #Juego ganado
                    print (f'{nickname} ha GANADO el juego')
                    partidaGanadaIA += 1 #Sumar partida ganada
                    jugador['Partida Ganada IA'] = partidaGanadaIA
                    if nickname not in maquina['Jugadores Ganaron']:
                        maquina['Jugadores Ganaron'].append(nickname) #Agregar el nombre del jugador en la lista
                    else:
                        print (f'{nickname} le ha ganado a la máquina nuevamente')
                    juego[nickname] = jugador
                    juego['maquina'] = maquina
                    guardarJuego (juego,JUEGO_BASE)
                    c.pausarPantalla()
                    break
            else: #Parámetros del juego en caso de ganar la máquina
                print (f'La máquina ha GANADO, {nickname} ha perdido')
                puntosIA += 2 #Sumar puntos máquina
                maquina["Puntos IA"] = puntosIA
                rondaGanadaIA += 1 #Sumar ronda ganada máquina
                print (f'Usuario {rondaGanadaUser} Máquina {rondaGanadaIA}') #Marcador
                if (rondaGanadaIA == 2): #Escudo al tener dos rondas ganadas
                    print ("La maquina ha recibido un ESCUDO")
                if (rondaGanadaIA == 3): #Juego Ganado Máquina
                    print ("La maquina ha GANADO el juego")
                    partidaPerdidaIA += 1 #Sumar partida perdida
                    jugador["Partida Perdida IA"] = partidaPerdidaIA
                    maquina['Jugadores Perdieron'].append(nickname) #Agregar eñ nombre del jugador en la lista
                    print (f'El jugador {nickname} ha PERDIDO') 

                    juego[nickname] = jugador
                    juego['maquina'] = maquina
                    guardarJuego (juego,JUEGO_BASE)
                    c.pausarPantalla()
                    break
            #Puntos de jugador y máquina
            print (f'{nickname} ha conseguido {puntosUser} puntos por rondas ganadas.') 
            print (f'Maquina ha conseguido {puntosIA} puntos por rondas ganadas')
        else:
            print ("Error en la opción seleccionada")



