# -*- coding: utf-8 -*-
"""
Funciones Auxiliares
"""


def caracteristicaValida(carac):
        
        assert carac >= 0 , "La caracteristica tiene que ser mayor o igual que 0"
        assert carac <= 5 , "La caracteristica tiene que ser menor o igual que 5"

def estimarValoracion(caracteristicas):
    pesos = [0.4,0.11,0.07,0.16,0.26]

    valoracion = 0

    for valor, peso in zip(caracteristicas.values(), pesos):

            valoracion += valor * peso

    return valoracion