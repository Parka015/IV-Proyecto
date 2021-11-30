# -*- coding: utf-8 -*-

from funciones import caracteristicaValida

class Caracteristicas:
    

    def __init__(self, genero, anio, duracion, pais, direccion, sinopsis):
        
        #Todos los generos serán valores reales del [0.0 - 5.0]
        self.genero = caracteristicaValida(genero)
        self.anio = anio
        self.duracion = duracion
        self.pais = pais
        self.direccion = direccion
        self.sinopsis = sinopsis
        
    ####  Gets  ####
        
    def getGenero(self):
        gen = ""
        
        if self.genero == 1.0
            gen = "Accion"
           
        if self.genero == 2.0
            gen = "Terror"
        
        if self.genero == 3.0
            gen = "Romance"
           
        if self.genero == 4.0
            gen = "Efectos Especiales"
            
        if self.genero == 5.0
            gen = "Suspense"
           
        return gen
    
    def getAnio(self):
        return self.anio
    
    def getDuracion(self):
        return self.duracion
    
    def getPais(self):
        return self.pais
    
    def getDireccion(self):
        return self.direccion
    
    def getSinopsis(self):
        return self.sinopsis
    

    
    ####  Sets  ####
    
    def setGenero(self, genero):
        self.genero = caracteristicaValida(genero)
    
    def setAnio(self, anio):
        self.anio = anio
        
    def setDuracion(self, duracion):
        self.duracion = duracion
        
    def setPais(self, pais):
        self.pais = pais
        
    def setDireccion(self, direccion):
        self.direccion = direccion
        
    def setSinopsis(self, sinopsis):
        self.sinopsis = sinopsis

