import pilasengine

from actores.tablero import Tablero
from actores.cabezal import Cabezal
from actores.historial import Historial
from actores.textoAyuda import TextoAyuda


from partida import Partida
from tts import leer as tts
from sonido import Sonido

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas, datos=None):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/fondoJuego.jpg")
        self.decir = tts
        self.datos   = datos
        self.partida = Partida(pilas, self.datos)
        self.partida.definir_reglas(pilas.datos.modoJuego)
        self.textoAyuda = TextoAyuda(self.pilas)


        # armamos tablero:
        self.tablero = Tablero(pilas, x=- 400 ,y=-250)
        self.partida.definir_tablero(self.tablero)
        self.partida.iniciar()

        self.cabezal = Cabezal(pilas, tablero=self.tablero, tts=tts)
        # conexiones con eventos:
        self.pilas.eventos.pulsa_tecla.conectar(self.interpreta_teclado)
        self.pilas.eventos.click_de_mouse.conectar(self.click_mouse)
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.activar_menu_principal)
        # eventos de juego:
        self.partida.eventoPreMueveFicha.conectar(self.mueveFicha)
        self.partida.eventoFinalizar.conectar(self.mostrarResultado)

        # sonidos:
        self.sonido_mover = Sonido('audio/mover-ficha.ogg')
        self.historial = Historial(pilas, ejex=300, ejey=0)
        self.historial.fijo = True

        #
        self.botonReiniciar = pilas.interfaz.Boton("Nueva Partida")
        self.botonReiniciar.x =  400
        self.botonReiniciar.y = -300
        self.botonReiniciar.conectar(self.nuevaPartida)

    def activar_menu_principal(self, evento):
        datos=None
        if self.partida.activa:
            datos=self.partida.datos
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas, datos=datos)

    def mueveFicha(self, evento):
        self.sonido_mover.reproducir()
        self.decir(str(evento.ficha)+" mueve a: "+repr(evento.celdaDestino))
        if evento.fichaEliminada:
            #print("fuera de juego", fichaEliminada.nombre,  fichaEliminada.color)
            self.historial.agregar(repr(evento.ficha) + "x" + repr(evento.celdaDestino))
        else:
            self.historial.agregar(repr(evento.ficha) + repr(evento.celdaDestino))


    def click_mouse(self, evento):
        x = (int(evento.x) + (self.tablero.distancia / 2) + int(self.pilas.camara.x)) - self.tablero.x
        y = (int(evento.y) + (self.tablero.distancia / 2) + int(self.pilas.camara.y)) - self.tablero.y
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
            if self.tablero.columnas > 8 and abs(self.cabezal.x - self.camara.x) > 400 and self.cabezal.x - self.camara.x < 399:
                self.pilas.camara.x = [self.cabezal.x + 400]
        if evento.codigo == "d" or evento.codigo == self.pilas.simbolos.DERECHA:
            self.cabezal.mover_derecha()
            if self.tablero.columnas > 8 and self.cabezal.x - self.camara.x > -400 and self.cabezal.x - self.camara.x > 399 :
                self.pilas.camara.x = [self.cabezal.x - 400]
        if evento.codigo == "s" or evento.codigo == self.pilas.simbolos.ABAJO:
            self.cabezal.mover_abajo()
            if self.tablero.filas > 8 and abs(self.cabezal.y - self.camara.y) > 200:
                self.pilas.camara.y = [self.cabezal.y + 200]
        if evento.codigo == "w" or evento.codigo == self.pilas.simbolos.ARRIBA:
            self.cabezal.mover_arriba()
            if self.tablero.filas > 8 and abs(self.cabezal.y - self.camara.y) > 200:
                self.pilas.camara.y = [self.cabezal.y - 200]
        if evento.codigo == self.pilas.simbolos.SELECCION:
            self.partida.seleccionar_celda(columna=self.cabezal.columna, fila=self.cabezal.fila)
        if evento.codigo == "g":
            self.historial.subir()
        if evento.codigo == "h":
            self.historial.bajar()
        if evento.codigo == "n":
            self.nuevaPartida()
        if evento.codigo == "F1":
            ficha = self.tablero.obtenerFicha(columna=self.cabezal.columna, fila=self.cabezal.fila)
            if ficha is not None:
                info = self.textoAyuda.infoDePieza(ficha.nombre ,
                    self.cabezal.x +30,self.cabezal.y)
                self.decir(info)

    def nuevaPartida(self):
        self.pilas.escenas.PantallaJuego(pilas=self.pilas, datos=self.datos)

    def mostrarResultado(self,evento):
        texto = self.pilas.actores.Texto("Ganan las ", y=300,ancho=300)
        texto.color = self.pilas.colores.Color(77, 38, 22)
        if evento.color == "blanco":
            texto.texto = texto.texto + "blancas"
        else:
            texto.texto = texto.texto + "negras"

