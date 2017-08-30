from pilasengine.actores.actor import Actor

class Rey(Actor):

    def iniciar(self, color="blanco"):
        self.imagen = "imagenes/pieza/"+color+"/rey.png"
        self.bando = color
        self.escala = 0.7


