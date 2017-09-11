# -*- encoding: utf-8 -*-
import unittest

import pilasengine

from actor.peon import Peon

class TestPeon(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.pilas = pilasengine.iniciar(modo_test=True)
        self.peon = Peon(self.pilas)
        # iniciamos un peon blanco en e2.
        self.peonBlanco = Peon(self.pilas, color="blanco", columna=5, fila=2)
        # iniciamos un peon negro en e7.
        self.peonNegro = Peon(self.pilas, color="negro", columna=5, fila=7)

    def test_01_DadoUnPeonNuevoSeIniciaEn_columna1(self):
        self.assertEquals(self.peon.columna, 1, "columna incorrecta")

    def test_02_DadoUnPeonNuevoSeIniciaEn_fila1(self):
        self.assertEquals(self.peon.fila, 1, "fila incorrecta")

    def test_03_DadoUnPeonNuevoSuAtributoColorIniciaSiendoBlanco(self):
        self.assertEquals(self.peon.color, "blanco", "el color debe ser blanco")

    def test_04_DadoUnPeonBlanco_validamosQueEsteIniciadoEnLaColumnaQueLeDefinimos_5(self):
        self.assertEquals(self.peonBlanco.columna, 5, "La columna tiene que ser 5")

    def test_05_DadoUnPeonBlanco_validamosQueEsteIniciadoEnLaFilaQueLeDefinimos_2(self):
        self.assertEquals(self.peonBlanco.fila, 2, "La fila tiene que ser 2")

    def test_06_DadoUnPeonBlanco_verificamosQueSuColorSeaBlanco(self):
        self.assertEquals(self.peonBlanco.color, "blanco", "El color tendria que ser blanco")

    def test_07_DadoUnPeonNegro_validamosQueEsteIniciadoEnLaFilaQueLeDefinimos_5(self):
        self.assertEquals(self.peonNegro.columna, 5, "La columna tiene que ser 5")

    def test_08_DadoUnPeonNegro_validamosQueEsteIniciadoEnLaFilaQueLeDefinimos_7(self):
        self.assertEquals(self.peonNegro.fila, 7, "La fila tiene que ser 7")

    def test_09_DadoUnPeonNegro_verificamosQueSuColorSeaNegro(self):
        self.assertEquals(self.peonNegro.color, "negro", "El color tendria que ser negro")

    def test_10_UnPeonBlancoEnE2_puedeMoverA_e3(self):
        self.assertTrue(self.peonBlanco.puedeMoverA(5, 3), "un peon de e2 puede moverse a e3")
