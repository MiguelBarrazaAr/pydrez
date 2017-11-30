# -*- encoding: utf-8 -*-
from .reglas import Reglas
from sonido import Sonido
from random import randint

class ReglasAjedrezMinado(Reglas):

    def __init__(self, *args, **kwargs):
        Reglas.__init__(self, *args, **kwargs)
        self.sonido_revote = Sonido("audio/boing.ogg")
        self.sonido_boom = Sonido("audio/boom.wav")
        self.sonido_boom.volumen = 0.6

    def posIniciar(self):
        self.colocarMinaZonaBlanca()
        self.colocarMinaZonaNegra()

    def seleccionar_celda(self, columna, fila):
        """Selecciona una celda.
        solo se puede seleccionar celdas que tienen fichas.
        si ya hay una seleccionada realiza un movimiento
        """

        if self.celda_seleccionada is None:
            # si no hay ninguna celda seleccionada:
            celda = self.partida.tablero.obtener_celda(columna, fila)
            if celda.tiene_ficha():
                turno_actual = self.turno_actual()
                if celda.ficha.color == turno_actual:
                    # seleccionamos la celda:
                    self.celda_seleccionada = celda
                    self.celda_seleccionada.seleccionar()
                    self.decir(str(self.celda_seleccionada.ficha)+" seleccionado")
                else:
                    self.decir("es turno del "+turno_actual)

        else:
            # si ya hay celda seleccionada:
            if self.celda_seleccionada.columna == columna and  self.celda_seleccionada.fila == fila:
                # si selecciona 2 veces la misma celda la deselecciona.
                self.decir(str(self.celda_seleccionada.ficha)+" deseleccionado")
                self._deseleccionarCelda()
            else:
                # si selecciona otra celda realiza el movimiento:
                self.mover_ficha(columna, fila)

    def mover_ficha(self, columna, fila):
        ficha = self.celda_seleccionada.ficha
        celda = self.partida.tablero.obtener_celda(columna, fila)
        # verificamos si la celda tiene ficha:
        if celda.tiene_ficha():
            # si tiene ficha verificamos que no sea del mismo color:
            celdaVerificada = ficha.color != celda.ficha.color
        else:
            celdaVerificada = True

        if ficha.puede_mover(celda) and celdaVerificada:
            # puede realizar el movimiento:

            self.partida.registrar_movimiento(ficha=self.celda_seleccionada.ficha,
                fichaEliminada=celda.ficha, celdaOrigen=self.celda_seleccionada, celdaDestino=celda)
            self.celda_seleccionada.liberar()
            # valida si se comio el rey para finalizar la partida:
            if celda.ficha is not None and celda.ficha.nombre == "rey":
                self.partida.finalizar("jacke mate")

            self.partida.tablero.posicionar(ficha, columna=columna, fila=fila)
            if(celda.fila == self.minaZonaBlanca[0] and celda.columna == self.minaZonaBlanca [1]):
                self.explotar(celda)
                self.colocarMinaZonaBlanca()
            if (celda.fila == self.minaZonaNegra[0] and celda.columna == self.minaZonaNegra[1]):
                self.explotar(celda)
                self.colocarMinaZonaNegra()
            self.pasar_turno()
            self._deseleccionarCelda()
            self.partida.finalizaMovimiento(celda)
        else:
            # no puede realizar el movimiento:
            self._deseleccionarCelda()
            self.movimiento_imposible()

    def _deseleccionarCelda(self):
        """deselecciona una celda seleccionada:
        precondici�n: debe haber una celda seleccionada.
        la propiedad: celda_seleccionada no debe ser None"""
        self.celda_seleccionada.deseleccionar()
        self.celda_seleccionada = None

    def movimiento_imposible(self):
        """metodo que se ejecuta cuando un jugador realiza un movimiento imposible"""
        self.sonido_revote.reproducir()
        self.decir("movimiento imposible")

    def colocarMinaZonaBlanca(self):

        bomba = (randint(0, (self.partida.tablero.columnas / 2) - 1), randint(0, self.partida.tablero.filas - 1))

        while (self.partida.tablero.obtener_celda(bomba[1],bomba[0]).ficha is not None):
            bomba = (randint(0, (self.partida.tablero.columnas / 2) - 1), randint(0, self.partida.tablero.filas - 1))
        print bomba
        self.minaZonaBlanca = bomba

    def colocarMinaZonaNegra(self):

        bomba = (randint((self.partida.tablero.columnas / 2 ) + 1 , self.partida.tablero.columnas - 1),randint(0, self.partida.tablero.filas - 1))
        while (self.partida.tablero.obtener_celda(bomba[1],bomba[0]).ficha is not None):
            bomba = (randint((self.partida.tablero.columnas / 2 ) + 1 , self.partida.tablero.columnas - 1),randint(0, self.partida.tablero.filas - 1))
        print bomba
        self.minaZonaNegra = bomba

    def explotar(self,celda):
        if celda.ficha.nombre == 'rey':
            self.partida.finalizar("jacke mate")
        self.sonido_boom.reproducir()
        self.grilla = self.partida.pilas.imagenes.cargar_grilla("imagenes/animaciones/ExplosionGrande.png", 12)
        p = self.partida.pilas.actores.Animacion(self.grilla, False, x=celda.x, y=celda.y, velocidad=15)
        celdas = self.partida.tablero.obteneer_celdas_lindantes(celda.fila, celda.columna)
        for x in celdas:
            if x.ficha is not None and x.ficha.nombre != 'peon':
                if x.ficha.nombre == 'rey':
                    self.partida.finalizar("jacke mate")
                self.partida.tablero.elimiraPieza(x)
        self.partida.tablero.elimiraPieza(celda)