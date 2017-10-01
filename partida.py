# -*- encoding: utf-8 -*-
from sonido import Sonido
from fichas.pool import PoolDeFichas

class Partida(object):

    def __init__(self, pilas, tts):
        self.pilas = pilas
        self.decir = tts
        self.pool = PoolDeFichas(pilas)
        self.reglas = None
        self.tablero = None
        # sonidos de la partida:
        self.sonido_mover = Sonido('audio/mover-ficha.ogg')

    def definir_reglas(self, reglas):
        self.reglas = reglas
        self.reglas.definir_partida(self)

    def definir_tablero(self, tablero):
        self.tablero = tablero
        self.pool.definir_tablero(self.tablero)

    def iniciar(self, *args, **kwargs):
        """Inicia la partida."""
        organizador = self.reglas.obtener_organizador()
        self.tablero.acomodarFichas(organizador(pool=self.pool, *args, **kwargs))

    def seleccionar_celda(self, columna, fila):
        """Realiza una seleccion de celda."""
        self.reglas.seleccionar_celda(columna, fila)

    def registrar_movimiento(self, ficha, celda_origen, celda_destino):
        self.sonido_mover.reproducir()
