# -*- encoding: utf-8 -*-
from .reglas import Reglas
from sonido import Sonido

class PuzzleAjedrez(Reglas):

    def __init__(self, *args, **kwargs):
        Reglas.__init__(self, *args, **kwargs)
        self.personalizado=True
        self.sonido_revote = Sonido("audio/boing.ogg")

    def seleccionar_celda(self, columna, fila):
        """Selecciona una celda.
        solo se puede seleccionar celdas que tienen fichas.
        si ya hay una seleccionada realiza un movimiento
        """

        if self.celda_seleccionada is None:
            # si no hay ninguna celda seleccionada:
            celda = self.partida.tablero.obtener_celda(columna, fila)
            if celda.tiene_ficha():
                # seleccionamos la celda:
                self.celda_seleccionada = celda
                self.celda_seleccionada.seleccionar()
                self.decir(str(self.celda_seleccionada.ficha)+" seleccionado")

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
        if ficha.puede_mover(celda):
            # puede realizar el movimiento:
            self.partida.registrar_movimiento(ficha=self.celda_seleccionada.ficha,
                fichaEliminada=celda.ficha, celda_origen=self.celda_seleccionada, celda_destino=celda)
            self.celda_seleccionada.liberar()
            # valida si queda una ficha o no tiene posibilidad de comer. para finalizar el puzzgle.
            #self.partida.finalizar()

            self.partida.tablero.posicionar(ficha, columna=columna, fila=fila)
            self._deseleccionarCelda()
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
