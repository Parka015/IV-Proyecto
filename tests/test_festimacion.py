
import pytest
from source.caracteristicas import Caracteristicas
from tests.funciones_tests import leerCSV, convertStringToFloatList
from source.funciones import estimarValoracion, caracteristicaValida
from source.KNN import KNN

#Comprueba que se cree correctamente un objeto tipo Caracteristicas
def test_creacionCaracteristica():

    dato = leerCSV("tests/test_data.txt")
    dato = convertStringToFloatList(dato)[0]

    caracteristicas = Caracteristicas(dato[0],\
        dato[1],dato[2],dato[3],dato[4])
        
    assert len(caracteristicas.getCaracteristicas()) == 5
    

#Comprueba que el modelo se entrene
def test_modeloEntrenado():
    
    lista = leerCSV("tests/train_data.txt")
    lista = convertStringToFloatList(lista)
    
    modelo = KNN()
    modelo.fit(lista)
    
    assert len(modelo.getData()) > 0


#Se asegura que el KNN devuelve un valor entre 0 y 5
def test_estimacionKNNCorrecta():
    
    #Entrada de datos de training
    list_train = leerCSV("tests/train_data.txt")
    list_train = convertStringToFloatList(list_train)

    #Entrada de datos de test
    list_test = leerCSV("tests/test_data.txt")
    list_test = convertStringToFloatList(list_test)[0]
    
    #Quito la valoración que ya tiene
    list_test = list_test[:len(list_test)-1]

    caracteristicas = Caracteristicas(list_test[0],\
        list_test[1],list_test[2],list_test[3],list_test[4])
    
    #Entrenamos el modelo
    modelo = KNN()
    modelo.fit(list_train)

    #Calculo de la estimacion
    estimacion = modelo.predict(list(caracteristicas.getCaracteristicas().values()) , 3 )
        
    #Verificacion de que devuelve un valor entre 0 y 5
    caracteristicaValida(estimacion)  