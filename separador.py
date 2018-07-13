#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ramiro Lezcano"
__copyright__ = "Copyright 2018, Separador"
__version__ = "0.1"
__email__ = "relezcano369@gmail.com"
__materia__ = "Redes I"
__profesor__ = "Federico Martiniau"

import sys, os


def stream_to_array(stream):
    # print "--------------------------------------------"
    # stream = raw_input("Ingrese numeros: ")
    array = list(stream)
    return array
    # print "
    # print "El arreglo es: ",array
    # print ""


def array_to_stream(array):
    # print "--------------------------------------------------------"
    # print ""
    # print "* Ingresar cantidad de posiciones y valores del arreglo *"
    # print ""

    # largo = input("Cuantas posiciones tendra su arreglo?: ")
    # print ""

    stream = []

    for i in array:
        stream.append(i)

    # print ""
    stream = "".join(str(espacio) for espacio in stream)
    # print "La cadena es: ",stream
    # print ""
    exit()

# print ""
# print "@-------------------------------------@"
# print "|  Stream to Array - Array to Stream  |"
# print "@-------------------------------------@"
# print ""
# print "1) Stream to Array"
# print "2) Array to Stream"
# print ""
# opcion = input("Escriba el Numero de la opcion deseada: ")
# print ""
# if opcion == 1:
#     stream_to_array()
# elif opcion == 2:
#     array_to_stream()
# while opcion != 1 & opcion != 2:
#     print "____________________________________________________________________________"
#     print ""
#     print "  ERROR... Ingrese '1' para Stream/Array o la opcion '2' para Array/Stream"
#     print "____________________________________________________________________________"
#     print ""
#     opcion = input("Escriba el Numero de la opcion deseada: ")
#     if opcion == 1:
#         stream_to_array()
#     elif opcion == 2:
#         array_to_stream()
