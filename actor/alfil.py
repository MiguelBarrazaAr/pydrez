from pilasengine.actores.actor import Actor

class Alfil(Actor):

    def iniciar(self, color="blanco"):
        self.imagen = "imagenes/pieza/"+color+"/alfil.png"
        self.bando = color
        self.escala = 0.7


