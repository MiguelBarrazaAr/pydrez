# -*- encoding: utf-8 -*-
from organizadores.ajedrez_basico import OrganizadorAjedrezTradicional
from organizadores.acomodar_fichas import AcomodarFichas

class Reglas(object):

    def __init__(self, personalizado=False):
        self.bandos = ['blanco', 'negro']
        self.turno = 0
        self.partida = None
        self.celda_seleccionada = None
        self.dimensionTablero = (8, 8)
        self.personalizado = personalizado
        self.organizador = self.obtener_organizador()
        self.efectoTablero = None

    def iniciar(self, *args, **kwargs):
        """configura el inicio de una partida"""
        self.acomodarTablero()
        self.partida.tablero.acomodarFichas(self.organizador(pool=self.partida.pool, *args, **kwargs))
        self.partida.activa = True
        self.partida.turno = self.bandos[self.turno]
        self.posIniciar(*args, **kwargs)

    def reiniciar(self, *args, **kwargs):
        """Continua con la partida ya iniciada."""
        self.acomodarTablero()
        self.posIniciar(*args, **kwargs)

    def acomodarTablero(self):
        self.partida.tablero.eliminarCeldas()
        self.partida.tablero.columnas = self.dimensionTablero[0]
        self.partida.tablero.filas = self.dimensionTablero[1]
        self.partida.tablero.graficar(self.efectoTablero)

    def PosIniciar(self, *args, **kwargs):
        """metodo que se ejecuta despues de iniciar la partida.
        se debe sobreescribir si es necesario"""
        return None

    def definir_partida(self, partida):
        self.partida = partida

    def pasar_turno(self):
        self.turno = (self.turno+1)%2
        self.partida.turno = self.bandos[self.turno]
        if self.turno == 0:
            self.partida.cantTurnos+=1

    def turno_actual(self):
        return self.bandos[self.turno]

    def obtener_organizador(self):
        """retorna el organizador de fichas en el tablero"""
        if self.personalizado:
            return AcomodarFichas
        else:
            return OrganizadorAjedrezTradicional

    def decir(self, texto, interrumpir=True):
        self.partida.decir(texto, interrumpir)

    def log(self, *args, **kwargs):
        self.partida.pilas.log(*args, **kwargs)

    def definirTablero(self, clave):
        import tableros
        efecto = tableros.generar(clave)()
        self.dimensionTablero = efecto.dimensionTablero
        self.efectoTablero = efecto

    def seleccionar_celda(self, columna, fila):
        """Selecciona una celda.
        solo se puede seleccionar celdas que tienen fichas.
        si ya hay una seleccionada realiza un movimiento.
        nota: este metodo se debe sobreescribir si la regla define otro comportamiento al dar enter.
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
        pass