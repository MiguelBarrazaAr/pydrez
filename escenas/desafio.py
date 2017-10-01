import pilasengine

from actores.tablero import Tablero
from actores.cabezal import Cabezal
from partida import Partida
from reglas.ajedrez_tradicional import ReglasAjedrezTradicional

class Desafio(pilasengine.escenas.Escena):

    def iniciar(self, pilas, tts):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        self.partida = Partida(pilas, tts)
        self.partida.definir_reglas(ReglasAjedrezTradicional(personalizado=True))
        # armamos tablero:
        self.tablero = Tablero(pilas, filas=8, columnas=8, centrado=True, tts=tts)
        self.partida.definir_tablero(self.tablero)

        # definimos la posicion inicial:
        fichas = [('rey', 'negro', 7, 7),
            ('peon', 'negro', 6, 6),
            ('torre', 'negro', 7, 6),
            ('torre', 'negro', 6, 7),
            ('dama', 'blanco', 4, 4),
            ('torre', 'blanco', 7, 0),
            ('torre', 'blanco', 0, 7)]
        self.partida.iniciar(posicionInicial=fichas)

        self.cabezal = Cabezal(pilas, tablero=self.tablero, tts=tts)
        # conexiones con eventos:
        self.pilas.eventos.pulsa_tecla.conectar(self.interpreta_teclado)
        self.pilas.eventos.click_de_mouse.conectar(self.click_mouse)
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.activar_menu_principal)

    def activar_menu_principal(self, evento):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas, tts=self.decir)

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
            self.partida.seleccionar_celda(columna=self.cabezal.columna, fila=self.cabezal.fila)
