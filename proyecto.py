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
