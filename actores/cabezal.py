# -*- encoding: utf-8 -*-
from sonido import Sonido
from pilasengine.actores.actor import Actor

class Cabezal(Actor):
    """Representa al cursor del teclado, se puede mover sobre un tablero."""

    def __init__(self, pilas, tablero, tts, demora=30):
        Actor.__init__(self, pilas, x=tablero.x, y=tablero.y)
        self.imagen = "imagenes/cabezal.png"
        self.tablero = tablero
        self.columna=0
        self.fila=0
        self.control = pilas.escena_actual().control
        self.decir=tts
        self.activo = True
        # sonidos:
        self.sonido_mover = Sonido('audio/mover.ogg')
        self.sonido_limite = Sonido('audio/limite.ogg')
        self.x, self.y = self.tablero.posicion_de_celda(self.columna, self.fila)
        self.escala = 2.3

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
        if ubicacion   >= 0 and ubicacion < self.tablero.columnas:
            self.columna = ubicacion
            self.actualizar_posicion()
        else:
            self.error_de_limite()


    def moverseEnFila(self, paso):
        ubicacion = self.fila+paso
        if ubicacion   >= 0 and ubicacion < self.tablero.filas:
            self.fila = ubicacion
            self.actualizar_posicion()
        else:
            self.error_de_limite()

    def mover(self, columna, fila):
        if columna >= 0 and columna < self.tablero.columnas and fila >= 0 and fila < self.tablero.filas:
            self.columna = columna
            self.fila = fila
            self.actualizar_posicion()

    def actualizar_posicion(self):
        self.sonido_mover.reproducir()
        self.leer_ubicacion()
        self.x, self.y = self.tablero.posicion_de_celda(self.columna, self.fila)

    def error_de_limite(self):
        self.sonido_limite.reproducir()

    def leer_ubicacion(self):
        celda = self.tablero.obtener_celda(columna=self.columna, fila=self.fila)
        self.decir(str(celda))

        if celda.ficha:
            self.decir(str(celda.ficha), False)

    def letra_de_columna(self):
        if self.columna >= 0 and self.columna <= 24:
            return chr(self.columna+65)
        else:
            return str(self.columna)
