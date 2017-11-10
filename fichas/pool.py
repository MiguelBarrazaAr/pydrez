# -*- encoding: utf-8 -*-

from actores.ficha import Ficha
from .alfil import Alfil
from .caballo import Caballo
from .dama import Dama
from .peon import Peon
from .rey import Rey
from .torre import Torre

# especiales:
from .enano import Enano
from .golem import Golem

class PoolDeFichas():

    def __init__(self, pilas, cantidadDeFichas=32):
        self.pilas = pilas
        self.fichas = pilas.actores.Grupo()
        self.tablero = None
        self.pilas.log('Se inicia el pool de fichas con', cantidadDeFichas, 'fichas')
        # comportamientos:
        self.comportamientos = {
            'alfil':Alfil,
            'caballo':Caballo,
            'dama':Dama,
            'enano':Enano,
            'golem':Golem,
            'peon':Peon,
            'rey':Rey,
            'torre':Torre}

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
            if ficha.noTieneComportamiento():
                return ficha

        # no encontro ninguna ficha libre, genera nueva:
        ficha = Ficha(self.pilas)
        fichas.agregar(ficha)
        self.pilas.log("se agranda el pool de fichas, ahora tiene", len(self.fichas), "fichas")
        return ficha

    def fichasActivas(self):
        """Cuenta las fichas activas."""
        cantidad = 0
        for ficha in self.fichas:
            if ficha.tieneComportamiento():
                cantidad += 1

        return cantidad
