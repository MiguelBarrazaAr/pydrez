# -*- encoding: utf-8 -*-
from fichas.pool import PoolDeFichas

class Partida(object):

    def __init__(self, pilas, tts):
        self.pilas = pilas
        self.decir = tts
        self.pool = PoolDeFichas(pilas)
        self.reglas = None
        self.tablero = None

    def definir_reglas(self, reglas):
        self.reglas = reglas

    def definir_tablero(self, tablero):
        self.tablero = tablero
        self.pool.definir_tablero(self.tablero)

    def iniciar(self):
        """Inicia la partida."""
        organizador = self.reglas.obtener_organizador()
        self.tablero.acomodarFichas(organizador(self.pool))
