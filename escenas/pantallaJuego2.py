import pilasengine

from actor.tablero import Tablero
from actor.cursor import Cursor
from actor.reloj import Reloj
from logica.ajedrez_basico import armarAjedrezBasico

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas, tts):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        # armamos tablero:
        self.reloj = Reloj(pilas)
        self.reloj.configurar(min=15, seg=30)

