# -*- encoding: utf-8 -*-
import pilasengine

from escenas.menuPrincipal import MenuPrincipal
from escenas.configurar import Configurar
from escenas.elegirColor import ElegirColor
from escenas.conectarseAlServidor import ConectarseAlServidor
from escenas.pantallaJuego import PantallaJuego
from escenas.menuPromocion  import MenuPromocion
from escenas.menuDesafios import MenuDesafios
from escenas.desafioSuperado import DesafioSuperado
from escenas.desafio import Desafio
from escenas.modoJuego import ModoJuego
from escenas.creditos import Creditos
from escenas.ganasteLosDesafios import GanasteLosDesafios

# iniciamos:
pilas = pilasengine.iniciar(ancho=1024,alto=768, titulo='pydrez 1.1 - alpha', capturar_errores=False, habilitar_mensajes_log=False)
pilas.forzar_habilitacion_de_audio()

# vinculamos las pantallas:
pilas.escenas.vincular(MenuPrincipal)
pilas.escenas.vincular(Configurar)
pilas.escenas.vincular(ElegirColor)
pilas.escenas.vincular(ConectarseAlServidor)
pilas.escenas.vincular(PantallaJuego)
pilas.escenas.vincular(MenuPromocion)
pilas.escenas.vincular(MenuDesafios)
pilas.escenas.vincular(Desafio)
pilas.escenas.vincular(DesafioSuperado)
pilas.escenas.vincular(ModoJuego)
pilas.escenas.vincular(Creditos)
pilas.escenas.vincular(GanasteLosDesafios)

# configuramos el cliente:
pilas.datos['modoJuego'] = "ajedrezIa"
pilas.datos['posicion'] = None
pilas.datos['tablero'] = "8x8"
pilas.datos['fichasFx'] = "off"
# musica:
pilas.datos['musica'] = pilas.musica.cargar('audio/presentacion.mp3')

pilas.escenas.MenuPrincipal(pilas=pilas)
pilas.ejecutar()
