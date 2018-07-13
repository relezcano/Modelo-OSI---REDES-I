#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author = "Ramiro Lezcano"
@copyright = "Copyright 2018, Capa de Fisica."
@version = "0.1"
@email = "relezcano369@gmail.com"
@materia = "Redes I"
@profesor = "Federico Martiniau"

"""


class Capa_fisica():

    def __init__(self):
        pass

    def send_msg(self, trama):
        f = open("enviados.txt", "a")
        f.write(trama)
        f.close()

    def leer_trama(self):

        global cadenaHexa
        f = open("enviados.txt", "r")
        lineas = f.readlines()

        for linea in lineas:
            cadenaBin = linea[194:-10]  # tomo la parte que necesito de la cadena de binarios.
            listaHexa = []

            for i in range(0, len(cadenaBin), 4):
                hexa = hex(int(cadenaBin[i:i + 4], 2))  # Transformo cada caracter a binario de 4 bits
                hexa = hexa[2:]  # Tomo el valor que necesito
                listaHexa.append(hexa)  # Lo agrego a la lista
                cadenaHexa = "".join(str(x) for x in listaHexa)  # Lo transformo en una cadena hexa

            print "Cadena Hexa de la trama: ", cadenaHexa   # Imprimo la cadena hexadeciamal de la trama.

        f.close()


capa = Capa_fisica()

