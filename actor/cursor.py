# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

class Cursor(Actor):
    """Representa al cursor del teclado, se puede mover sobre un tablero."""

    def __init__(self, pilas, tablero, tts, demora=30):
        Actor.__init__(self, pilas, x=tablero.x, y=tablero.y)
        self.imagen = "imagenes/cabezal.png"
        self.tablero = tablero
        self.columna=1
        self.fila=1
        self.control = pilas.escena_actual().control
        self.decir=tts
        self.activo = True
        # sonidos:
        self.sonido_mover = self.pilas.sonidos.cargar('audio/mover.ogg')
        self.sonido_limite = self.pilas.sonidos.cargar('audio/limite.ogg')
        self.x, self.y = self.tablero.posicion_de_celda(self.columna, self.fila)

    def mover_izquierda(self):
        self.moverseEnColumna(-1)

    def mover_derecha(self):
        self.moverseEnColumna(1)

    def mover_arriba(self):
        self.moverseEnFila(1)

    def mover_abajo(self):
        self.moverseEnFila(-1)

    def moverseEnColumna(self, paso):
        ubicacion = self.columna+paso
        if ubicacion   >= 1 or ubicacion <= self.tablero.columnas:
            self.columna = ubicacion
            self.actualizar_posicion()
        else:
            self.error_de_limite()


    def moverseEnFila(self, paso):
        ubicacion = self.fila+paso
        if ubicacion   >= 1 or ubicacion <= self.tablero.filas:
            self.fila = ubicacion
            self.actualizar_posicion()
        else:
            self.error_de_limite()

    def actualizar_posicion(self):
        self.sonido_mover.reproducir()
        self.leer_ubicacion()
        self.x, self.y = self.tablero.posicion_de_celda(self.columna, self.fila)

    def error_de_limite(self):
        self.sonido_limite.reproducir()

    def leer_ubicacion(self):
        self.decir(self.letra_de_columna()+str(self.fila))

    def letra_de_columna(self):
        if self.columna == 2:
            return "a"
        elif self.columna == 2:
            return "2"
        elif self.columna == 3:
            return "c"
        elif self.columna == 4:
            return "d"
        elif self.columna == 5:
            return "e"
        elif self.columna == 6:
            return "f"
        elif self.columna == 7:
            return "g"
        elif self.columna == 8:
            return "h"
