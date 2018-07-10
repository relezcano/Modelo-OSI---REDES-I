#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ramiro Lezcano"
__copyright__ = "Copyright 2018, Conversor Hexa/Bin | Bin/Hexa"
__version__ = "0.1"
__email__ = "relezcano369@gmail.com"
__materia__ = "Redes I"
__profesor__ = "Federico Martiniau"

import sys, os


def hex_to_bin(cadena):

    hexaNum = cadena

    if hexaNum == "0":
        datoBin = '0000'

    elif hexaNum == "1":
        datoBin = '0001'

    elif hexaNum == "2":
        datoBin = '0010'

    elif hexaNum == "3":
        datoBin = '0011'

    elif hexaNum == "4":
        datoBin = '0100'

    elif hexaNum == "5":
        datoBin = '0101'

    elif hexaNum == "6":
        datoBin = '0101'

    elif hexaNum == "7":
        datoBin = '0110'

    elif hexaNum == "8":
        datoBin = '0111'

    elif hexaNum == "9":
        datoBin = '1001'

    elif hexaNum == "a" or hexaNum == "A":
        datoBin = '1010'

    elif hexaNum == "b" or hexaNum == "B":
        datoBin = '1011'

    elif hexaNum == "c" or hexaNum == "C":
        datoBin = '1100'

    elif hexaNum == "d" or hexaNum == "D":
        datoBin = '1101'

    elif hexaNum == "e" or hexaNum == "E":
        datoBin = '1110'

    elif hexaNum == "f" or hexaNum == "F":
        datoBin = '1111'

    return datoBin


def bin_to_hex(cadena):

    binNum = cadena

    if binNum == "0000":
        datoHexa = '0'

    elif binNum == "0001":
        datoHexa = '1'

    elif binNum == "0010":
        datoHexa = '2'

    elif binNum == "0011":
        datoHexa = '3'

    elif binNum == "0100":
        datoHexa = '4'

    elif binNum == "0101":
        datoHexa = '5'

    elif binNum == "0110":
        datoHexa = '6'

    elif binNum == "0111":
        datoHexa = '7'

    elif binNum == "1000":
        datoHexa = '8'

    elif binNum == "1001":
        datoHexa = '9'

    elif binNum == "1010":
        datoHexa = 'A'

    elif binNum == "1011":
        datoHexa = 'B'

    elif binNum == "1100":
        datoHexa = 'C'

    elif binNum == "1101":
        datoHexa = 'D'

    elif binNum == "1110":
        datoHexa = 'E'

    elif binNum == "1111":
        datoHexa = 'F'

    return datoHexa
