# -*- encoding: utf-8 -*-
import pilasengine

from actores.menu import MenuAccesible

class MenuPrincipal(pilasengine.escenas.Escena):

    def iniciar(self, pilas, tts):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        opciones = [('jugar', self.jugar),
                    (u'desafíos', self.desafios),
                    ('conectarse', self.conectarse),
                    ('tutorial', self.tutorial),
                    ('creditos', self.creditos),
                    ('salir', self.salir)]
        self.menu = MenuAccesible(pilas, y = 50 , opciones = opciones, tts=tts)
        self.decir(u"menú principal: pulse las flechas para navegar por el menú.", False)


    def jugar(self):
        self.pilas.escenas.PantallaJuego(pilas=self.pilas, tts=self.decir)

    def desafios(self):
        self.pilas.escenas.Desafio(pilas=self.pilas, tts=self.decir)

    def conectarse(self):
        print("conectarse")

    def tutorial(self):
        print("tutorial")

    def creditos(self):
        print("creditos")

    def salir(self):
        exit()