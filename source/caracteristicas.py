# -*- coding: utf-8 -*-

from funciones import caracteristicaValida

class Caracteristicas:
    

    def __init__(self,accion,terror,romance,comedia,efectos_especiales, valoracion):
        
        #Todas las características serán valores reales del [0.0 - 5.0]
        caracteristicaValida(accion)    #En caso de no ser válida genera un error
        caracteristicaValida(terror)
        caracteristicaValida(romance)
        caracteristicaValida(efectos_especiales)
        caracteristicaValida(valoracion)

        self.accion = accion
        self.terror = terror
        self.romance =romance
        self.efectos_especiales = efectos_especiales
        self.valoracion = valoracion
        
        
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
        caracteristicaValida(accion)    #En caso de no ser válida genera un error
        self.accion = accion
    
    def setTerror(self, terror):
        caracteristicaValida(terror)
        self.terror = terror
    
    def setRomance(self, romance):
        caracteristicaValida(romance)
        self.romance = romance
    
    def setEfectos_especiales(self, efectos_especiales):
        caracteristicaValida(efectos_especiales)
        self.efectos_especiales = efectos_especiales
    
    def setValoracion(self, valoracion):
        caracteristicaValida(valoracion)
        self.valoracion = valoracion
        

                 
    
    

        
    