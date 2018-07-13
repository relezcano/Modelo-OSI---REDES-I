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
from capa_red import Capa_red


class Capa_enlace():

    def __init__(self):
        pass

    def enviar_trama(self):
        conf = ConfigParser()
        conf.read("config.ini")
        cadena = conf.get("CONFIGURACION", "cadena")
        inicio = conf.get("CONFIGURACION", "inicio")
        final = conf.get("CONFIGURACION", "final")
        global binIni, stringList

        # Header -------------------------------------------------------------------------------------------------------
        hlen = ""
        typeS = ""
        total = ""
        iD = ""
        flaG = ""
        offSet = ""
        ttlive = ""
        protocol = ""
        checkSum = ""
        ipO = ""
        ipD = ""

        capa3 = Capa_red()
        header = capa3.send_header()

        vers = header[:1]
        longi = header[1:3]
        ts = header[3:5]
        long_total = header[5:9]
        id = header[9:13]
        flag = header[13:15]
        offset = header[15:18]
        ttl = header[18:20]
        prot = header[20:22]
        checksum = header[22:26]
        ip_origen = header[26:34]
        ip_destino = header[34:42]

        verBin = bin(int(vers, 16))[2:].zfill(4)

        for i in range(len(longi)):
            lonBin = bin(int(longi[i], 16))[2:].zfill(4)
            hlen = hlen + str(lonBin)

        for i in range(len(ts)):
            tsBin = bin(int(ts[i], 16))[2:].zfill(4)
            typeS = typeS + str(tsBin)

        for i in range(len(long_total)):
            totalBin = bin(int(long_total[i], 16))[2:].zfill(4)
            total = total + str(totalBin)

        for i in range(len(id)):
            idBin = bin(int(id[i], 16))[2:].zfill(4)
            iD = iD + str(idBin)

        for i in range(len(flag)):
            flagBin = bin(int(flag[i], 16))[2:].zfill(4)
            flaG = flaG + str(flagBin)

        for i in range(len(offset)):
            offBin = bin(int(offset[i], 16))[2:].zfill(4)
            offSet = offSet + str(offBin)

        for i in range(len(ttl)):
            ttlBin = bin(int(ttl[i], 16))[2:].zfill(4)
            ttlive = ttlive + str(ttlBin)

        for i in range(len(prot)):
            protBin = bin(int(prot[i], 16))[2:].zfill(4)
            protocol = protocol + str(protBin)

        for i in range(len(checksum)):
            checkBin = bin(int(checksum[i], 16))[2:].zfill(4)
            checkSum = checkSum + str(checkBin)

        for i in range(len(ip_origen)):
            ipoBin = bin(int(ip_origen[i], 16))[2:].zfill(4)
            ipO = ipO + str(ipoBin)

        for i in range(len(ip_destino)):
            ipdBin = bin(int(ip_destino[i], 16))[2:].zfill(4)
            ipD = ipD + str(ipdBin)

        head = verBin + hlen + typeS + total + iD + flaG + offSet + ttlive + protocol + checkSum + ipO + ipD
        print
        print "Encabezado en binario: ", head

        # Cuerpo de la cadena ------------------------------------------------------------------------------------------
        lista = []
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
        autoCompletar = lenString - len(stringList)  # diferencia entre largo de la cadena y 8 para luego autocompletar con 0

        if autoCompletar == 7:
            msg = "0000000" + stringList
        elif autoCompletar == 6:
            msg = "000000" + stringList
        elif autoCompletar == 5:
            msg = "00000" + stringList
        elif autoCompletar == 4:
            msg = "0000" + stringList
        elif autoCompletar == 3:  # Autocompleto con ceros a 8 bits el numero de cantidad de caracteres de la trama
            msg = "000" + stringList
        elif autoCompletar == 2:
            msg = "00" + stringList
        elif autoCompletar == 1:
            msg = "0" + stringList

        datoArray = stream_to_array(cadena)
        lista2 = []

        for i in range(len(cadena)):
            binar = str(hex_to_bin(datoArray[i]))
            msg = str(msg) + binar  # Transformo cada caracter a binario de 4 bits
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

        trama = inicio + mensaje + final  # Agrego inicio y final de la trama

        # AGREGO HEAD A TA TRAMA

        trama = head + trama

        # Numero de trama ----------------------------------------------

        contrama = 0
        f = open("enviados.txt", "r")
        lineas = f.readlines()
        for l in lineas:
            contrama = contrama + 1

        contadorTrama = contrama + 1
        numtram = "TRAMA " + str(contadorTrama) + ": "
        trama = numtram + trama + "\n"

        # ENVÍO TRAMA A LA CAPA FÍSICA ---------------------------------

        capa1 = Capa_fisica()
        capa1.send_msg(trama)
        print
        print "Trama completa ingresada --> ", trama


capa1 = Capa_fisica()
capa2 = Capa_enlace()
capa3 = Capa_red()

capa2.enviar_trama()
capa3.read_header()
print
capa1.leer_trama()
