

import pytest
import tests.funciones_tests
import source.funciones
import numpy as np

#Se asegura que la regresion lineal devuelve un valor entre 0 y 5
def regLinValorCorrecto():
    
    #Entrada de datos de training
    list_train = funciones_tests.leerCSV("train_data.txt")
    list_train = funciones_tests.convertStringToFloatList(list_train)
    
    #Entrenamiento
    pesos = funciones.regLin(list_train)
    
    #Entrada de datos de test
    list_test = funciones_tests.leerCSV("test_data.txt")
    list_test = funciones_tests.convertStringToFloatList(list_test)[0]
    
    list_test = np.array(list_test)[:len(list_test)-1]

    #Calculo de la estimacion
    estimacion = 0
    for pos, elemento in enumerate(pesos):
        estimacion += elemento[0] * list_test[pos]
        
    #Verificacion de que devuelve un valor entre 0 y 5
    funciones.caracteristicaValida(estimacion)  #Usa asserts


