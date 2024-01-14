import threading
import time
from os import system
import Tablero
from Robot import Robot

def juego():
    robot = Robot(tablero)
    stickersJuntados = 0
    contadorSegundos = 0
    instrucciones = input("Ingrese las instrucciones que le dara al robot" 
                          "\n\t- 'F' (Mover al frente)\n\t- 'D' (Girar a la derecha)\n\t- 'I' (Girar a la izquierda)\n➡️  ")
    while instrucciones != "":
        system("cls")
    
        instruccion = instrucciones[0]
        match instruccion:
            case "F":
                robot.mover(tablero)
            case "D":
                robot.girar(True)
            case "I":
                robot.girar(False)
            case _:
                print("❌ Error. Movimiento no valido", instruccion)

        Tablero.pintar(tablero)
        contadorSegundos += 1
        instrucciones = instrucciones[1:]
        
        print(f"Segundos: {contadorSegundos}, posicion del robot: {robot.posicion.en_tupla()}, "
                f"orientacion del robot: {robot.orientacion.en_tupla()}"
                f"frente del robot {robot.pos_casilla_frente().en_tupla()}"
                f"stickers juntados: {stickersJuntados}")
        time.sleep(1)

tablero = Tablero.crear()

t = threading.Thread(target=juego)
t.start()