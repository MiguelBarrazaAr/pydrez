import pilasengine

from actor.tablero import Tablero
from actor.cursor import Cursor
from logica.ajedrez_basico import AjedrezTradicional

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas, tts):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        # armamos tablero:
        self.tablero = Tablero(pilas, filas=8, columnas=8, centrado=True)
        self.tablero.acomodarFichas(AjedrezTradicional())
        self.cursorTeclado = Cursor(pilas, tablero=self.tablero, tts=tts)
        self.pilas.eventos.pulsa_tecla.conectar(self.interpreta_teclado)
        self.pilas.eventos.click_de_mouse.conectar(self.click_mouse)

    def click_mouse(self, evento):
        pass

    def interpreta_teclado(self, evento):
        if evento.codigo == "a":
            self.cursorTeclado.mover_izquierda()
        if evento.codigo == "d":
            self.cursorTeclado.mover_derecha()
        if evento.codigo == "s":
            self.cursorTeclado.mover_abajo()
        if evento.codigo == "w":
            self.cursorTeclado.mover_arriba()
