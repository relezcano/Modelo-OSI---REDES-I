#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = "Ramiro Lezcano Pustula"
@copyright = "Copyright 2018, Capa de Red."
@version = "0.1"
@email = "relezcano369@gmail.com"
@materia = "Redes I"
@profesor = "Federico Martiniau"

"""


class Capa_red():

    def __init__(self):
        self.vers = "1"  # 4 bits / 1 caracter
        self.longi = "3d"  # 8 bits
        self.ts = "ef"  # 8 bits
        self.long_total = "c75b"  # 16 bits
        self.id = "7efa"  # 16 bits
        self.flag = "26"  # 8 bits
        self.offset = "de6"  # 12 bits
        self.ttl = "30"  # 8 bits
        self.protocolo = "c8"  # 8 bits / 2 caracteres
        self.checksum = "6e1b"  # 16 bits / 4 caracteres
        self.ip_origen = "c0a83245"  # 32 bits / 8 caracteres
        self.ip_destino = "c0a8325a"  # 32 bits / 8 caracteres
        # self.relleno = "00000000"  # 32 bits / 8 caracteres

    def send_header(self):

        encabezado = self.vers + self.longi + self.ts + self.long_total + self.id + self.flag + self.offset + self.ttl + self.protocolo + self.checksum + self.ip_origen + self.ip_destino
        return encabezado

    def read_header(self):

        global cadenaHeader
        f = open("enviados.txt", "r")
        lineas = f.readlines()
        for linea in lineas:

            cadenaHead = linea[9:177]
            listaHead = []

            for i in range(0, len(cadenaHead), 4):
                hexa = hex(int(cadenaHead[i:i + 4], 2))  # Transformo cada caracter a binario de 4 bits
                hexa = hexa[2:]  # Tomo el valor que necesito
                listaHead.append(hexa)  # Lo agrego a la lista
                cadenaHeader = "".join(str(x) for x in listaHead)

            print "Cadena Hexa del header: ", cadenaHeader  # Imprimo la cadena hexadeciamal del header.

        f.close()


capaRed = Capa_red()
