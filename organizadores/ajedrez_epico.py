# -*- encoding: utf-8 -*-
from .organizador_de_fichas import OrganizadorDeFichas

class AjedrezEpico(OrganizadorDeFichas):

    def organizar_fichas(self):
        """acomoda las fichas de un ajedrez tradicional."""
        self.tablero.pilas.log("inicia el organizador... Acomoda el tablero como un ajedrez epico")
        self.acomodarPiezas(fila=0, color="blanco")
        self.acomodarDefensa(fila=1, color="blanco")
        self.acomodarPiezas(fila=self.tablero.filas-1, color="negro")
        self.acomodarDefensa(fila=self.tablero.filas-2, color="negro")
        self.tablero.pilas.log("Finaliza el organizador... termina de acomodar el tablero como un ajedrez epico")

    def acomodarPiezas(self, fila, color):
        self.colocar('golem', color, 0, fila)
        self.colocar('hipogrifo', color, 1, fila)
        self.colocar('licantropo', color, 2, fila)
        self.colocar('dragon', color, 3, fila)
        self.colocar('rey', color, 4, fila)
        self.colocar('licantropo', color, 5, fila)
        self.colocar('hipogrifo', color, 6, fila)
        self.colocar('golem', color, 7, fila)

    def acomodarDefensa(self, fila, color):
        for x in range(8):
            self.colocar('enano', color, x, fila)
