# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

from celda import *

class Tablero(Actor):
    """Representa al tablero"""

    def __init__(self, pilas, x=0, y=0, alto=8, ancho=8):
        """Constructor del tablero:
        :param x: x del punto central de a1 (casilla inferior izquierda).
        :type x: int
        :param y: y del punto central de a1
        :type y: int
        :param ancho: cantidad de casillas a lo ancho del tablero
        :type ancho: int
        :param alto: cantidad de casillas a lo alto.
        :type ancho: int
        """

        self._alto = alto
        self._ancho = ancho
        self._x = x
        self._y = y
        self.distancia = 30
        self.celda = Celda(pilas) * (alto * ancho)
        #self.z = 5
        #self.radio_de_colision = None

        negro = True
        h=0
        w=0
        for c in self.celda:
            c.x=x+w*self.distancia
            c.y=y+h*self.distancia
            c.z=100

            # coloreamos la celda:
            if negro:
                c.colorearNegro()


            w+=1
            # si llegamos al final de la fila volvemos al principio y subimos:
            if w == ancho:
                w=0
                h+=1
                if (ancho%2) == 1:
                    negro = not negro
            else:
                negro = not negro

    def posicionar(self, actor, x, y):
        """Posiciona un actor en una casilla del tablero
        y lo almacena como actor activo dentro del tablero.

        :param actor: un actor a posicionar en una casilla del tablero.
        :type actor: Actor
        :param x: numero de columna en la que se posicionará (0..n)
        :type x: int
        :param y: numero de fila (0..n)
        :type y: int
        """

        actor.x=self._x+x*self.distancia
        actor.y=self._y+y*self.distancia
