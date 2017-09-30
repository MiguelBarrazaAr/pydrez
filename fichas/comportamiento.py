# -*- encoding: utf-8 -*-

class Comportamiento(object):

    def __init__(self, bando):
        self.nombre = self.__class__.__name__.lower()
        self.escala = 0.7
        self.saltadora = False
        self.bando = bando
        self.ficha = None

    def activar(self, ficha):
        self.ficha = ficha
        ficha.imagen = self.ruta_de_imagen()
        ficha.nombre = self.nombre
        ficha.color = self.bando
        if self.escala:
            ficha.escala = self.escala

    def desactivar(self):
        self.ficha.imagen = 'invisible.png'
        self.ficha.nombre = 'desconocido'
        self.ficha.color = ''
        self.ficha = None

    def ruta_de_imagen(self):
        return "imagenes/fichas/"+self.bando+"/"+self.nombre+".png"

    @property
    def columna(self):
        return self.ficha._celda.columna

    @property
    def fila(self):
        return self.ficha._celda.fila

    def puedeMoverA(self, columna, fila):
        """Verifica si la pieza puede llegar a la columna y fila indicada.
        este metodo se debe sobreescribir."""
        return False

    def puedeComerEn(self, celda):
        """retorna true si esta ficha puede comer en esa celda_destino.
        una ficha no puede comer a otra del mismo bando.
        este metodo se debe sobreescribir si es necesario."""
        if celda.ficha.color == self.bando:
            return False
        else:
            return self.puedeMoverA(columna=celda.columna, fila=celda.fila)

    def verificar_celdas(self, celda):
        """retorna una lista de tupla (columna, fila) de las celdas que se debe verificar para llegar a celda_destino.
        este metodo se debe sobreescribir si no es saltadora."""
        return []
