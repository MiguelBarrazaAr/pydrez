# -*- encoding: utf-8 -*-
import pilasengine

from escenas.menuPrincipal import MenuPrincipal
from escenas.conectarseAlServidor import ConectarseAlServidor
from escenas.pantallaJuego import PantallaJuego
from escenas.menuPromocion  import MenuPromocion
from escenas.menuDesafios import MenuDesafios
from escenas.desafioSuperado import DesafioSuperado
from escenas.desafio import Desafio
from escenas.modoJuego import ModoJuego

# iniciamos:
pilas = pilasengine.iniciar(ancho=1024,alto=768, titulo='pydrez 0.1 - alpha', capturar_errores=False, habilitar_mensajes_log=False)

# vinculamos las pantallas:
pilas.escenas.vincular(MenuPrincipal)
pilas.escenas.vincular(ConectarseAlServidor)
pilas.escenas.vincular(PantallaJuego)
pilas.escenas.vincular(MenuPromocion)
pilas.escenas.vincular(MenuDesafios)
pilas.escenas.vincular(Desafio)
pilas.escenas.vincular(DesafioSuperado)
pilas.escenas.vincular(ModoJuego)

pilas.escenas.MenuPrincipal(pilas=pilas)

# configuramos el cliente:
pilas.datos['modoJuego'] = "tradicional"
pilas.datos['posicion'] = None
pilas.datos['tablero'] = "8x8"


pilas.ejecutar()
