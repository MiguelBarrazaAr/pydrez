# -*- encoding: utf-8 -*-

from .rio import TableroRio

definiciones = {
    "rio":TableroRio,
}

def generar(clave):
    return definiciones[clave]
