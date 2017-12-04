# -*- encoding: utf-8 -*-

from .agua import FxAgua
from .lava import FxLava

definiciones = {
    "agua":FxAgua,
    "lava":FxLava
}

def generar(clave):
    return definiciones[clave]
