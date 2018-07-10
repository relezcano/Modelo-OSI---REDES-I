#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = "Ramiro Lezcano Pustula"
@copyright = "Copyright 2018, Capa de Enlace."
@version = "0.1"
@email = "relezcano369@gmail.com"
@materia = "Redes I"
@profesor = "Federico Martiniau"

"""

from ConfigParser import ConfigParser
from capa_fisica import Capa_fisica
from conversor import hex_to_bin
from separador import stream_to_array


class Capa_enlace():

    def __init__(self):
        pass

    def enviar_trama(self):
        conf = ConfigParser()
        conf.read("config.ini")
        cadena = conf.get("CONFIGURACION", "cadena")
        inicio = conf.get("CONFIGURACION", "inicio")
        final = conf.get("CONFIGURACION", "final")

        lista = []
        global binIni, stringList

        lenString = 8
        largo = len(cadena)

        # ALGORITMO PARA TRANSFORMAR DECIMAL DEL LARGO DE LA CADENA A BINARIO --------------------------------

        while largo > 1:
            binIni = largo % 2
            largo = largo / 2
            lista.append(binIni)

            if largo == 1:
                lista.append(largo)
                lista.reverse()  # ordeno el numero binario de 4 bits (numero de cant. elementos)
                stringList = "".join(str(x) for x in lista)

        # LARGO DE LA CADENA ----------------------------------------------

        msg = stringList
        autoCompletar = lenString - len(
            stringList)  # diferencia entre largo de la cadena y 8 para luego autocompletar con 0

        if autoCompletar == 7:
            msg = "0000000" + stringList
        elif autoCompletar == 6:
            msg = "000000" + stringList
        elif autoCompletar == 5:
            msg = "00000" + stringList
        elif autoCompletar == 4:
            msg = "0000" + stringList
        elif autoCompletar == 3:      # Autocompleto con ceros a 8 bits el numero de cantidad de caracteres de la trama
            msg = "000" + stringList
        elif autoCompletar == 2:
            msg = "00" + stringList
        elif autoCompletar == 1:
            msg = "0" + stringList

        datoArray = stream_to_array(cadena)
        lista2 = []

        for i in range(len(cadena)):
            binar = str(hex_to_bin(datoArray[i]))
            msg = str(msg) + binar                  # Transformo cada caracter a binario de 4 bits
            lista2.append(msg)

        # BIT DE PARIDAD -----------------------------------------------

        cad = msg[8:]
        contador = 0

        for num in cad:
            if num == "1":
                contador += 1  # sumo todos los 1 de la cadena

        paridad = contador % 2  # saco el resto de la división por 2 del resultado anterior

        if paridad == 1:
            mensaje = msg + "1"  # Resto 1 (impar) le agrego un 1 de paridad a la trama
        else:
            mensaje = msg + "0"  # Resto 0 (par) le agrego un 0 de paridad a la trama

        # BIT DE ORDEN -------------------------------------------------

        iterlen = lambda it: sum(1 for _ in it)
        cantLineas = iterlen(file("enviados.txt"))
        resto = cantLineas % 2  # Resto de la división por 2 de la cantidad de lineas del archivo txt
        if resto == 0:
            mensaje = "0" + mensaje  # agrego un 0 de control
        else:
            mensaje = "1" + mensaje  # agrego un 1 de control

        # INICIO Y FINAL DE LA TRAMA -----------------------------------

        trama = inicio + mensaje + final + "\n"  # Agrego inicio y final de la trama

        # ENVÍO TRAMA A LA CAPA FÍSICA ---------------------------------

        capa1 = Capa_fisica()
        capa1.send_msg(trama)
        print trama

    def leer_trama(self):

        global cadenaHexa
        f = open("enviados.txt", "r")
        lineas = f.readlines()

        for linea in lineas:

            cadenaBin = linea[17:-10]   # tomo la parte que necesito de la cadena de binarios.
            listaHexa = []

            for i in range(0, len(cadenaBin), 4):
                hexa = hex(int(cadenaBin[i:i + 4], 2))  # Transformo cada caracter a binario de 4 bits
                hexa = hexa[2:]  # Tomo el valor que necesito
                listaHexa.append(hexa)  # Lo agrego a la lista
                cadenaHexa = "".join(str(x) for x in listaHexa)  # Lo transformo en una cadena hexa

            print cadenaHexa  # Imprimo la cadena hexadeciamal.

        f.close()


capa2 = Capa_enlace()
capa2.enviar_trama()
capa2.leer_trama()
