
from source.caracteristicas import Caracteristicas
from source.funciones import distancia

class KNN:

    def __init__(self):
        
        self.data = []
    
    #Funcion para entrenar el modelo
    def fit(self,labeled_data : list):

        self.data = labeled_data



    def predict(self, carac : Caracteristicas, k : int):

        #Se debe previamente haber entrenado el algoritmo
        assert len(self.data) > 0 , "El modelo debe ser entrenado primero, use el método fit"

        # Calculamos las distancias del dato "carac" con los datos de entrenamiento
        distancias = []

        for d in self.data:
            distancias.append( distancia(d, carac) )

        # Ordenaremos los datos de entrenamiento en funcion de su cercania al dato "carac"
        distancias, ordered_data = zip(*sorted(zip(distancias, self.data)))
        
        estimacion = []
        print("Ordered training data:\n",ordered_data)
        for vecino in range(k):
            print(f"Etiqueta {vecino}: ",ordered_data[vecino][len(ordered_data[vecino])-1])
            estimacion.append(ordered_data[vecino][len(ordered_data[vecino])-1])

        estimacion = sum(estimacion)/len(estimacion)
        print("Estimacion: ", estimacion)
        return estimacion
	
    def getData(self):
        return self.data


