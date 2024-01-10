import threading
import time
from os import system
import Tablero



def ubicar_robot():
    for y in range(len(tablero)):
        for x in range(len(tablero[y])):
            if tablero[y][x] in ["N", "S", "L", "O"]:
                return [y, x]

def orientar_robot(posicion):
    return direcciones[tablero[posicion[0]][posicion[1]]]

def pos_casilla_frente_robot(posicion, orientacion):
    return posicion[0] + orientacion[0], posicion[1] + orientacion[1] 

def girar_robot(orientacion, es_sentido_horario: bool):
    listaDirecciones = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    direccion_giro =  1 if es_sentido_horario else -1
    nueva_orientacion = listaDirecciones.index(orientacion) + direccion_giro
    if nueva_orientacion < 0:
        return listaDirecciones[3]
    if nueva_orientacion > len(listaDirecciones) - 1:
        return listaDirecciones[0]
    
    return listaDirecciones[nueva_orientacion]




def juego():

    
        

    
    posicionDelRobot = ubicar_robot()
    orientacionDelRobot = orientar_robot(posicionDelRobot)
    stickersJuntados = 0
    contadorSegundos = 0
    instrucciones = input("Ingrese las instrucciones que le dara al robot" 
                          "\n\t- 'F' (Mover al frente)\n\t- 'D' (Girar a la derecha)\n\t- 'E' (Girar a la izquierda)\n➡️  ")
    while instrucciones != "":
        instruccion = instrucciones[0]
        system("cls")
        if instruccion == "F":
            pos_casilla_frente = pos_casilla_frente_robot(posicionDelRobot, orientacionDelRobot)
            try:
                casilla_frente = tablero[pos_casilla_frente[0]][pos_casilla_frente[1]]
            except:
                casilla_frente = "#" 
            if  casilla_frente != "#":
                if casilla_frente == "*":
                    stickersJuntados += 1
                Tablero.actualizar(tablero=tablero, pos_casilla_frente=pos_casilla_frente, posicion=posicionDelRobot)
                posicionDelRobot = pos_casilla_frente
        elif instruccion == "D":
            orientacionDelRobot  = girar_robot(orientacionDelRobot, True)
        elif instruccion == "E":
            orientacionDelRobot = girar_robot(orientacionDelRobot, False)

        Tablero.pintar(tablero)
        contadorSegundos += 1
        instrucciones = instrucciones[1:]
        print(f"Segundos: {contadorSegundos}, posicion del robot: {posicionDelRobot}, "
                f"orientacion del robot: {orientacionDelRobot}"
                f"frente del robot {pos_casilla_frente_robot(posicionDelRobot, orientacionDelRobot)}"
                f"stickers juntados: {stickersJuntados}")
        time.sleep(1)


direcciones = {"N": [-1, 0], "L": [0, 1], "S": [1, 0], "O": [0, -1]}
tablero = Tablero.crear()

t = threading.Thread(target=juego)
t.start()