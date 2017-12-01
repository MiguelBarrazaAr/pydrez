# -*- encoding: utf-8 -*-
from organizadores.ajedrez_basico import AjedrezTradicional
from organizadores.acomodar_fichas import AcomodarFichas

class Reglas(object):

    def __init__(self, personalizado=False):
        self.bandos = ['blanco', 'negro']
        self.turno = 0
        self.partida = None
        self.celda_seleccionada = None
        self.dimensionTablero = (8, 8)
        self.personalizado = personalizado
        self.organizador = None

    def iniciar(self, *args, **kwargs):
        """configura el inicio de una partida"""
        if self.organizador is None:
            self.organizador = self.obtener_organizador()
            self.partida.tablero.eliminarCeldas()
            self.partida.tablero.columnas = self.dimensionTablero[0]
            self.partida.tablero.filas = self.dimensionTablero[1]
            self.partida.tablero.graficar()
        self.partida.tablero.acomodarFichas(self.organizador(pool=self.partida.pool, *args, **kwargs))
        self.partida.activa = True
        self.partida.turno = self.bandos[self.turno]
        self.posIniciar()

    def PosIniciar(self):
        """metodo que se ejecuta despues de iniciar la partida.
        se debe sobreescribir si es necesario"""
        return None

    def definir_partida(self, partida):
        self.partida = partida

    def pasar_turno(self):
        self.turno = (self.turno+1)%2
        self.partida.turno = self.bandos[self.turno]
        if self.turno == 0:
            self.partida.cantTurnos+=1

    def turno_actual(self):
        return self.bandos[self.turno]

    def obtener_organizador(self):
        """retorna el organizador de fichas en el tablero"""
        if self.personalizado:
            return AcomodarFichas
        else:
            return AjedrezTradicional

    def decir(self, texto, interrumpir=True):
        self.partida.decir(texto, interrumpir)

    def log(self, *args, **kwargs):
        self.partida.pilas.log(*args, **kwargs)

    def seleccionar_celda(self, columna, fila):
        """metodo que se ejecuta al seleccionar una celda.
        este metodo se debe redefinir"""
        pass
