import pilasengine

from actor.tablero import Tablero
from actor.cursor import Cursor
from logica.ajedrez_basico import armarAjedrezBasico

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas, tts):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        # armamos tablero:
        self.tablero = Tablero(pilas, filas=8, columnas=8, x=-120, y=-120)
        armarAjedrezBasico(pilas, self.tablero)
        self.cursorTeclado = Cursor(pilas, tablero=self.tablero, tts=tts)
