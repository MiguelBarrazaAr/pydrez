# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

class Cursor(Actor):
    """Representa al cursor del teclado, se puede mover sobre un tablero."""

    def __init__(self, pilas, tablero, imagen="invisible.png"):
        Actor.__init__(self, pilas, x=tablero.x, y=tablero.y)
        self.imagen = imagen
        self.tablero = tablero
        self.columna=0
        self.fila=0
