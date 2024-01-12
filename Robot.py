from Vectores import Vector
import Tablero
class Robot:

    direcciones = {"N": Vector(-1, 0), "E": Vector(0, 1), "S": Vector(1, 0), "O": Vector(0, -1)}

    def __init__(self, tablero) -> None:
        self.posicion = Robot.ubicar(tablero)
        self.orientacion = Robot.orientar(posicion=self.posicion, tablero=tablero)
     

    def ubicar(tablero: list) -> Vector:
        for y in range(len(tablero)):
            for x in range(len(tablero[y])):
                if tablero[y][x] in Robot.direcciones.keys():
                    return Vector(y, x)

    def orientar(posicion: Vector, tablero: list) -> Vector:
        return Robot.direcciones[tablero[posicion.y][posicion.x]]

    def pos_casilla_frente(self) -> Vector:
        return Vector(self.posicion.y + self.orientacion.y, self.posicion.x + self.orientacion.x) 

    def mover(self, tablero):
        pos_casilla_frente = self.pos_casilla_frente()
        try:
            casilla_frente = tablero[pos_casilla_frente.y][pos_casilla_frente.x]
        except:
            casilla_frente = "#" 
        if  casilla_frente != "#":
            if casilla_frente == "*":
                stickersJuntados += 1
            Tablero.actualizar(tablero=tablero, pos_casilla_frente=pos_casilla_frente, posicion=self.posicion)
            self.posicion = pos_casilla_frente

    def girar(self, es_sentido_horario: bool) -> None:
        listaDirecciones = []
        for direccion in Robot.direcciones.values():
            listaDirecciones.append(direccion)
        direccion_giro =  1 if es_sentido_horario else -1
        nueva_orientacion = listaDirecciones.index(self.orientacion) + direccion_giro
        if nueva_orientacion < 0:
            self.orientacion = listaDirecciones[3]
        elif nueva_orientacion > len(listaDirecciones) - 1:
            self.orientacion = listaDirecciones[0]
        else:
            self.orientacion = listaDirecciones[nueva_orientacion]

