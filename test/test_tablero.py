# -*- encoding: utf-8 -*-
import unittest

from modelo.tablero import Tablero


class TestTablero(unittest.TestCase):

    #@classmethod
    def setUp(self):
        self.tablero4x4 = Tablero(filas=4, columnas=4)
        self.tablero = Tablero(filas=8, columnas=8)
        self.peon = "peon"

    def test_DadoUnTableroDe8x8_debeTenerColumnaIgualA8(self):
        self.assertEquals(self.tablero.columnas, 8, "cantidad de columnas incorrecta")

    def test_DadoUnTableroDe8x8_debeTenerFilaIgualA8(self):
        self.assertEquals(self.tablero.filas, 8, "cantidad de filas incorrecta")

    def test_DadoUnTablero_noTieneCeldasConFichas(self):
        celdas = self.tablero.celdasActivas()
        self.assertEquals(len(celdas), 0, "no tiene celdas activas")

    def test_DadoUnTablero_siSeAgregaUnaFichaTieneUnaCeldaActiva(self):
        self.tablero.agregar((0, 0), self.peon)
        celdas = self.tablero.celdasActivas()
        self.assertEquals(len(celdas), 1, "tiene una celda activas")

    def test_DadoUnTablero_laCelda_0_0_estaLibre(self):
        self.assertTrue(self.tablero.estaLibre((0, 0)), "la celda 0 0 esta libre.")

    def test_DadoUnTablero_conUnaFichaEnLaCelda_0_0_estaNoEstaLibre(self):
        self.tablero.agregar((0, 0), self.peon)
        self.assertFalse(self.tablero.estaLibre((0, 0)), "la celda 0 0 no esta libre.")

    def test_DadoUnTablero_conUnaFichaEnLaCelda_0_0_siSePideSuValorEstaRetornaLaMismaFicha(self):
        self.tablero.agregar((0, 0), self.peon)
        self.assertEquals(self.tablero.valor((0, 0)), self.peon, "tiene un peon en la celda 0 0.")

    def test_DadoUnTablero_conUnaFichaEnLaCelda_0_0_siSeEliminaDichaFichaLaCeldaQuedaLibre(self):
        self.tablero.agregar((0, 0), self.peon)
        self.tablero.eliminar((0, 0))
        self.assertTrue(self.tablero.estaLibre((0, 0)), "la celda 0 0 esta libre luego de eliminar la ficha.")

    def test_DadoUnTablero_siSeAgregaUnaFichaEnLaCelda_0_0_yLuegoSeElimina_noTieneCeldasActivas(self):
        self.tablero.agregar((0, 0), self.peon)
        self.tablero.eliminar((0, 0))
        celdas = self.tablero.celdasActivas()
        self.assertEquals(len(celdas), 0, "no tiene celdas activas")
