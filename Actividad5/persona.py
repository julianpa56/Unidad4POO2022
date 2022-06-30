# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:26:22 2022

@author: Emiliano
"""

class Persona():
    __nombre=""
    __apellido=""
    __telefono=""
    __altura:float
    __peso:float 
    
    def __init__(self,nombre,apellido,telefono,altura,peso):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__telefono=telefono
        self.__altura=float(altura)
        self.__peso=float(peso)
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getTelefono(self):
        return self.__telefono
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso
    def setPeso(self,peso):
        self.__peso=float(peso)
    def ToJSON(self):
        diccionario=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                apellido=self.__apellido,
                telefono=self.__telefono,
                altura=self.__altura,
                peso=self.__peso)
            )
        return diccionario
        
        
