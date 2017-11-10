# -*- encoding: utf-8 -*-
from fichas.pool import PoolDeFichas

from tts import leer as tts

class Partida(object):

    def __init__(self, pilas, datos=None):
        self.pilas = pilas
        self.decir = tts
        self.pool = PoolDeFichas(pilas)
        self.reglas = None
        self.tablero = None
        # datos de la partida:
        self._turno = ""
        self.datos = {}

        if datos is None:
            self.activa = False
        else:
            self.activa = True
            self.cargarDatos(datos)

        # eventos de la partida:
        self.eventoMueveFicha = pilas.evento.Evento("mueve_ficha")
        self.eventoFinalizar = pilas.evento.Evento("finaliza_partida")

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
        self.cantMovimientos = 0
        self.datos['posicion'] = self.pool.posicion
        self.datos['movimientos'] = self.cantMovimientos
        self.datos['turno'] = self._turno

    def reiniciar(self):
        """reinicia la partida."""
        # elimina las fichas del tablero.
        # reinicia el historial de movimientos.
        # vuelve a iniciar la partida.
        self.datos = {}

    def finalizar(self, motivo):
        """finaliza la partida
        : param motivo: se refiere al motivo por el cual finaliza esta partida."""
        self.activa = False
        self.datos = {}
        self.eventoFinalizar.emitir(motivo=motivo)

    def seleccionar_celda(self, columna, fila):
        """Realiza una seleccion de celda si la partida esta activa"""
        if self.activa:
            self.reglas.seleccionar_celda(columna, fila)

    def registrar_movimiento(self, ficha, fichaEliminada, celdaOrigen, celdaDestino):
        self.datos['posicion'] = self.pool.posicion
        self.cantMovimientos += 1
        self.datos['movimientos'] = self.cantMovimientos
        self.eventoMueveFicha.emitir(ficha=ficha, fichaEliminada=fichaEliminada, celdaOrigen=celdaOrigen, celdaDestino=celdaDestino)

    def cargarDatos(self, datos):
        self.datos = datos
