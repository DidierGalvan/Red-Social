#-*- coding: utf-8 -*-
from proyecto import *
from libreria import *
from imagen import *
Fun = []
Prueba = Libreria()
def trabaja(A):
    for i in range(len(A.keys())):
            ruta = A.keys()[i]
            for j in range(len(A.values()[i])):
                nombre = A.values()[i][j]
                Prueba.AgregarImagen(ruta,nombre)



trabaja(A)
Prueba.asignacion()
Prueba.AsignarEtiqueta()
Prueba.ListaAsignacion()
Prueba.AsignarGenero()
print Prueba.show()
Prueba.To_Json()
Prueba.Escribe("enviar.txt")
