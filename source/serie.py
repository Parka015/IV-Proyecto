# -*- coding: utf-8 -*-
# Clase que almacena la información correspondiente a una serie

import KNN

Class serie:
  def __init__(self, iden):
    self.identificador = iden   # Codigo para identificar de forma unica cada serie
    self.prediccion_valoracion = -1 # Éxito estimado de una serie. Inicialmente nulo
    
  ### Gets ### 
    
  def getId(self):
    return self.identificador
  
  def getPrediccion(self):
    return self.prediccion_valoracion
  
  ### Sets ### 

  def setId(self, id):
    self.identificador = id
    
  def setPrediccion(self, prediccion):
    self.prediccion_valoracion = prediccion
    
