# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:43:19 2022

@author: Emiliano
"""
import json
from pathlib import Path
from ClaseManejador import Manejador
from persona import Persona
class ObjectEncoder(object):
    __pathArchivo=None
    def __init__(self, pathArchivo):
        self.__pathArchivo=pathArchivo
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                personas=d['personas']
                manejador=class_()
                for i in range(len(personas)):
                    dPersonas=personas[i]
                    class_name=dPersonas.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPersonas['__atributos__']
                    unContacto=class_(**atributos)
                    manejador.agregarPaciente(unContacto)
        return manejador
    
    def guardarJSONArchivo(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
        return diccionario
