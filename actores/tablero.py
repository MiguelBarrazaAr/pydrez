# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

from celda import Celda

class Tablero(Actor):
    """Representa al tablero"""

    def __init__(self, pilas, x=0, y=0, columnas=8, filas=8, centrado=False, estiloDeCelda="celda", tts=None):
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
        :param centrado: indica si el tablero estar� centrado.
        :type centrado: bool
        """

        self.distancia = 45
        # si esta centrado calculamos su posici�n:
        if centrado:
            x = pilas.camara.x+columnas/2*self.distancia*-1
            y = pilas.camara.y+filas/2*self.distancia*-1

        Actor.__init__(self, pilas, x=x, y=y, imagen='invisible.png')
        self.columnas = columnas
        self.filas = filas
        self.celda = []
        self.celda_seleccionada = None
        self.ficha = []
        #self.radio_de_colision = None
        self.decir = tts

        color = 'negro'
        for f in range(filas):
            self.celda.append([])
            for c in range(columnas):
                self.celda[f].append(Celda(pilas, x=(x+c*self.distancia), y=(y+f*self.distancia), z=100, color=color, columna=c, fila=f, estiloDeCelda=estiloDeCelda))

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
