
Id = 0
class Imagen:

    def __init__(self,path,nombre):
        self.Direccion = path
        self.NombreDEImagen = nombre
        self.Etiqueta = None
        self.Genero = []
        global Id
        Id += 1
        self.Id = Id
    def show(self):
        return str(self.Direccion)+"-"+str(self.NombreDEImagen)+"-"+str(self.Etiqueta)+"-"+str(self.Genero)

    def getEtiqueta(self):
        return str(self.Etiqueta)

    def TamaoEtiqueta(self):
        return len(self.Etiqueta)

    def Direccion(self):
        return self.Direccion

    def NombreDEImagen(self):
        return self.NombreDEImagen

    def  setGenero(self,nuevoGenero):
        return self.Genero.append(nuevoGenero)

    def getName(self):
        return str(self.NombreDEImagen)+str(self.Direccion)
