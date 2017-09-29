# -*- encoding: utf-8 -*-
from .reglas import Reglas

class ReglasAjedrezTradicional(Reglas):

    def seleccionar_celda(self, columna, fila):
        """Selecciona una celda.
        solo se puede seleccionar celdas que tienen fichas.
        si ya hay una seleccionada realiza un movimiento
        """
        celda = self.partida.tablero.obtener_celda(columna, fila)
        if self.celda_seleccionada is None:
            # si no hay ninguna celda seleccionada:
            if celda.tieneFicha():
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
                if self.celda_seleccionada.ficha.moverA(celda):
                    # pudo realizar el movimiento:
                    self.partida.registrar_movimiento(ficha=self.celda_seleccionada.ficha,
                        celda_origen=self.celda_seleccionada, celda_destino=celda)
                    self._deseleccionarCelda()
                else:
                    # no puede realizar el movimiento:
                    self._deseleccionarCelda()
                    self.movimiento_imposible()

    def _deseleccionarCelda(self):
        """deselecciona una celda seleccionada:
        precondición: debe haber una celda seleccionada.
        la propiedad: celda_seleccionada no debe ser None"""
        self.celda_seleccionada.deseleccionar()
        self.celda_seleccionada = None

    def movimiento_imposible(self):
        """metodo que se ejecuta cuando un jugador realiza un movimiento imposible"""
        self.decir("movimiento imposible")
