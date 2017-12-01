# -*- encoding: utf-8 -*-
from .organizador_de_fichas import OrganizadorDeFichas

class AjedrezSalvaje(OrganizadorDeFichas):

    def organizar_fichas(self):
        """acomoda las fichas de un ajedrez tradicional."""
        self.tablero.pilas.log("inicia el organizador... Acomoda el tablero como un ajedrez salvaje")
        self.acomodarPiezas(fila=0, color="blanco")
        self.acomodarDefensa(fila=1, color="blanco")
        self.acomodarPiezas(fila=self.tablero.filas-1, color="negro")
        self.acomodarDefensa(fila=self.tablero.filas-2, color="negro")
        self.tablero.pilas.log("Finaliza el organizador... termina de acomodar el tablero como un ajedrez salvaje")

    def acomodarPiezas(self, fila, color):
        self.colocar('conejo', color, 0, fila)
        self.colocar('lobo', color, 1, fila)
        self.colocar('elefante', color, 2, fila)
        self.colocar('serpiente', color, 3, fila)
        self.colocar('leon', color, 4, fila)
        self.colocar('elefante', color, 5, fila)
        self.colocar('lobo', color, 6, fila)
        self.colocar('conejo', color, 7, fila)

    def acomodarDefensa(self, fila, color):
        for x in range(8):
            self.colocar('raton', color, x, fila)
