# -*- encoding: utf-8 -*-

class OrganizadorDeFichas(object):

    def __init__(self, pool, *args, **kwargs):
        self.pool = pool

    def colocar(self, tipoDeFicha, color, columna, fila):
        self.tablero.posicionar(self.pool.generar(tipoDeFicha, color), columna, fila)
        self.tablero.pilas.log("Se posiciona ", tipoDeFicha, " ", color, " en (", columna, ", ", fila, ")")

    def acomodar(self, tablero):
        """acomoda las fichas"""
        self.pool.definir_tablero(tablero)
        self.tablero = tablero
        self.organizar_fichas()

    def organizar_fichas(self):
        """este metodo se debe sobreescribir"""
        pass
