# -*- encoding: utf-8 -*-
import unittest

import pilasengine

from actor.peon import Peon

class TestPeon(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.pilas = pilasengine.iniciar(modo_test=True)
        self.peon= Peon(self.pilas, color="blanco")

    def test_01_DadoUnPeonNuevoSeIniciaEn_x0_y0(self):
        self.assertEquals(self.peon.x, 0, "x incorrecto")
        self.assertEquals(self.peon.y, 0, "y incorrecto")

    def test_02_DadoUnPeonBlancoSuAtributoColorDebeSerBlanco(self):
        self.assertEquals(self.peon.color, "blanco", "el color debe ser blanco")
