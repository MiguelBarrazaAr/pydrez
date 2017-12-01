# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

from celda import Celda

class Tablero(Actor):
    """Representa al tablero"""

    def __init__(self, pilas, x=0, y=0, columnas=0, filas=0, estiloDeCelda="celda"):
        """Constructor del tablero:

        :param x: x del punto central de a1 (casilla inferior izquierda).
        :type x: int
        :param y: y del punto central de a1
        :type y: int
        :param columnas: cantidad de columnas que tendra el tablero.
        :type columnas: int
        :param filas: cantidad de filas
        :type filas: int
        :param estiloDeCelda: nombre de la carpeta donde se encuentra las imagenes de las celdas. relativas a: /imagenes/(nombre de estilo)
        :type estiloDeCelda: string
        """

        self.distancia = 69
        Actor.__init__(self, pilas, x=x, y=y, imagen='invisible.png')
        self.columnas = columnas
        self.filas = filas
        self.estiloDeCelda = estiloDeCelda
        self.celda = []
        self.ficha = []
        if columnas > 0 and filas > 0:
            self.graficar()

    def graficar(self):
        color = 'negro'
        for f in range(self.filas):
            self.celda.append([])
            for c in range(self.columnas):
                self.celda[f].append(Celda(self.pilas,
                    x=(self.x+c*self.distancia),
                    y=(self.y+f*self.distancia),
                    z=100,
                    color=color,
                    columna=c, fila=f,
                    estiloDeCelda=self.estiloDeCelda))

                # invertimos el color:
                if color == 'negro':
                    color = 'blanco'
                else:
                    color = 'negro'

            if (f%2) == 1:
                # la siguiente fila es par, es negro:
                color = 'negro'
            else:
                # la siguiente fila es impar, es blanco:
                color = 'blanco'

    def eliminarCeldas(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                del self.celda[f][c]

    def acomodarFichas(self, loader):
        loader.acomodar(tablero=self)

    def posicionar(self, ficha, columna, fila):
        """Posiciona un actor en una casilla del tablero
        y lo almacena como actor activo dentro del tablero.

        :param actor: una ficha a Agregarlo al juego.
        :type actor: Actor
        :param columna: numero de columna en la que se posicionar� (1..n)
        :type columna: int
        :param fila: numero de fila (1..n)
        :type fila: int
        """

        self.celda[fila][columna].ponerFicha(ficha)

    def obtener_celda(self, columna, fila):
        return self.celda[fila][columna]

    def obtenerFicha(self, columna, fila):
        return self.celda[fila][columna].ficha

    def posicion_de_celda(self, columna, fila):
        return self.x+(columna*self.distancia), self.y+(fila*self.distancia)

    def obteneer_celdas_lindantes(self, fila, columna):
        celdas_lindantes = []
        lindantes = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for x in lindantes:
            if (columna + x[0] >= 0 and columna + x[0] <= self.filas - 1)and (fila + x[1] >= 0 and fila + x[1] <= self.columnas - 1):
               celdas_lindantes.append(self.obtener_celda(columna + x[0], fila + x[1]))

        return celdas_lindantes

    def elimiraPieza(self, celda):
        ficha = celda.ficha
        if ficha is not None:
            celda.liberar()
            ficha.eliminar()