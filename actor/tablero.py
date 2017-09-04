# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

from celda import Celda

class Tablero(Actor):
    """Representa al tablero"""

    def __init__(self, pilas, x=0, y=0, columnas=8, filas=8):
        """Constructor del tablero:

        :param x: x del punto central de a1 (casilla inferior izquierda).
        :type x: int
        :param y: y del punto central de a1
        :type y: int
        :param columnas: cantidad de columnas que tendra el tablero.
        :type columnas: int
        :param filas: cantidad de filas
        :type filas: int
        """

        Actor.__init__(self, pilas, x=x, y=y)
        self.imagen = "invisible.png"
        self.columnas = columnas
        self.filas = filas
        self.distancia = 30
        self.celda = []
        self.ficha = []
        #self.radio_de_colision = None

        color = 'negro'
        for f in range(filas):
            self.celda.append([])
            for c in range(columnas):
                self.celda[f].append(Celda(pilas, x=(x+c*self.distancia), y=(y+f*self.distancia), z=100, color=color))

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

    def posicionar(self, actor, columna, fila):
        """Posiciona un actor en una casilla del tablero
        y lo almacena como actor activo dentro del tablero.

        :param actor: un actor a posicionar en una casilla del tablero.
        :type actor: Actor
        :param columna: numero de columna en la que se posicionará (0..n)
        :type columna: int
        :param fila: numero de fila (0..n)
        :type fila: int
        """

        actor.x=self.x+columna*self.distancia
        actor.y=self.y+fila*self.distancia
        self.ficha.append(actor)
