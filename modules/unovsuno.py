'''
Desarrollo del juego en el modo Uno vs Uno
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

def unoVersusUno (JUEGO_BASE: str):
    juego = cargarJuego(JUEGO_BASE)
    
    nicknameJ1 = input("Ingrese su nickname: ")
    nicknameJ2 = input("Ingrese su nickname: ")
    if (nicknameJ1 not in juego) or (nicknameJ2 not in juego):
        print (f"El nickname {nicknameJ1} no ha sido registrado")
        print (f"El nickname {nicknameJ2} no ha sido registrado")
        c.borrarPantalla()
    
    else:
        rondaGanadaUser1 = 0
        rondaGanadaUser2 = 0
        partidaGanadaUno1 = juego[nicknameJ1].get('Partida Ganada Uno',0)
        partidaPerdidaUno1 = juego[nicknameJ1].get('Partida Perdida Uno', 0)
        puntosUser1 =juego[nicknameJ1].get('Puntos Usuario',0)
        partidaGanadaUno2 = juego[nicknameJ2].get('Partida Ganada Uno',0)
        partidaPerdidaUno2 = juego[nicknameJ2].get('Partida Perdida Uno', 0)
        puntosUser2 =juego[nicknameJ2].get('Puntos Usuario',0)

        jugador1 = {
                'Nombre': '',
                'Nickname': nicknameJ1,
                'Puntos Usuario': puntosUser1,
                'Partida Ganada Uno': partidaGanadaUno1,
                'Partida Perdida Uno': partidaPerdidaUno1
            }
        
        jugador2 = {
                'Nombre': '',
                'Nickname': nicknameJ2,
                'Puntos Usuario': puntosUser2,
                'Partida Ganada Uno': partidaGanadaUno2,
                'Partida Perdida Uno': partidaPerdidaUno2
            }
        
        while (rondaGanadaUser1 < 3) and (rondaGanadaUser2 < 3):
            opciones = ("piedra", "papel", "tijera")
            jugadaUser1 = input ('Ingrese su elección (piedra, papel o tijera): ').casefold()
            jugadaUser2 = input ('Ingrese su elección (piedra, papel o tijera): ').casefold()
            c.borrarPantalla()
            if (jugadaUser1 in opciones) and (jugadaUser2 in opciones):
                print (f'Jugador 1: {jugadaUser1}')
                print (f'Jugador 2: {jugadaUser2}')

                if (jugadaUser1 == jugadaUser2):
                    print ("EMPATE")
                elif (jugadaUser1 == "piedra" and jugadaUser2 == "tijera") or (jugadaUser1 == "tijera" and jugadaUser2 == "papel") or (jugadaUser1 == "papel" and jugadaUser2 == "piedra"):
                    print (f'{nicknameJ1} ha GANADO')
                    puntosUser1 += 2
                    jugador1['Puntos Usuario'] = puntosUser1
                    rondaGanadaUser1 += 1
                    print (f'Jugador 1 {nicknameJ1}:{rondaGanadaUser1} Jugador 2 {nicknameJ2}:{rondaGanadaUser2}')
                    if (rondaGanadaUser1 == 2):
                        print (f'{nicknameJ1} ha recibido un ESCUDO')
                    if (rondaGanadaUser2 == 3):
                        print (f'{nicknameJ1} ha GANADO el juego')
                        partidaGanadaUno1 += 1
                        jugador1['Partida Ganada Uno'] = partidaGanadaUno1
                        partidaPerdidaUno2 += 1
                        jugador2['Partida Perdida Uno'] = partidaPerdidaUno2
                        guardarJuego(juego,JUEGO_BASE)
                        c.pausarPantalla()
                        break
                else:
                    print (f'')



    

   