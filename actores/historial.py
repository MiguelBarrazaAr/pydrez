from pilasengine.actores.actor import Actor
from actores.columnaDeHistorial import ColumnaDeHistorial


class Historial(Actor):


    def iniciar(self, ejex, ejey, cantidadDeJugadores = 2):
        self.imagen = "invisible.png"
        self.cantidadDeJugadores = cantidadDeJugadores
        self.escala = 0.5
        self.x = ejex
        self.y = ejey
        self.jugadores = []
        for x in range(cantidadDeJugadores):
            self.jugadores.append(ColumnaDeHistorial(self.pilas, self.x + x * 75, ejey + 185))


        print self.jugadores


        #self.columnaBlanca = ColumnaDeHistorial(self.pilas, self.x + -70, ejey + 185)
        #self.columnaNegra  = ColumnaDeHistorial(self.pilas, self.x + 40, ejey + 185)
        self.columnaNumero = ColumnaDeHistorial(self.pilas, self.x + - 30, ejey + 185)
        self.indice = 0
        self.numeroDeLinea = 1

    def agregar(self, mensaje):
        if self.indice == 0:
            self.columnaNumero.agregar(str(self.numeroDeLinea) + ".")
            self.numeroDeLinea = self.numeroDeLinea + 1
            for x in self.jugadores:
                x.agregar(" ")
            (self.jugadores[0]).remplazar(mensaje)
            if self.cantidadDeJugadores == 1:
                self.indice += 0
            else:
                self.indice += 1
        else:
            (self.jugadores[self.indice]).remplazar(mensaje)
            if self.indice + 1 == self.cantidadDeJugadores:
                self.indice = 0
            else:
                self.indice += 1


    def subir(self):
        if self.numeroDeLinea > 14:
            for x in self.jugadores:
                x.subir()

    def bajar(self):
        if self.numeroDeLinea > 14:
            for x in self.jugadores:
                x.bajar()
