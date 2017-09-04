import pilasengine

from actor.tablero import Tablero
from actor.cursor import Cursor
from logica.ajedrez_basico import armarAjedrezBasico

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas):
        self.fondo = pilas.fondos.Plano()

        # armamos tablero:
        self.tablero = Tablero(pilas, filas=13, columnas=8, x=-240, y=-126)
        #armarAjedrezBasico(pilas, self.tablero)
        #self.cursorTeclado = Cursor(pilas, tablero=self.tablero)
