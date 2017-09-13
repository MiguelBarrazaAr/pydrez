# -*- encoding: utf-8 -*-
import unittest

import pilasengine

from actor.tablero import Tablero


class TestTablero(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.pilas = pilasengine.iniciar(modo_test=True)
        self.tablero = Tablero(self.pilas, filas=4, columnas=4)
        self.tableroCentrado = Tablero(self.pilas, filas=8, columnas=8, centrado=True)

    def test_DadoUnTableroDe4x4_debeTenerColumnaIgualA4(self):
        self.assertEquals(self.tablero.columnas, 4, "columna incorrecta")

    def test_DadoUnTableroDe4x4_debeTenerFilaIgualA4(self):
        self.assertEquals(self.tablero.filas, 4, "fila incorrecta")

    def test_DadoUnTableroNocentrado_xDebeIniciarseEn0(self):
        self.assertEquals(self.tablero.x, 0, "x debe ser 0")

    def test_DadoUnTableroNocentrado_yDebeIniciarseEn0(self):
        self.assertEquals(self.tablero.y, 0, "y debe ser 0")

    def test_DadoUnTableroDe8x8_Centrado_debeTenerColumnaIgualA8(self):
        self.assertEquals(self.tableroCentrado.columnas, 8, "columna incorrecta")

    def test_DadoUnTableroDe8x8_centrado_debeTenerFilaIgualA8(self):
        self.assertEquals(self.tableroCentrado.filas, 8, "fila incorrecta")

    def test_DadoUnTableroCentrado_susCoordenadas_x_y_DebenIniciarseCorrectamente(self):
        # si la camara esta en x=0 y y=0
        # si  un tablero de 8 x 8, debe estar 4 casillas del centro.
        # cada casilla es de largo = 30 px.

        # verificamos posicion de la camara:
        self.assertEquals(self.pilas.camara.x, 0, "camara.x debe ser 0")
        self.assertEquals(self.pilas.camara.y, 0, "camara.y debe ser 0")

        # validamos posicion del tablero:
        self.assertEquals(self.tableroCentrado.x, -120, "x debe ser -120")
        self.assertEquals(self.tableroCentrado.y, -120, "y debe ser -120")
