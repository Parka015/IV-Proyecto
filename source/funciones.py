# -*- coding: utf-8 -*-
"""
Funciones Auxiliares
"""

import numpy as np

def caracteristicaValida(carac):
        
        assert carac < 0 , "La caracteristica tiene que ser mayor o igual que 0"
        assert carac > 5 , "La caracteristica tiene que ser menor o igual que 5"

def regLin(caracteristicas,etiqueta):
    x = np.array(caracteristicas)
    y = np.array(etiqueta)
    
    pseudoinversa = np.linalg.pinv(x).dot(y)
    pseudoinversa = pseudoinversa[:,np.newaxis]

    return pseudoinversa