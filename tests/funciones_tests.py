
import csv

#Usada para pasar a lista un CSV con los datos de prueba de regresion lineal
def leerCSV(path):
    csvarchivo = open(path, encoding="utf8")  
    lista = list(csv.reader(csvarchivo, delimiter=";"))
    csvarchivo.close()
    return lista

#Convierte la lista devuelta por leerCSV en una lista de floats
def convertStringToFloatList(list):

    for pos_fila, fila in enumerate(list):
        for pos_columna, elemento in enumerate(fila):
            list[pos_fila][pos_columna] = float(elemento)
    return list
