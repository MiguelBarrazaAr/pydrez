from pilasengine.actores.actor import Actor
from actores.columnaDeHistorial import ColumnaDeHistorial


class Historial(Actor):


    def iniciar(self, ejex, ejey):
        self.imagen = "imagenes/papel.png"
        self.escala = 0.3
        self.x = 450
        self.columnaBlanca = ColumnaDeHistorial(self.pilas, ejex + 30, ejey)
        self.columnaNegra  = ColumnaDeHistorial(self.pilas, ejex + 90, ejey)
        self.columnaNumero = ColumnaDeHistorial(self.pilas, ejex, ejey)
        self.turnoBlanca = True
        self.numeroDeLinea = 1

    def agregar(self, mensaje):
        if self.turnoBlanca:
            self.columnaNumero.agregar(str(self.numeroDeLinea) + ".")
            self.columnaBlanca.agregar(mensaje)
            self.columnaNegra.agregar(' ')
            self.numeroDeLinea = self.numeroDeLinea + 1
            self.turnoBlanca = False
        else:
            self.columnaNegra.remplazar(mensaje)
            self.turnoBlanca = True

    def subir(self):
        if self.numeroDeLinea > 14:
            self.columnaBlanca.subir()
            self.columnaNegra.subir()
            self.columnaNumero.subir()

    def bajar(self):
        if self.numeroDeLinea > 14:
            self.columnaBlanca.bajar()
            self.columnaNegra.bajar()
            self.columnaNumero.bajar()
