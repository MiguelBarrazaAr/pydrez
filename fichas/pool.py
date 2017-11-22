# -*- encoding: utf-8 -*-

from actores.ficha import Ficha
from .alfil import Alfil
from .caballo import Caballo
from .dama import Dama
from .peon import Peon
from .rey import Rey
from .torre import Torre

# especiales:
from .enano import Enano
from .golem import Golem
from .lobo import Lobo
from .dragon import Dragon
from .pegaso import Pegaso
from .caballero_oscuro import Caballero_oscuro
from .conejo import Conejo
from .hipogrifo import Hipogrifo
from .licantropo import Licantropo
from .serpiente import Serpiente
from .murcielago_oscuro import Murcielago_oscuro

class PoolDeFichas():

    def __init__(self, pilas, cantidadDeFichas=32):
        self.pilas = pilas
        self.fichas = pilas.actores.Grupo()
        self.tablero = None
        self.pilas.log('Se inicia el pool de fichas con', cantidadDeFichas, 'fichas')
        # comportamientos:
        self.comportamientos = {
            'alfil':Alfil,
            'caballero_oscuro':Caballero_oscuro,
            'caballo':Caballo,
            'conejo':Conejo,
            'dama':Dama,
            'dragon':Dragon,
            'enano':Enano,
            'golem':Golem,
            'hipogrifo':Hipogrifo,
            'licantropo':Licantropo,
            'lobo':Lobo,
            'murcielago_oscuro':Murcielago_oscuro,
            'pegaso':Pegaso,
            'peon':Peon,
            'rey':Rey,
            'serpiente':Serpiente,
            'torre':Torre}
        self.prefijo = {
            'a':'alfil',
            'co':'caballero_oscuro',
            'c':'caballo',
            'con':'conejo',
            'd':'dama',
            'dr':'dragon',
            'e':'enano',
            'g':'golem',
            'h':'hipogrifo',
            'li':'licantropo',
            'l':'lobo',
            'm':'murcielago_oscuro',
            'pe':'pegaso',
            'p':'peon',
            'r':'rey',
            's':'serpiente',
            't':'torre'
        }

        # iniciamos las fichas:
        for x in range(cantidadDeFichas):
            self.fichas.agregar(Ficha(pilas))

    def definir_tablero(self, tablero):
        self.tablero = tablero

    def generar(self, tipoDeFicha, color):
        ficha = self.buscar_ficha_libre()

        ficha.definir_comportamiento(self.comportamientos[tipoDeFicha](color))
        ficha.definir_tablero(self.tablero)
        return ficha

    def buscar_ficha_libre(self):
        """busca una ficha que este libre.
        si no la encuentra genera una ficha nueva para el pool."""
        for ficha in self.fichas:
            if ficha.noTieneComportamiento():
                return ficha

        # no encontro ninguna ficha libre, genera nueva:
        ficha = Ficha(self.pilas)
        fichas.agregar(ficha)
        self.pilas.log("se agranda el pool de fichas, ahora tiene", len(self.fichas), "fichas")
        return ficha

    def fichasActivas(self):
        """Cuenta las fichas activas."""
        cantidad = 0
        for ficha in self.fichas:
            if ficha.tieneComportamiento():
                cantidad += 1

        return cantidad

    def limpiar(self):
        """Elimina de pantalla la fichas Activas."""
        for ficha in self.fichas:
            if ficha.tieneComportamiento():
                ficha.eliminar()

    def posicion(self):
        """Retorna una lista de strings con la posici�n de las fichas"""
        posicion = ""
        for ficha in self.fichas:
            if ficha.tieneComportamiento():
                if posicion == "":
                    posicion += repr(ficha)+str(ficha.celda)
                else:
                    posicion += " "+repr(ficha)+str(ficha.celda)

        return posicion

    def cargarPosicion(self, texto):
        """Carga una posicion indicada por parametro"""
        self.limpiar()
        lista = texto.split(" ")
        color = ""

        for n, x in enumerate(lista):
            if lista[n][0].islower():
                color="negro"
            else:
                color = "blanco"

            lista[n] = (
                self.prefijo[(lista[n][0].lower())],
                color,
                ord(lista[n][1])-97,
                int(lista[n][2:])-1)

        for ficha in lista:
            self.tablero.posicionar(self.generar(ficha[0], ficha[1]), ficha[2], ficha[3])
