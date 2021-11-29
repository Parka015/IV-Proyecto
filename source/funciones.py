# -*- coding: utf-8 -*-
"""
Funciones Auxiliares
"""

import numpy as np

def caracteristicaValida(carac):
        
        assert carac > 0 , "La caracteristica tiene que ser mayor o igual que 0"
        assert carac < 5 , "La caracteristica tiene que ser menor o igual que 5"

def regLin(matriz):
    matriz = np.array(matriz)

    x = matriz[:,:len(matriz[0])-1]

    y = matriz[:,len(matriz[0])-1:]

    pseudoinversa = np.linalg.pinv(x).dot(y)

    return pseudoinversa