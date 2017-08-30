from pilasengine.actores.actor import Actor

class Caballo(Actor):

    def iniciar(self, color="blanco"):
        self.imagen = "imagenes/pieza/"+color+"/caballo.png"
        self.bando = color
        self.escala = 0.7


