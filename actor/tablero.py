# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

from celda import Celda

class Tablero(Actor):
    """Representa al tablero"""

    def __init__(self, pilas, x=0, y=0, columnas=8, filas=8, centrado=False, tts=None):
        """Constructor del tablero:

        :param x: x del punto central de a1 (casilla inferior izquierda).
        :type x: int
        :param y: y del punto central de a1
        :type y: int
        :param columnas: cantidad de columnas que tendra el tablero.
        :type columnas: int
        :param filas: cantidad de filas
        :type filas: int
        :param centrado: indica si el tablero estará centrado.
        :type centrado: bool
        """

        self.distancia = 30
        # si esta centrado calculamos su posición:
        if centrado:
            x = pilas.camara.x+columnas/2*self.distancia*-1
            y = pilas.camara.y+filas/2*self.distancia*-1

        Actor.__init__(self, pilas, x=x, y=y, imagen='invisible.png')
        #self.imagen = "invisible.png"
        self.columnas = columnas
        self.filas = filas
        self.celda = []
        self.celda_seleccionada = None
        self.ficha = []
        #self.radio_de_colision = None
        self.decir = tts
        self.sonido_mover = self.pilas.sonidos.cargar('audio/mover-ficha.ogg')

        color = 'negro'
        for f in range(filas):
            self.celda.append([])
            for c in range(columnas):
                self.celda[f].append(Celda(pilas, x=(x+c*self.distancia), y=(y+f*self.distancia), z=100, color=color, columna=c, fila=f))

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
        :param columna: numero de columna en la que se posicionará (1..n)
        :type columna: int
        :param fila: numero de fila (1..n)
        :type fila: int
        """

        self.celda[fila][columna].ponerFicha(ficha)

    def obtenerFicha(self, columna, fila):
        return self.celda[fila][columna].ficha

    def posicion_de_celda(self, columna, fila):
        return self.x+(columna*self.distancia), self.y+(fila*self.distancia)

    def seleccionar(self, columna, fila):
        """selecciona una celda.
        solo se puede seleccionar celdas que tienen fichas.
        si ya hay una seleccionada realiza un movimiento
        """
        if self.celda_seleccionada is None:
            # si no hay ninguna celda seleccionada:
            if self.celda[fila][columna].tieneFicha():
                # seleccionamos la celda:
                self.celda_seleccionada = self.celda[fila][columna]
                self.celda_seleccionada.seleccionar()
                self.decir(str(self.celda_seleccionada.ficha)+" seleccionado")

        else:
            # si ya hay celda seleccionada:
            if self.celda_seleccionada.columna == columna and  self.celda_seleccionada.fila == fila:
                # si selecciona 2 veces la misma celda la deselecciona.
                self.decir(str(self.celda_seleccionada.ficha)+" deseleccionado")
                self.deseleccionarCelda()
            else:
                # si selecciona otra celda realiza el movimiento:
                if self.celda_seleccionada.ficha.moverA(columna=columna, fila=fila):
                    # pudo realizar el movimiento:
                    self.sonido_mover.reproducir()
                    self.deseleccionarCelda()
                else:
                    # no puede realizar el movimiento:
                    self.deseleccionarCelda()
                    self.movimiento_imposible()

    def deseleccionarCelda(self):
        """deselecciona una celda seleccionada:
        precondición: debe haber una celda seleccionada.
        la propiedad: celda_seleccionada no debe ser None"""
        self.celda_seleccionada.deseleccionar()
        self.celda_seleccionada = None

    def movimiento_imposible(self):
        """metodo que se ejecuta cuando un jugador realiza un movimiento imposible"""
        self.decir("movimiento imposible")
