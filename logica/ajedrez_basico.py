# -*- encoding: utf-8 -*-

class AjedrezTradicional():

    def __init__(self, pool):
        self.pool = pool

    def acomodar(self, tablero):
        # acomoda las fichas de un ajedrez tradicional:
        self.pool.definir_tablero(tablero)
        self.acomodarPiezas(tablero, fila=0, color="blanco")
        self.acomodarPeones(tablero, fila=1, color="blanco")
        self.acomodarPiezas(tablero, fila=7, color="negro")
        self.acomodarPeones(tablero, fila=6, color="negro")

    def acomodarPiezas(self, tablero, fila, color):
        tablero.posicionar(self.pool.generar("torre", color=color), 0, fila)
        tablero.posicionar(self.pool.generar("caballo", color=color), 1, fila)
        tablero.posicionar(self.pool.generar("alfil", color=color), 2, fila)
        tablero.posicionar(self.pool.generar("reina", color=color), 3, fila)
        tablero.posicionar(self.pool.generar("rey", color=color), 4, fila)
        tablero.posicionar(self.pool.generar("alfil", color=color), 5, fila)
        tablero.posicionar(self.pool.generar("caballo", color=color), 6, fila)
        tablero.posicionar(self.pool.generar("torre", color=color), 7, fila)

    def acomodarPeones(self, tablero, fila, color):
        for i in range(8):
            tablero.posicionar(self.pool.generar("peon", color=color), i, fila)
