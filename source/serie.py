# -*- coding: utf-8 -*-
# Clase que almacena la información correspondiente a una serie

class Serie:
  def __init__(self, iden, titulo, director, duracion, lanzamiento):
    self.identificador = iden   # Codigo para identificar de forma unica cada serie
    self.prediccion = None # Éxito estimado de una serie. Inicialmente nulo
    self.titulo = titulo
    self.director = director
    self.duracion = duracion
    self.lanzamiento = lanzamiento
    
  def getId(self):
    return self.identificador
  
  def getPrediccion(self):
    return self.prediccion
  
  def getTitulo(self):
    return self.titulo
  
  def getDirector(self):
    return self.director
  
  def getDuracion(self):
    return self.duracion
  
  def getLanzamiento(self):
    return self.lanzamiento

  def setId(self, id):
    self.identificador = id
    
  def setPrediccion(self, prediccion):
    self.prediccion = prediccion
    
  def setTitulo(self, titulo):
    self.titulo = titulo
    
  def setDirector(self, director):
    self.director = director
    
  def setDuracion(self, duracion):
    self.duracion = duracion
    
  def setLanzamiento(self, lanzamiento):
    self.lanzamiento = lanzamiento
