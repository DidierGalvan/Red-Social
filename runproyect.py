from proyecto import *
from libreria import *
from imagen import *
Fun = []
Prueba = Libreria()
def trabaja(A):
#/home/eric/java/imagenes
    for i in range(len(A.keys())):
            ruta = A.keys()[i]
            for j in range(len(A.values()[i])):
                nombre = A.values()[i][j]
                Prueba.AgregarImagen(ruta,nombre)



trabaja(A)
#print Prueba.size(),"final"
#print Prueba.show()
Prueba.asignacion()
print Prueba.ruta1[1]
directorio=Prueba.ruta1[1]
print directorio
#for i in Prueba.ruta1:
Prueba.AsignarEtiqueta()
Prueba.ListaAsignacion()
print Prueba.show()

#label=tk.Label(vp,image=img2).grid(column=0,row=0)
#Prueba.etiqueta()
#Prueba.AsignarGenero()
#print Prueba.show()
#print Prueba.getGeneros()
#print Prueba.To_Json()
