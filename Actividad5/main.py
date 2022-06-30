# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:59:13 2022

@author: Emiliano
"""
from RespositorioPaciente import RespositorioPaciente
from ventana import ContactsView
from Controlador import ControladorPacientes
from ObjectEncoder import ObjectEncoder
def main():
    conn=ObjectEncoder('pacientes.json')
    repo=RespositorioPaciente(conn)
    vista=ContactsView()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
if __name__ == "__main__":
    main()