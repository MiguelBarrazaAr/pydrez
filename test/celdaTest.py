# -*- encoding: utf-8 -*-
import unittest

import pilasengine

from actor.celda import Celda


class TestCelda(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.pilas = pilasengine.iniciar(modo_test=True)
        self.celda = Celda(self.pilas)

    def test_DadoUnaCeldaNueva_seIniciaCon_x_en0(self):
        self.assertEquals(self.celda.x, 0, "x se inicia en 0")

    def test_DadoUnaCeldaNueva_seIniciaCon_y_en0(self):
        self.assertEquals(self.celda.y, 0, "y se inicia en 0")

    def test_DadoUnaCeldaNueva_seIniciaConSinFichas(self):
        self.assertFalse(self.celda.tieneFicha(), "se inicia una celda libre, sin ficha")
