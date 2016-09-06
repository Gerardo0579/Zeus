import csv
import glob
import os

def listarArchivos():
    pathTexto = os.path.dirname(os.path.abspath(__file__)) + "\\*.csv"
    directorios = glob.glob(pathTexto)
    archivo = ""
    for var in directorios:
        print ('NOMBRE DEL ARCHIVO: ' + var)
        archivo = csv.reader(open(var, 'r'), delimiter=';')
        print ('\nBloque: ' + str(index + 1))

def obtenerInformacion(pathArchivo):
    pathTexto = os.path.dirname(os.path.abspath(__file__)) + "\\" + pathArchivo + ".csv"
    directorio = glob.glob(pathTexto)
    archivo = ""
    archivo = csv.reader(open(directorio[0], 'r'), delimiter=';')
    for index,row in enumerate(archivo):
        print ("\n Bloque: " + str(index + 1) )
        for dato in row:
            if len(dato)>0:
                print ("Dato:" + dato + "\n")

def obtenerInformacionBloque(pathArchivo, bloque):
    pathTexto = os.path.dirname(os.path.abspath(__file__)) + "\\" + pathArchivo + ".csv"
    directorio = glob.glob(pathTexto)
    archivo = ""
    archivo = csv.reader(open(directorio[0], 'r'), delimiter=';')
    for index,row in enumerate(archivo):
        if row[0] == bloque:
            print ("\n Bloque: " + str(index + 1) )
            for dato in row:
                if len(dato)>0:
                    print ("Dato:" + dato + "\n")

#obtenerInformacion("fisica1")
obtenerInformacionBloque("fisica1", "Bloque 1 declarativo")
