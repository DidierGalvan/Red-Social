from imagen import *
from proyecto import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
from Tkinter import *
import sys
from PIL import Image
from PIL import ImageTk
import Tkinter as tk

class Libreria:

    def __init__(self):
        self.Libro = []
        self.Generos = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[]}
        self.Json = []
        self.ruta1 = []
        self.etequetas = []
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

    def frame(self,NombreTk,side):
        w= Frame(NombreTk)
        w.pack(side=side,expand=YES,fill=BOTH)
        return w

    def Etiquis(self,obtencion):
        etiqueta = obtencion.split(' ')
        self.etequetas.append(etiqueta)
        return True


    def siguiente(self,num,vp):
            try:
                cargar=Image.open(self.ruta1[num])
                img=cargar.resize((500,400),Image.ANTIALIAS)
                img2=ImageTk.PhotoImage(img)
                label=tk.Label(vp,image=img2).grid(column=0,row=0)
            except:
                label=tk.Label(vp, text = 'Esto no es imagen').grid(column=0,row=0)

    def asignacion(self):
        print Etiquis('hola fg')
        for i in range(len(A.keys())):
                ruta = A.keys()[i]
                for j in range(len(A.values()[i])):
                    strg= ""
                    nombre = A.values()[i][j]
                    strg = ruta +'/'+ nombre
                    self.ruta1.append(strg)
    def AsignarEtiqueta(self):
        app=Tk()
        app.title("Etiquetar imagen")
        vp=self.frame(app,LEFT)
        vp.grid(column=0,row=0,padx=(10,10),pady=(1,1))
        etiques = StringVar()
        obtencion = etiques.get()

        etiqueta=Label(vp,text="Etiqueta:").grid(column=1,row=0)
        e1=Entry(vp, textvariable=etiques)
        e1.grid(column=2,row=0)
        self.asignacion()
        print Etiquis(str(obtencion))
        boton1=Button(vp,text="Siguente", command = app.quit ).grid(column=2,row=1)
        boton2=Button(vp,text="Aceptar", command = self.Etiquet()).grid(column=1,row=1)
        for i in range(len(self.ruta1)):
            try:
                cargar=Image.open(self.ruta1[i])
                img=cargar.resize((500,400),Image.ANTIALIAS)
                img2=ImageTk.PhotoImage(img)
                label=tk.Label(vp,image=img2).grid(column=0,row=0)
                app.mainloop()
            except:
                label=tk.Label(vp, text = 'Esto no es imagen').grid(column=0,row=0)
                app.mainloop()



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
    def To_Json(self):
        for imagen in self.Libro:
            path = imagen.Direccion
            nombre = imagen.NombreDEImagen
            Eti = imagen.Etiqueta
            a = {"Nombre":nombre,"Direccion":path,"Etiquetas":Eti}
            self.Json.append(a)
