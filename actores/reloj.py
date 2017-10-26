from pilasengine.actores.actor import Actor
from pilasengine.colores import *

class Reloj(Actor):

    def iniciar(self, x=0, y=0, incremental=True):
        self.incremental = incremental
        self.imagen = "invisible.png"
        self.minutos = 0
        self.segundos = 0
        self.tarea_en_curso = None
        self.texto = self.pilas.actores.Texto(str(self.minutos) + ":" + str(self.segundos))
        self.texto.x = x
        self.texto.y = y
        self.texto.color = negro

    def configurar(self, min, seg):
        self.minutos = min
        if seg >= 59:
        	self.segundos = 59
        else:
        	self.segundos = seg
        self.actualizarTexto()


    def comenzar(self):
        if self.tarea_en_curso == None:
            if self.incremental:
                self.tarea_en_curso = self.pilas.tareas.siempre(1, self.aumentarAlContador)
            else:
                self.tarea_en_curso = self.pilas.tareas.siempre(1, self.restarAlContador)

    def restarAlContador(self):
    	if self.segundos >= 1 or self.minutos >= 1:
    		if self.segundos >= 1:
        		self.segundos -= 1
        	else:
        		self.minutos -= 1
        		self.segundos = 59
        self.actualizarTexto()

    def aumentarAlContador(self):
        if self.segundos < 59:
            self.segundos += 1
        else:
            self.minutos += 1
            self.segundos = 0
        self.actualizarTexto()

    def actualizarTexto(self):
    	self.texto.texto = (str(self.minutos) + ":" + str(self.segundos))

    def pausar(self):
         self.tarea_en_curso.eliminar()
         self.tarea_en_curso = None


