# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

class Cursor(Actor):
    """Representa al cursor del teclado, se puede mover sobre un tablero."""

    def __init__(self, pilas, tablero, tts, imagen="invisible.png"):
        Actor.__init__(self, pilas, x=tablero.x, y=tablero.y)
        self.imagen = imagen
        self.tablero = tablero
        self.columna=0
        self.fila=0
        self.control = pilas.escena_actual().control
        self.decir=tts
        # sonidos:
        self.sonido_mover = self.pilas.sonidos.cargar('audio/mover.ogg')
        self.sonido_limite = self.pilas.sonidos.cargar('audio/limite.ogg')

    def actualizar(self):
        if self.pilas.control.izquierda:
            self.moverseEnColumna(1)
        if self.pilas.control.derecha:
            self.moverseEnColumna(-1)
        if self.pilas.control.arriba:
            self.moverseEnFila(1)
        if self.pilas.control.abajo:
            self.moverseEnFila(-1)
        if self.pilas.control.boton:
            self.decir("pulsado")

    def moverseEnColumna(self, paso):
        ubicacion = self.columna+paso
        if ubicacion   >= 0 or ubicacion <= self.tablero.columnas:
            self.sonido_mover.reproducir()
            self.columna = ubicacion
        else:
            self.sonido_limite.reproducir()


    def moverseEnFila(self, paso):
        self.decir("fila")
        print("c")
