
import pytest
from source.caracteristicas import Caracteristicas
from tests.funciones_tests import leerCSV, convertStringToFloatList
from source.funciones import estimarValoracion, caracteristicaValida

#Se asegura que la regresion lineal devuelve un valor entre 0 y 5
def test_regLinValorCorrecto():

    #Entrada de datos de test
    list_test = leerCSV("test_data.txt")
    list_test = convertStringToFloatList(list_test)[0]
    
    #Quito la valoración que ya tiene
    list_test = list_test[:len(list_test)-1]

    caracteristicas = Caracteristicas(list_test[0],\
        list_test[1],list_test[2],list_test[3],list_test[4])
    
    #Calculo de la estimacion
    estimacion = estimarValoracion(caracteristicas.getCaracteristicas())
        
    #Verificacion de que devuelve un valor entre 0 y 5
    caracteristicaValida(estimacion)  #Usa asserts
    
