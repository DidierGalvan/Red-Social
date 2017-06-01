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
    def getGeneros(self):
        for key, value in self.Generos.iteritems():
            for valor in value:
                print key,"=>",valor.getName()

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
                etiqueta = etiquetas.split(' ')
                self.Libro[i].Etiqueta = etiqueta
            except AttributeError:
                print "Eso no es imagen"
            except IOError:
                print "Eso no es imagen"
    def AsignarGenero(self):
        tamano = len(self.Libro)
        for i in range(tamano):
            a = self.Libro[i]
            ListaEti= a.getEtiqueta()
            for Eti in ListaEti:
                Etis = Eti
                for t in range(len(self.Generos.keys())):
                    if Etis == self.Generos.keys()[t]:
                        nombre = a.getName
                        self.Generos[Etis].append(nombre)
                        a.setGenero(self.Generos.keys()[t])

    def ElemenetosPorGenero(self,Genero):
            print len(Generos[Genero].values())
    def buscar(self,go_id,stop_id):
        for i in self.Libro:
            if i.Id >= go_id and i.Id<=stop_id:
                print i
