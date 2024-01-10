import re

def crear() -> list:
    tablero = []
    with open("tablero.txt", "r", encoding="utf-8") as archivo:
        for fila in archivo.readlines():
            tablero.append(re.findall(".", fila))
    return tablero

def actualizar(tablero: list, pos_casilla_frente ,posicion):
    tablero[pos_casilla_frente[0]][pos_casilla_frente[1]] = "🤖"
    tablero[posicion[0]][posicion[1]] = "."

def pintar(tablero: list):
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ")
        print("")