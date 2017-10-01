# -*- encoding: utf-8 -*-
from .organizador_de_fichas import OrganizadorDeFichas

class AcomodarFichas(OrganizadorDeFichas):

    def __init__(self, pool, posicionInicial):
        """la tuplasDeFicha tiene que tener los siguientes elementos:
        1. nombre de ficha: string
        2. bando: string
        3. columna: int
        4. fila, int."""
        self.pool = pool
        self.fichas = posicionInicial

    def organizar_fichas(self):
        """acomoda las fichas."""
        self.tablero.pilas.log("inicia el organizador...")
        for x in self.fichas:
            #print("posicionar", x)
            self.colocar(x[0], x[1], x[2], x[3])

        self.tablero.pilas.log("Finaliza el organizador... termina de acomodar el tablero.")
