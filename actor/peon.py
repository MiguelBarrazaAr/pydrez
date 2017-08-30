from pilasengine.actores.actor import Actor

class Peon(Actor):

    def iniciar(self, color="blanco"):
        self.imagen = "imagenes/pieza/"+color+"/peon.png"
        self.bando = color
        self.escala = 0.7


