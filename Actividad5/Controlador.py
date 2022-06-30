# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:23:23 2022

@author: Emiliano
"""

from ventana import ContactsView, NewContact
from ClaseManejador import Manejador
from persona import Persona
class ControladorPacientes(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.paciente = list(repo.obtenerListaPaciente())
    # comandos que se ejecutan a través de la vista
    def crearPaciente(self):
        nuevoPacientes = NewContact(self.vista).show()
        if nuevoPacientes:
            paciente = self.repo.agregarPaciente(nuevoPacientes)
            self.paciente.append(paciente)
            self.vista.agregarPaciente(paciente)
    def seleccionarPaciente(self, index):
        self.seleccion = index
        paciente = self.paciente[index]
        self.vista.verPacienteEnForm(paciente)
        
    def CalcularINCdePaciente(self):
        if self.seleccion==-1:
            return
        rowid = self.paciente[self.seleccion]
        calculo=rowid.getPeso()/rowid.getAltura()**2
        if calculo<18.5:
            message="Peso inferior al normal"
        else:
            if calculo>18.5 and calculo<25:
                message="Peso normal"
            else:
                if calculo>=25.0 and calculo<30:
                    message="Peso superior normal"
                else:
                    message="Obesidad"
        self.vista.verINCPaciente(calculo,message)
    
    def modificarPaciente(self):
        if self.seleccion==-1:
            return
        rowid = self.paciente[self.seleccion]
        detallesPaciente = self.vista.obtenerDetalles()
        nuevo=Persona(detallesPaciente.getApellido(), detallesPaciente.getNombre(), detallesPaciente.getTelefono(), detallesPaciente.getAltura(), detallesPaciente.getPeso())
        detallesPaciente = rowid
        paciente = self.repo.modificarPaciente(nuevo)
        self.paciente[self.seleccion] = paciente
        self.vista.modificarPaciente(paciente, self.seleccion)
        self.seleccion=-1
    def borrarPaciente(self):
        if self.seleccion==-1:
            return
        paciente = self.paciente[self.seleccion]
        self.repo.borrarPaciente(paciente)
        self.paciente.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion=-1
    def start(self):
        for c in self.paciente:
            self.vista.agregarPaciente(c)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.repo.grabarDatos()
    