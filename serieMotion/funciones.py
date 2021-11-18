# -*- coding: utf-8 -*-
"""
Funciones Auxiliares
"""

def caracteristicaValida(carac):
        
        if (carac < 0):
            
            carac = 0.0
            
        elif (carac > 5):
            
            carac = 5.0
        
        return carac