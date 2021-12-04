# -*- coding: utf-8 -*-

from source.funciones import caracteristicaValida

class Caracteristicas:
    

    def __init__(self,accion,terror,romance,comedia,efectos_especiales):
        
        #Todas las características serán valores reales del [0.0 - 5.0]
        caracteristicaValida(accion)    #En caso de no ser válida genera un error
        caracteristicaValida(terror)
        caracteristicaValida(romance)
        caracteristicaValida(comedia)
        caracteristicaValida(efectos_especiales)
        
        self.atributos={}
        
        self.atributos["accion"] = accion
        self.atributos["terror"] = terror
        self.atributos["romance"] = romance
        self.atributos["comedia"] = comedia
        self.atributos["efectos_especiales"] = efectos_especiales
        
        
    ####  Gets  ####
        
    def getCaracteristicas(self):
        return self.atributos 
    

    ####  Sets  ####
    
    def setAccion(self, accion,terror,romance,comedia,efectos_especiales, valoracion):
        caracteristicaValida(accion)    #En caso de no ser válida genera un error
        self.atributos["accion"] = accion
 
    def setTerror(self, terror):
        caracteristicaValida(terror)
        self.atributos["terror"] = terror
    
    def setRomance(self, romance):
        caracteristicaValida(romance)
        self.atributos["romance"] = romance

    def setComedia(self, comedia):
        caracteristicaValida(comedia)
        self.atributos["comedia"] = comedia
    
    def setEfectos_especiales(self, efectos_especiales):
        caracteristicaValida(efectos_especiales)
        self.atributos["efectos_especiales"] = efectos_especiales
    
    def setValoracion(self, valoracion):
        caracteristicaValida(valoracion)
        self.atributos["valoracion"] = valoracion
        

                 
    
    

        
    