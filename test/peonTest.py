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
        self.peonBlanco = Peon(self.pilas, color="blanco", columna=4, fila=1)
        # iniciamos un peon negro en e7.
        self.peonNegro = Peon(self.pilas, color="negro", columna=4, fila=6)

    def test_01_DadoUnPeonNuevoSeIniciaEn_columna0(self):
        self.assertEquals(self.peon.columna, 0, "columna incorrecta")

    def test_02_DadoUnPeonNuevoSeIniciaEn_fila0(self):
        self.assertEquals(self.peon.fila, 0, "fila incorrecta")

    def test_03_DadoUnPeonNuevoSuAtributoColorIniciaSiendoBlanco(self):
        self.assertEquals(self.peon.color, "blanco", "el color debe ser blanco")

    def test_04_DadoUnPeonBlanco_validamosQueEsteIniciadoEnLaColumnaQueLeDefinimos_4(self):
        self.assertEquals(self.peonBlanco.columna, 4, "La columna tiene que ser 4")

    def test_05_DadoUnPeonBlanco_validamosQueEsteIniciadoEnLaFilaQueLeDefinimos_1(self):
        self.assertEquals(self.peonBlanco.fila, 1, "La fila tiene que ser 1")

    def test_06_DadoUnPeonBlanco_verificamosQueSuColorSeaBlanco(self):
        self.assertEquals(self.peonBlanco.color, "blanco", "El color tendria que ser blanco")

    def test_07_DadoUnPeonNegro_validamosQueEsteIniciadoEnLaFilaQueLeDefinimos_4(self):
        self.assertEquals(self.peonNegro.columna, 4, "La columna tiene que ser 4")

    def test_08_DadoUnPeonNegro_validamosQueEsteIniciadoEnLaFilaQueLeDefinimos_6(self):
        self.assertEquals(self.peonNegro.fila, 6, "La fila tiene que ser 6")

    def test_09_DadoUnPeonNegro_verificamosQueSuColorSeaNegro(self):
        self.assertEquals(self.peonNegro.color, "negro", "El color tendria que ser negro")

    def test_10_UnPeonBlancoEnE2_puedeMoverA_e3(self):
        self.assertTrue(self.peonBlanco.puedeMoverA(4, 2), "un peon de e2 puede moverse a e3")
