# -*- encoding: utf-8 -*-
from actores.historial import Historial
from sonido import Sonido
from fichas.pool import PoolDeFichas

class Partida(object):

    def __init__(self, pilas, tts):
        self.pilas = pilas
        self.decir = tts
        self.pool = PoolDeFichas(pilas)
        self.reglas = None
        self.tablero = None
        self.activa = False
        # sonidos de la partida:
        self.sonido_mover = Sonido('audio/mover-ficha.ogg')
        self.historial = Historial(pilas,130,140)

    def definir_reglas(self, reglas):
        self.reglas = reglas
        self.reglas.definir_partida(self)

    def definir_tablero(self, tablero):
        self.tablero = tablero
        self.pool.definir_tablero(self.tablero)

    def iniciar(self, *args, **kwargs):
        """Inicia la partida.
        precondicion: debe tener cargada las reglas y definido un tablero."""
        # falta validar precondicion.
        #if not self.activa:
        self.reglas.iniciar(*args, **kwargs)

    def reiniciar(self):
        """reinicia la partida."""
        # elimina las fichas del tablero.
        # reinicia el historial de movimientos.
        # vuelve a iniciar la partida.
        print("reiniciando")
        pass

    def finalizar(self, mensaje, audio=None):
        """finaliza la partida"""
        self.activa = False
        self.decir(mensaje, False)
        self.pilas.avisar(mensaje)

    def seleccionar_celda(self, columna, fila):
        """Realiza una seleccion de celda si la partida esta activa"""
        if self.activa:
            self.reglas.seleccionar_celda(columna, fila)

    def registrar_movimiento(self, ficha, fichaEliminada, celda_origen, celda_destino):
        self.sonido_mover.reproducir()
        if fichaEliminada:
            #print("fuera de juego", fichaEliminada.nombre,  fichaEliminada.color)
            self.historial.agregar(repr(ficha) +  "x" + str(celda_destino))
        else:
            self.historial.agregar(repr(ficha) + str(celda_destino))
