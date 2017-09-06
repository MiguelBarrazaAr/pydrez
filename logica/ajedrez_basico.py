# -*- encoding: utf-8 -*-

from actor.alfil import Alfil
from actor.caballo import Caballo
from actor.peon import Peon
from actor.reina import Reina
from actor.rey import Rey
from actor.torre import Torre

class AjedrezTradicional():

    def acomodar(self, tablero):
        # acomoda las fichas de un ajedrez tradicional:
        self.acomodarPiezas(tablero, fila=0, color="blanco")
        self.acomodarPeones(tablero, fila=1, color="blanco")
        self.acomodarPiezas(tablero, fila=7, color="negro")
        self.acomodarPeones(tablero, fila=6, color="negro")

    def acomodarPiezas(self, tablero, fila, color):
        tablero.posicionar(Torre(tablero.pilas, color=color), 0, fila)
        tablero.posicionar(Caballo(tablero.pilas, color=color), 1, fila)
        tablero.posicionar(Alfil(tablero.pilas, color=color), 2, fila)
        tablero.posicionar(Reina(tablero.pilas, color=color), 3, fila)
        tablero.posicionar(Rey(tablero.pilas, color=color), 4, fila)
        tablero.posicionar(Alfil(tablero.pilas, color=color), 5, fila)
        tablero.posicionar(Caballo(tablero.pilas, color=color), 6, fila)
        tablero.posicionar(Torre(tablero.pilas, color=color), 7, fila)

    def acomodarPeones(self, tablero, fila, color):
        for i in range(8):
            tablero.posicionar(Peon(tablero.pilas, color=color), i, fila)
