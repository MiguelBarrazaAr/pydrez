# -*- encoding: utf-8 -*-
from .ajedrez_tradicional import ReglasAjedrezTradicional
from sonido import Sonido
import sunfish

class ReglasAjedrezTradicionalConIa(ReglasAjedrezTradicional):

    def __init__(self, *args, **kwargs):
        ReglasAjedrezTradicional.__init__(self, *args, **kwargs)
        self.posicion = sunfish.positionInitial()
        self.secs=2

    def posIniciar(self, *args, **kwargs):
        if self.partida.pilas.datos.colorPc == 'blanco':
            self.secs=1
            self.partida.pilas.tareas.agregar(2, self.jugarPc)

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

            # ajustamos el movimiento:
            desde = chr(97+self.celda_seleccionada.columna) + str(self.celda_seleccionada.fila+1)
            hasta = chr(97+columna) + str(fila+1)
            if self.secs == 1:
                mover = sunfish.parse(desde, 'b'), sunfish.parse(hasta, 'b')
            else:
                mover = sunfish.parse(desde), sunfish.parse(hasta)
            self.posicion = self.posicion.move(mover)

            # valida si se comio el rey para finalizar la partida:
            if celda.ficha is not None and celda.ficha.nombre == "rey":
                self.partida.finalizar(motivo="jacke mate", color=self.colorOpuesto(celda.ficha.color))

            self.partida.tablero.posicionar(ficha, columna=columna, fila=fila)
            self.celda_seleccionada.liberar()
            self._deseleccionarCelda()
            self.partida.finalizaMovimiento(celda)
            self.pasar_turno()
            self.partida.pilas.tareas.agregar(1, self.jugarPc)
        else:
            # no puede realizar el movimiento:
            self._deseleccionarCelda()
            self.movimiento_imposible()

    def jugarPc(self):
        """Juega la maquina"""
        mover, _ = sunfish.search(self.posicion, self.secs)
        self.posicion = self.posicion.move(mover)
        if self.secs == 1:
            desde = sunfish.render(mover[0])
            hasta = sunfish.render(mover[1])
        else:
            desde = sunfish.brender(mover[0])
            hasta = sunfish.brender(mover[1])

        self.realizarMovimiento(desde, hasta)
        self.pasar_turno()

    def realizarMovimiento(self, desde, hasta):
        c1 = ord(desde[0])-97
        f1 = int(desde[1])-1
        c2 = ord(hasta[0])-97
        f2 = int(hasta[1])-1
        celda_origen = self.partida.tablero.obtener_celda(c1, f1)
        ficha = celda_origen.ficha

        celda_destino = self.partida.tablero.obtener_celda(c2, f2)

        if celda_destino.ficha is not None and celda_destino.ficha.nombre == "rey":
            self.partida.finalizar(motivo="jacke mate",
                color=self.colorOpuesto(celda_destino.ficha.color))
        else:
            self.partida.registrar_movimiento(ficha=ficha,
                fichaEliminada = celda_destino.ficha,
                celdaOrigen = celda_origen,
                celdaDestino=celda_destino)
            self.partida.tablero.posicionar(ficha, columna=c2, fila=f2)
            celda_origen.liberar()
