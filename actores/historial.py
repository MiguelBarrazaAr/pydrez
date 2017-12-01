from pilasengine.actores.actor import Actor
from actores.columnaDeHistorial import ColumnaDeHistorial


class Historial(Actor):


    def iniciar(self, ejex, ejey):
        self.imagen = "invisible.png"
        self.escala = 0.5
        self.x = ejex
        self.y = ejey
        self.columnaBlanca = ColumnaDeHistorial(self.pilas, self.x + -70, ejey + 185)
        self.columnaNegra  = ColumnaDeHistorial(self.pilas, self.x + 40, ejey + 185)
        self.columnaNumero = ColumnaDeHistorial(self.pilas, self.x + -120, ejey + 185)
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
