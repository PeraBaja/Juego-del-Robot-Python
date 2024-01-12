import re
from Vectores import Vector
def crear() -> list:
    tablero = []
    with open("tablero.txt", "r", encoding="utf-8") as archivo:
        for fila in archivo.readlines():
            tablero.append(re.findall(".", fila))
    return tablero

def actualizar(tablero: list, pos_casilla_frente: Vector,posicion: Vector):
    tablero[pos_casilla_frente.y][pos_casilla_frente.x] = "🤖"
    tablero[posicion.y][posicion.x] = "."

def pintar(tablero: list):
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ")
        print("")