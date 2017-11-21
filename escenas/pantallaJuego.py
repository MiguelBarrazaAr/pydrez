import pilasengine

from actores.tablero import Tablero
from actores.cabezal import Cabezal
from actores.historial import Historial
from actores.textoAyuda import TextoAyuda

from partida import Partida
from reglas.ajedrez_tradicional import ReglasAjedrezTradicional
from tts import leer as tts
from sonido import Sonido

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas, datos=None):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        self.partida = Partida(pilas, datos)
        self.partida.definir_reglas(ReglasAjedrezTradicional())
        self.textoAyuda = TextoAyuda(self.pilas)

        # armamos tablero:
        self.tablero = Tablero(pilas, filas=8, columnas=8, centrado=False, tts=tts)
        self.partida.definir_tablero(self.tablero)
        self.partida.iniciar()

        self.cabezal = Cabezal(pilas, tablero=self.tablero, tts=tts)
        # conexiones con eventos:
        self.pilas.eventos.pulsa_tecla.conectar(self.interpreta_teclado)
        self.pilas.eventos.click_de_mouse.conectar(self.click_mouse)
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.activar_menu_principal)
        # eventos de juego:
        self.partida.eventoPreMueveFicha.conectar(self.mueveFicha)

        self.pilas.camara.x = 270
        self.pilas.camara.y= 160

        # sonidos:
        self.sonido_mover = Sonido('audio/mover-ficha.ogg')
        self.historial = Historial(pilas, 130, 140)

    def activar_menu_principal(self, evento):
        datos=None
        if self.partida.activa:
            datos=self.partida.datos
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas, datos=datos)

    def mueveFicha(self, evento):
        self.sonido_mover.reproducir()
        self.decir(str(evento.ficha)+" mueve a: "+str(evento.celdaDestino))
        if evento.fichaEliminada:
            #print("fuera de juego", fichaEliminada.nombre,  fichaEliminada.color)
            self.historial.agregar(repr(evento.ficha) + "x" + str(evento.celdaDestino))
        else:
            self.historial.agregar(repr(evento.ficha) + str(evento.celdaDestino))


    def click_mouse(self, evento):
        x = int(evento.x) + (self.tablero.distancia / 2) + self.pilas.camara.x
        y = int(evento.y) + (self.tablero.distancia / 2) + self.pilas.camara.y
        columna = x / self.tablero.distancia
        fila = y / self.tablero.distancia
        if(evento.boton == 1):
            self.cabezal.mover(columna=columna, fila=fila)
            #elf.cabezal.seleccionar()
            self.partida.seleccionar_celda(columna=self.cabezal.columna, fila=self.cabezal.fila)
        if(evento.boton == 2):
            ficha = self.tablero.obtenerFicha(columna=columna,fila=fila)
            if ficha is not None:
                self.textoAyuda.infoDePieza(ficha.nombre,x,y)




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
        if evento.codigo == "m":
            self.historial.subir()
        if evento.codigo == "n":
            self.historial.bajar()

