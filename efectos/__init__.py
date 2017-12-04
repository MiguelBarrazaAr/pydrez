# -*- encoding: utf-8 -*-

from .agua import FxAgua

definiciones = {
    "agua":FxAgua,
}

def generar(clave):
    return definiciones[clave]
