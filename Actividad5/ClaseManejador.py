# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:52:20 2022

@author: Emiliano
"""
from persona import Persona
class Manejador(object):
    indice=0
    __personas=[]
    def __init__(self):
        self.__personas=[]
    def agregarPaciente(self, persona):
        self.__personas.append(persona)
        
    def getListaPaciente(self):
        return self.__personas
    
    def deletePaciente(self, persona):
        indice=self.obtenerIndicePaciente(persona)
        self.__personas.pop(indice)
        
    def updatePaciente(self, persona):
        indice=self.obtenerIndicePaciente(persona)
        print(indice)
        for i in self.__personas:
            print(vars(i))
        self.__personas[indice-1]=persona
        
    def obtenerIndicePaciente(self, persona):
        bandera = False
        i=0
        while not bandera and i < len(self.__personas):
            if self.__personas[i].getNombre() == persona.getNombre():
                bandera=True
            else:
                i+=1
        if i <= len(self.__personas):
            print(i)
            return i
        else:
            print("no encotrado")
            return None

    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        personas=[Persona.ToJSON() for Persona in self.__personas]
        )
        return d
