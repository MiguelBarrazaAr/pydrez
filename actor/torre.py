from pilasengine.actores.actor import Actor

class Torre(Actor):

    def iniciar(self, color="blanco"):
        self.imagen = "imagenes/pieza/"+color+"/torre.png"
        self.bando = color
        self.escala = 0.7


