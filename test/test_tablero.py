# -*- encoding: utf-8 -*-
import unittest

from modelo.tablero import Tablero


class TestTablero(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.tablero4x4 = Tablero(filas=4, columnas=4)
        self.tablero = Tablero(filas=8, columnas=8)

    def test_DadoUnTableroDe8x8_debeTenerColumnaIgualA8(self):
        self.assertEquals(self.tablero.columnas, 8, "cantidad de columnas incorrecta")

    def test_DadoUnTableroDe8x8_debeTenerFilaIgualA8(self):
        self.assertEquals(self.tablero.filas, 8, "cantidad de filas incorrecta")

    def test_DadoUnTableroDe8x8_debeTenerSuListaEscaquesConLongitudIgualASusFilas(self):
        self.assertEquals(len(self.tablero.escaques), self.tablero.filas, "la lista escaque tiene que ser igual a sus filas.")

    def test_DadoUnTablero_debeTenerSuSublistasDeEscaquesConLongitudIgualASusColumnas(self):
        longitudCorrecta = True
        for fila in self.tablero.escaques:
            longitudCorrecta = longitudCorrecta and (len(fila)==self.tablero.columnas)
        self.assertTrue(longitudCorrecta, "la sublista escaque tiene que ser igual a sus columnas.")

    def test_DadoUnTablero_TodosSusEscaquesEstanVacios(self):
        escaqueVacio= reduce(lambda f, col: f and (
            reduce(lambda x, scaque: x and (scaque is None), col, True)
            ), self.tablero.escaques, True)
        self.assertTrue(escaqueVacio, "la sublista escaque tiene que ser igual a sus columnas.")
