# -*- coding: utf-8 -*-
# Clase que almacena la información correspondiente a una serie

Class serie:
  def __init__(self, iden):
    self.identificador = iden   # Codigo para identificar de forma unica cada serie
    
  ### Gets ### 
    
  def getId(self):
    return self.identificador
  
  ### Sets ### 

  def setId(self, id):
    self.identificador = id
    
    
