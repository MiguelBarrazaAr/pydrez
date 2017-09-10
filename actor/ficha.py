from pilasengine.actores.actor import Actor

class Ficha(Actor):

    def iniciar(self, color="blanco", fila=0, columna=0):
        self.imagen = "imagenes/pieza/"+color+"/"+self.nombre()+".png"
        self.color = color
        self.escala = 0.7
        self.columna = columna
        self.fila = fila
        self.tablero = None

    def definirTablero(self, tablero):
        self.tablero = tablero
