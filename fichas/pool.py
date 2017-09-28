# -*- encoding: utf-8 -*-

from actores.ficha import Ficha
from .alfil import Alfil
from .caballo import Caballo
from .dama import Dama
from .peon import Peon
from .rey import Rey
from .torre import Torre

class PoolDeFichas():

    def __init__(self, pilas, cantidadDeFichas=32):
        self.pilas = pilas
        self.fichas = pilas.actores.Grupo()
        self.tablero = None
        self.pilas.log('Se inicia el pool de fichas con', cantidadDeFichas, 'fichas')
        # comportamientos:
        self.comportamientos = {}
        self.comportamientos['alfil']=Alfil
        self.comportamientos['caballo']=Caballo
        self.comportamientos['dama']=Dama
        self.comportamientos['peon']=Peon
        self.comportamientos['rey']=Rey
        self.comportamientos['torre']=Torre

        # iniciamos las fichas:
        for x in range(cantidadDeFichas):
            self.fichas.agregar(Ficha(pilas))

    def definir_tablero(self, tablero):
        self.tablero = tablero

    def generar(self, tipoDeFicha, color):
        ficha = self.buscar_ficha_libre()

        ficha.definir_comportamiento(self.comportamientos[tipoDeFicha](color))
        ficha.definir_tablero(self.tablero)
        return ficha

    def buscar_ficha_libre(self):
        """busca una ficha que este libre.
        si no la encuentra genera una ficha nueva para el pool."""
        for ficha in self.fichas:
            if ficha.no_tiene_comportamiento():
                return ficha

        # no encontro ninguna ficha libre, genera nueva:
        ficha = Ficha(self.pilas)
        fichas.agregar(ficha)
        self.pilas.log("se agranda el pool de fichas, ahora tiene", len(self.fichas), "fichas")
        return ficha
