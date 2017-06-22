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
print Prueba.size(),"final"
print Prueba.show()
Prueba.AsignarEtiqueta()
print Prueba.show()

#label=tk.Label(vp,image=img2).grid(column=0,row=0)
#Prueba.etiqueta()
#Prueba.AsignarGenero()
#print Prueba.show()
#print Prueba.getGeneros()
#print Prueba.To_Json()
