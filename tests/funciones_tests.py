import csv

def leerCSV(path):
    with open(path, newline=';') as File:  
        lista = list(csv.reader(File))
        return lista