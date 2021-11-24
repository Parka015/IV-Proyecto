# -*- coding: utf-8 -*-
# Clase que almacena la información correspondiente a una serie

Class serie:
  def __init__(self, iden, val):
    self.identificador = iden   # Codigo para identificar de forma unica cada serie
    self.valoracion = val       # Valor real entre 0.0 y 5.0 que determina la puntiación de una serie
    
  # GETTERS  
    
  def getId(self):
    return self.identificador
  
  def getValoracion(self):
    return self.valoracion	


