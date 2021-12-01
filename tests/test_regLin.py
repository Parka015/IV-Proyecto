

import pytest
from tests.funciones_tests import leerCSV, convertStringToFloatList
from source.funciones import regLin, caracteristicaValida
import numpy as np

#Se asegura que la regresion lineal devuelve un valor entre 0 y 5
def test_regLinValorCorrecto():
    
    #Entrada de datos de training
    list_train = leerCSV("tests/train_data.txt")
    list_train = convertStringToFloatList(list_train)
    
    #Entrenamiento
    pesos = regLin(list_train)
    
    #Entrada de datos de test
    list_test = leerCSV("tests/test_data.txt")
    list_test = convertStringToFloatList(list_test)[0]
    
    list_test = np.array(list_test)[:len(list_test)-1]

    #Calculo de la estimacion
    estimacion = 0
    for pos, elemento in enumerate(pesos):
        estimacion += elemento[0] * list_test[pos]
        
    #Verificacion de que devuelve un valor entre 0 y 5
    caracteristicaValida(estimacion)  #Usa asserts


