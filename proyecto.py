#!/usr/bin/env python
#-*-coding: utf-8-*-
#-*-coding: cp1252-*-
#-*-coding: Windows-1252-*-
#-*-coding: IBM850-*-
from os import walk

A = {}
#path = raw_input("Dame la ruta de la carpeta de imagenes:"+" ")
path = "/home/eric/java/imagenes"
for (path,ficheros,archivo) in walk(path):
    lista = [path]
    lista2= archivo
    for i in lista:
        A[i]=[]
        for j in lista2:
            A[i].append(j)
