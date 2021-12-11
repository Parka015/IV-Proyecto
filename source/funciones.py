# -*- coding: utf-8 -*-
"""
Funciones Auxiliares
"""


def caracteristicaValida(carac):
        
        assert carac >= 0 , "La caracteristica tiene que ser mayor o igual que 0"
        assert carac <= 5 , "La caracteristica tiene que ser menor o igual que 5"

#Calcula la distancia euclídea de dos listas
#Ambas listas deben ser del mismo tamaño
def distancia(lista1, lista2):
    cuadrados = [(l1 - l2)**2 for l1, l2 in zip(lista1, lista2)]
    return sum(cuadrados)**0.5
    