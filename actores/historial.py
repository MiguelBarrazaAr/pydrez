from pilasengine.actores.actor import Actor


class Historial(Actor):
    
    def iniciar(self,ejex,ejey):
        self.posicion = 0
        self.imagen = "invisible.png"
        self.lineas = []

        # Este se tendria que quitar
        self.actor_texto = self.pilas.actores.Texto(x=-90, y=90)
        self.actor_texto.ancho = 240
        self.actor_texto.x = ejex
        self.actor_texto.y = ejey
        self.actor_texto.escala = 0.5
        self.borde = self.pilas.actores.Pizarra()
        self.lineas.append("")
        self.actualizar_textos()
        self.numero = 1
       
    def agregar(self, mensaje):
        self.lineas.append(str(self.numero ) + "." +mensaje)
        self.actualizar_textos()
        self.numero += 1
        if(len(self.lineas) > 14):
            self.bajar()

    def subir(self):
        self.posicion -= 1
        if self.posicion < 0:
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
        cantidad_de_lineas = 14
        lineas_a_mostrar = self.lineas[self.posicion:self.posicion+cantidad_de_lineas]
        self.actor_texto.texto = "\n".join(lineas_a_mostrar)
        self.actor_texto.centro_y = 0
        self.actor_texto.centro_x = 0