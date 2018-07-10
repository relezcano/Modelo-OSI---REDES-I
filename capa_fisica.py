#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author = "Ramiro Lezcano"
@copyright = "Copyright 2018, Capa de Enlace."
@version = "0.1"
@email = "relezcano369@gmail.com"
@materia = "Redes I"
@profesor = "Federico Martiniau"

"""

class Capa_fisica:

    def __init__(self):
        pass

    def send_msg(self, trama):

        f = open("enviados.txt", "a")
        f.write(trama)
        f.close()


capa = Capa_fisica()
print(capa)
