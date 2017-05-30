
Id = 0
class Imagen:

    def __init__(self,path,nombre):
        self.Direccion = path
        self.NombreDEImagen = nombre
        self.Etiqueta = []
        self.Genero = None
        global Id
        Id += 1
        self.Id = Id
    def show(self):
        return str(self.Direccion)+"-"+str(self.NombreDEImagen)+"-"+str(self.Etiqueta)+"-"+str(self.Genero)

    def Etiqueta(self):
        return self.Etiqueta

    def Direccion(self):
        return self.Direccion

    def NombreDEImagen(self):
        return self.NombreDEImagen

    def  Genero(self):
        return self.Genero

    def getName(self):
        return str(self.NombreDEImagen)
