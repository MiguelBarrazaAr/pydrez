# -*- encoding: utf-8 -*-
import unittest

import pilasengine

from actor.tablero import Tablero
from actor.peon import Peon
import celda

class TestPeon(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.pilas = pilasengine.iniciar(modo_test=True)
        self.peon = Peon(self.pilas)
        # iniciamos un peon blanco en e2.
        self.peonBlanco = Peon(self.pilas, color="blanco", celda=celda.generar(columna=5, fila=2))
        # iniciamos un peon negro en e7.
        self.peonNegro = Peon(self.pilas, color="negro", celda=celda.generar(columna=5, fila=7))

    def test_DadoUnPeonNuevoSeIniciaSinCeldaAsignada(self):
        self.assertIsNone(self.peon._celda, "la celda debe iniciarse a None")

    def test_DadoUnPeonNuevoSuAtributoColorIniciaSiendoBlanco(self):
        self.assertEquals(self.peon.color, "blanco", "el color debe ser blanco")

    def test_DadoUnPeonNuevo_IniciaSinNingunTableroAsignado(self):
        self.assertIsNone(self.peon.tablero, "el atributo tablero debe iniciarse a None")

    def test_DadoUnPeonBlanco_validamosQueEsteIniciadoEnLaColumnaQueLeDefinimos_5(self):
        self.assertEquals(self.peonBlanco._celda.columna, 4, "La columna tiene que ser 4")

    def test_DadoUnPeonBlanco_validamosQueEsteIniciadoEnLaFilaQueLeDefinimos_2(self):
        self.assertEquals(self.peonBlanco._celda.fila, 1, "La fila tiene que ser 1")

    def test_DadoUnPeonBlanco_verificamosQueSuColorSeaBlanco(self):
        self.assertEquals(self.peonBlanco.color, "blanco", "El color tendria que ser blanco")

    def test_DadoUnPeonNegro_validamosQueEsteIniciadoEnLaFilaQueLeDefinimos_5(self):
        self.assertEquals(self.peonNegro._celda.columna, 4, "La columna tiene que ser 4")

    def test_DadoUnPeonNegro_validamosQueEsteIniciadoEnLaFilaQueLeDefinimos_7(self):
        self.assertEquals(self.peonNegro._celda.fila, 6, "La fila tiene que ser 6")

    def test_DadoUnPeonNegro_verificamosQueSuColorSeaNegro(self):
        self.assertEquals(self.peonNegro.color, "negro", "El color tendria que ser negro")

    def test_UnPeonBlancoEnE2_puedeMoverA_e3(self):
        self.assertTrue(self.peonBlanco.puedeMoverA(4, 2), "un peon de e2 puede moverse a e3")

    def test_UnPeonBlancoEnE2_puedeMoverA_e4(self):
        self.assertTrue(self.peonBlanco.puedeMoverA(4, 3), "un peon de e2 puede moverse a e4")

    def test_UnPeonBlancoEnE2_noPuedeMoverA_e5(self):
        self.assertFalse(self.peonBlanco.puedeMoverA(4, 4), "un peon de e2 no puede moverse a e5")

    def test_UnPeonBlancoEnE2_noPuedeMoverA_d2(self):
        self.assertFalse(self.peonBlanco.puedeMoverA(3, 1), "un peon de e2 no puede moverse a d2")

    def test_UnPeonBlancoEnE2_noPuedeMoverA_f2(self):
        self.assertFalse(self.peonBlanco.puedeMoverA(5, 1), "un peon de e2 no puede moverse a f2")

    def test_UnPeonBlancoEnE2_noPuedeMoverA_d3(self):
        self.assertFalse(self.peonBlanco.puedeMoverA(3, 2), "un peon de e2 no puede moverse a d3")

    def test_UnPeonBlancoEnE2_noPuedeMoverA_f3(self):
        self.assertFalse(self.peonBlanco.puedeMoverA(5, 2), "un peon de e2 no puede moverse a f3")

    def test_UnPeonBlancoEnE2_noPuedeMoverA_d4(self):
        self.assertFalse(self.peonBlanco.puedeMoverA(3, 3), "un peon de e2 no puede moverse a d4")

    def test_UnPeonBlancoEnE2_noPuedeMoverA_f4(self):
        self.assertFalse(self.peonBlanco.puedeMoverA(6, 4), "un peon de e2 no puede moverse a f4")

    def test_UnPeonNegroEnE7_puedeMoverA_e6(self):
        self.assertTrue(self.peonNegro.puedeMoverA(4, 5), "un peon de e7 puede moverse a e6")

    def test_UnPeonNegroEnE7_puedeMoverA_e5(self):
        self.assertTrue(self.peonNegro.puedeMoverA(4, 4), "un peon de e7 puede moverse a e5")

    def test_UnPeonNegroEnE7_noPuedeMoverA_e4(self):
        self.assertFalse(self.peonNegro.puedeMoverA(4, 3), "un peon de e7 no puede moverse a e4")

