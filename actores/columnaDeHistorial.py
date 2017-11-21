from pilasengine.actores.actor import Actor

class ColumnaDeHistorial(Actor):
    
    def iniciar(self,ejex,ejey):
        self.posicion = 0
        self.imagen = "invisible.png"

        self.lineas = []

        self.cantidad_de_lineas = 14
        self.actor_texto = self.pilas.actores.Texto(x=-90, y=90)
        self.actor_texto.ancho = 240
        self.actor_texto.x = ejex - 26
        self.actor_texto.y = ejey - 45
        self.actor_texto.color = self.pilas.colores.negro
        self.actor_texto.escala = 0.5
        self.borde = self.pilas.actores.Pizarra()
        self.lineas.append("")
        self.actualizar_textos()
       
    def agregar(self, mensaje):
        self.lineas.append(mensaje)
        self.actualizar_textos()
        if(len(self.lineas) > 14):
            self.bajar()

    def remplazar(self,mensaje):
        self.lineas [len(self.lineas) - 1] = mensaje
        self.actualizar_textos()

    def subir(self):

        self.posicion -= 1
        if self.posicion < 1:
            self.posicion = 1
        self.actualizar_textos()
        
    def bajar(self):
        self.posicion += 1
        
        if self.posicion > len(self.lineas) - 14:
            self.posicion = len(self.lineas) - 14

        self.actualizar_textos()
        
    def evitar_desborde(self):
        self.posicion = max(self.posicion, 0)
    
    def actualizar_textos(self):
        lineas_a_mostrar = self.lineas[self.posicion:self.posicion + self.cantidad_de_lineas ]
        self.actor_texto.texto = "\n".join(lineas_a_mostrar)
        self.actor_texto.centro_y = 0
        self.actor_texto.centro_x = 0