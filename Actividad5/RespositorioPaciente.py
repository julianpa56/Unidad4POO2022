# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 23:16:17 2022

@author: Emiliano
"""
from persona import Persona
from ObjectEncoder import ObjectEncoder
from ClaseManejador import Manejador
class RespositorioPaciente(object):
    __paci=None
    __manejador=None
    def __init__(self, conn):
        self.__paci = conn
        diccionario=self.__paci.leerJSONArchivo()
        self.__manejador=self.__paci.decodificarDiccionario(diccionario)
    def obtenerListaPaciente(self):
        return self.__manejador.getListaPaciente()
    def agregarPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente
    def modificarPaciente(self, paciente):
        print(vars(paciente),"dentro de paciente")
        self.__manejador.updatePaciente(paciente)
        return paciente
    def borrarPaciente(self, paciente):
        self.__manejador.deletePaciente(paciente)
    def grabarDatos(self):
        self.__paci.guardarJSONArchivo(self.__manejador.toJSON())
