import pilasengine

from actores.tablero import Tablero
from actores.cabezal import Cabezal
from fichas.pool import PoolDeFichas
from organizadores.ajedrez_basico import AjedrezTradicional

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas, tts):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        self.pool = PoolDeFichas(pilas)
        # armamos tablero:
        self.tablero = Tablero(pilas, filas=8, columnas=8, centrado=True, tts=tts)
        self.pool.definir_tablero(self.tablero)
        self.tablero.acomodarFichas(AjedrezTradicional(self.pool))
        self.cabezal = Cabezal(pilas, tablero=self.tablero, tts=tts)
        self.pilas.eventos.pulsa_tecla.conectar(self.interpreta_teclado)
        self.pilas.eventos.click_de_mouse.conectar(self.click_mouse)

    def click_mouse(self, evento):
        if(evento.boton == 1):
            x = int(evento.x)-(self.tablero.x-self.tablero.distancia/2)
            y = int(evento.y)-(self.tablero.y-self.tablero.distancia/2)
            columna = x/self.tablero.distancia
            fila = y/self.tablero.distancia
            self.cabezal.mover(columna=columna, fila=fila)
            self.cabezal.seleccionar()

    def interpreta_teclado(self, evento):
        if evento.codigo == "a" or evento.codigo == self.pilas.simbolos.IZQUIERDA:
            self.cabezal.mover_izquierda()
        if evento.codigo == "d" or evento.codigo == self.pilas.simbolos.DERECHA:
            self.cabezal.mover_derecha()
        if evento.codigo == "s" or evento.codigo == self.pilas.simbolos.ABAJO:
            self.cabezal.mover_abajo()
        if evento.codigo == "w" or evento.codigo == self.pilas.simbolos.ARRIBA:
            self.cabezal.mover_arriba()
        if evento.codigo == self.pilas.simbolos.SELECCION:
            self.cabezal.seleccionar()
