import pilasengine

class Celda(pilasengine.actores.Actor):

    def iniciar(self):
        self.blanco = "imagenes/celda/blanco.png"
        self.negro = "imagenes/celda/negro.png"
        self.verde = "imagenes/celda/verde.png"
        self.imagen = self.blanco

    def colorearVerde(self):
        self.imagen = self.blanco

    def colorearNegro(self):
        self.imagen = self.negro

    def colorearVerde(self):
        self.imagen = self.verde
