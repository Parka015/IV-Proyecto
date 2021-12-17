# -*- coding: utf-8 -*-

from funciones import caracteristicaValida

class Caracteristicas:
    
    def __init__(self,accion,terror,romance,comedia,efectos_especiales, valoracion):
        #Todas las características serán valores reales del [0.0 - 5.0]
        
        self.accion = caracteristicaValida(accion)
        self.terror = caracteristicaValida(terror)
        self.romance = caracteristicaValida(romance)
        self.efectos_especiales = caracteristicaValida(efectos_especiales)
        self.valoracion = caracteristicaValida(valoracion)
        
        
    ####  Gets  ####
        
    def getAccion(self):
        return self.accion 

    def getTerror(self):
        return self.terror 

    def getRomance(self):
        return self.romance
    
     def getEfectos_especiales(self):
        return self.efectos_especiales
    
     def getValoracion(self):
        return self.valoracion    
    
    ####  Sets  ####
    
    def setAccion(self, accion):
        self.accion = caracteristicaValida(accion)
        
    def setTerror(self, terror):
        self.terror = caracteristicaValida(terror)

    def setRomance(self, romance):
        self.romance = caracteristicaValida(romance)
        
    def setEfectos_especiales(self, efectos_especiales):
        self.efectos_especiales = caracteristicaValida(efectos_especiales)
        
    def setValoracion(self, valoracion):
        self.valoracion = caracteristicaValida(valoracion)
