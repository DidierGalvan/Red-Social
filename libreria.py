from imagen import *
from proyecto import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

class Libreria:

    def __init__(self):
        self.Libro = []
        self.Generos = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[]}
    def size(self):
        return len(self.Libro)
    def show(self):
        for imagen in self.Libro:
            print imagen.show()
    def AgregarImagen(self,nombre,ruta):
        print self.size()
        self.Libro.append(Imagen(nombre,ruta))

    def AsignarEtiqueta(self):
        ruta1 = []
        for i in range(len(A.keys())):
                ruta = A.keys()[i]
                for j in range(len(A.values()[i])):
                    strg= ""
                    nombre = A.values()[i][j]
                    strg = ruta +'/'+ nombre
                    ruta1.append(strg)
        for i in range(len(ruta1)):
            try:
                img = Image.open(ruta1[i])
                plt.imshow(img)
                plt.show()
                etiquetas= raw_input("Etiqueta: ")
                etiqueta = etiquetas.split(',')
                self.Libro[i].Etiqueta = etiqueta
            except AttributeError:
                print "Eso no es imagen"
            except IOError:
                print "Eso no es imagen"
    def AsignarGenero(self):
            tamano = self.size()
        for i in range(tamano):
            a = self[i]
            if len(a.Etiqueta()) == 1:
                for j in range(len(self.Generos.keys())):
                    if a.Etiqueta == self.Generos.keys()[j]:
                        self.Generos[i].append(a)
                        a.Genero = keys()[j]
            else:
                for i in a.Etiqueta:
                    if a.Etiqueta == self.Generos.keys()[j]:
                        self.Generos[i].append(a)
                        a.Genero = keys()[j]

    def ElemenetosPorGenero(self,Genero):
            print len(Generos[Genero].values())
    def buscar(self,go_id,stop_id):
        for i in self.Libro:
            if i.Id >= go_id and i.Id<=stop_id:
                print i
