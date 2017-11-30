# -*- encoding: utf-8 -*-
import reglas
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
        self.cantTurnos = 0
        if datos is None:
            self.datos = {}
            self.activa = False
        else:
            self.datos = datos
            self.activa = True

        # eventos de la partida:
        self.eventoPreMueveFicha = pilas.evento.Evento("registra_movimiento")
        self.eventoMueveFicha = pilas.evento.Evento("mueve_ficha")
        self.eventoFinalizar = pilas.evento.Evento("finaliza_partida")

    def definir_reglas(self, clave):
        self.reglas = reglas.generar(clave)()
        self.reglas.definir_partida(self)

    def definir_tablero(self, tablero):
        self.tablero = tablero
        self.pool.definir_tablero(self.tablero)

    def iniciar(self, *args, **kwargs):
        """Inicia la partida.
        precondicion: debe tener cargada las reglas y definido un tablero."""
        # falta validar precondicion.
        if self.activa:
            self.pool.cargarPosicion(self.datos['posicion'])
            self.cantMovimientos = self.datos['movimientos']
            self._turno = self.datos['turno']
        else:
            self.cantMovimientos = 0
            self.reglas.iniciar(*args, **kwargs)
            self.datos['posicion'] = self.pool.posicion()
            self.datos['movimientos'] = self.cantMovimientos
            self.datos['turno'] = self._turno

    def reiniciar(self):
        """reinicia la partida."""
        # elimina las fichas del tablero.
        # reinicia el historial de movimientos.
        # vuelve a iniciar la partida.
        self.datos = {}
        self.pool.limpiar()
        self.reglas.iniciar(*args, **kwargs)

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
        self.eventoPreMueveFicha.emitir(ficha=ficha, fichaEliminada=fichaEliminada, celdaOrigen=celdaOrigen, celdaDestino=celdaDestino)

    def finalizaMovimiento(self, celda):
        posicion = self.pool.posicion()
        self.datos['posicion'] = posicion
        self.cantMovimientos += 1
        self.datos['movimientos'] = self.cantMovimientos
        self.eventoMueveFicha.emitir(posicion=posicion, celda=celda, turno=self.turno)
