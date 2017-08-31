# -*- encoding: utf-8 -*-

from actor.alfil import Alfil
from actor.caballo import Caballo
from actor.peon import Peon
from actor.reina import Reina
from actor.rey import Rey
from actor.torre import Torre


def armarAjedrezBasico(pilas, tablero):
    acomodarPiezas(pilas, tablero, fila=0, color="blanco")
    acomodarPeones(pilas, tablero, fila=1, color="blanco")
    acomodarPiezas(pilas, tablero, fila=7, color="negro")
    acomodarPeones(pilas, tablero, fila=6, color="negro")

def acomodarPiezas(pilas, tablero, fila, color):
    tablero.posicionar(Torre(pilas, color=color), 0, fila)
    tablero.posicionar(Caballo(pilas, color=color), 1, fila)
    tablero.posicionar(Alfil(pilas, color=color), 2, fila)
    tablero.posicionar(Reina(pilas, color=color), 3, fila)
    tablero.posicionar(Rey(pilas, color=color), 4, fila)
    tablero.posicionar(Alfil(pilas, color=color), 5, fila)
    tablero.posicionar(Caballo(pilas, color=color), 6, fila)
    tablero.posicionar(Torre(pilas, color=color), 7, fila)

def acomodarPeones(pilas, tablero, fila, color):
    for i in range(8):
        tablero.posicionar(Peon(pilas, color=color), i, fila)
