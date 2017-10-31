# -*- encoding: utf-8 -*-
import unittest

from modelo.fichas.ficha import Ficha


class TestFicha(unittest.TestCase):

    def setUp(self):
        self.ficha = Ficha("blanco", (1,2))

    def test_dadoUnaFichaNuevaSeIniciaConElBandoBrindadoEnElConstructor(self):
        self.assertEquals(self.ficha.bando, "blanco", "el color debe ser blanco.")

    def test_dadoUnaFichaSeIniciaEnLaColumnaIndicadaPorConstructor(self):
        self.assertEquals(self.ficha.columna, 1, "la columna es 1.")

    def test_dadoUnaFichaSeIniciaEnLaFilaIndicadaPorConstructor(self):
        self.assertEquals(self.ficha.fila, 2, "la columna es 2.")

    def test_dadoUnaFicha_suValorPorDefaultEs3(self):
        self.assertEquals(self.ficha.valor(), 3, "el valor default es 3.")

    def test_dadoUnaFicha_noPuedeMoversePorElTablero(self):
        self.assertFalse(self.ficha.puedeMoverA((0,2), None), "por default no puede moverse por el tablero.")
