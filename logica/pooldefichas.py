# -*- encoding: utf-8 -*-

from actor.alfil import Alfil
from actor.caballo import Caballo
from actor.peon import Peon
from actor.reina import Reina
from actor.rey import Rey
from actor.torre import Torre

class PoolDeFichas():

    def __init__(self, pilas):
        self.pilas = pilas
        self.activas = []
        self.eliminadas = []
        self.tablero = None
        # generador:
        self.generador = {}
        self.generador['alfil']=Alfil
        self.generador['caballo']=Caballo
        self.generador['peon']=Peon
        self.generador['reina']=Reina
        self.generador['rey']=Rey
        self.generador['torre']=Torre

    def definir_tablero(self, tablero):
        self.tablero = tablero

    def generar(self, tipoDeFicha, color):
        ficha = self.generador[tipoDeFicha](self.pilas, color=color)
        ficha.definir_tablero(self.tablero)
        return ficha
