# -*- coding: utf-8 -*-
# Clase que almacena la información correspondiente a una serie

from source.caracteristicas import Caracteristicas

class Serie:
  def __init__(self, iden, titulo, director, duracion, lanzamiento):
    self.identificador = iden                             # Codigo para identificar de forma unica cada serie
    self.caracteristicas = Caracteristicas(0, 0, 0, 0, 0) # Caracteristicas de una serie, inicialmente los atributos son 0
    self.titulo = titulo
    self.director = director
    self.duracion = duracion
    self.lanzamiento = lanzamiento
    
  def getId(self):
    return self.identificador
  
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
    
  def setTitulo(self, titulo):
    self.titulo = titulo
    
  def setDirector(self, director):
    self.director = director
    
  def setDuracion(self, duracion):
    self.duracion = duracion
    
  def setLanzamiento(self, lanzamiento):
    self.lanzamiento = lanzamiento
