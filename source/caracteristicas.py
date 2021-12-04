# -*- coding: utf-8 -*-

from funciones import caracteristicaValida

class Caracteristicas:
    

    def __init__(self,accion,terror,romance,comedia,efectos_especiales, valoracion):
        
        #Todas las características serán valores reales del [0.0 - 5.0]
        caracteristicaValida(accion)    #En caso de no ser válida genera un error
        caracteristicaValida(terror)
        caracteristicaValida(romance)
        caracteristicaValida(comedia)
        caracteristicaValida(efectos_especiales)
        caracteristicaValida(valoracion)

        self.atributos["accion"] = accion
        self.atributos["terror"] = terror
        self.atributos["romance"] = romance
        self.atributos["comedia"] = comedia
        self.atributos["efectos_especiales"] = efectos_especiales
        self.atributos["valoracion"] = valoracion
        
        
    ####  Gets  ####
        
    def getAtributos(self):
        return self.atributos 
    

    ####  Sets  ####
    
    def setAtributos(self, accion,terror,romance,comedia,efectos_especiales, valoracion):
        
        caracteristicaValida(accion)    #En caso de no ser válida genera un error
        caracteristicaValida(terror)
        caracteristicaValida(romance)
        caracteristicaValida(comedia)
        caracteristicaValida(efectos_especiales)
        caracteristicaValida(valoracion)

        self.atributos["accion"] = accion
        self.atributos["terror"] = terror
        self.atributos["romance"] = romance
        self.atributos["comedia"] = comedia
        self.atributos["efectos_especiales"] = efectos_especiales
        self.atributos["valoracion"] = valoracion

        

                 
    
    

        
    