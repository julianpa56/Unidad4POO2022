# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 23:07:47 2022

@author: Emiliano
"""

import tkinter as tk
from tkinter import messagebox
from persona import Persona

class ContactList(tk.Frame):
    
    def __init__(self, master, **kwargs):
        
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
    def insertar(self, paciente, index=tk.END):
        
        text = "{}, {}".format(paciente.getApellido(), paciente.getNombre())
        self.lb.insert(index, text)
        
    def borrar(self, index):
        
        self.lb.delete(index, index)
        
    def modificar(self, paciente, index):
        
        self.borrar(index)
        self.insertar(paciente, index)
        
    def bind_doble_click(self, callback):
        
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)
    
class ContactForm(tk.LabelFrame):
    fields = ("Apellido", "Nombre", "Teléfono", "Altura", "Peso")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Paciente", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry
    
    def mostrarEstadoPacienteEnFormulario(self, paciente):
        # a partir de un paciente, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (paciente.getApellido(), paciente.getNombre(), paciente.getTelefono(),paciente.getAltura(),paciente.getPeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearPacienteDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear un nuevo paciente
        values = [e.get() for e in self.entries]
        paciente=None
        try:
            paciente = Persona(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return paciente
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
        
    
class NewContact(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.paciente = None
        self.form = ContactForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    def confirmar(self):
        self.paciente = self.form.crearPacienteDesdeFormulario()
        if self.paciente:
            self.destroy()
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.paciente
        
#modifiar y agregar inc
class UpdateContactForm(ContactForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_inc = tk.Button(self,text="Ver INC")
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_inc.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
    def bind_save(self, callback):
        self.btn_save.config(command=callback)
    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)
    def CalculoIMC(self,callback):
        self.btn_inc.config(command=callback)
        

class ContactsView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Paciente")
        self.list = ContactList(self, height=15)
        self.form = UpdateContactForm(self)
        self.btn_new = tk.Button(self, text="Agregar paciente")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_doble_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.CalculoIMC(ctrl.CalcularINCdePaciente)
    def agregarPaciente(self, paciente):
        self.list.insertar(paciente)
    def modificarPaciente(self, paciente, index):
        self.list.modificar(paciente, index)
    def borrarPaciente(self, index):
        self.form.limpiar()
        self.list.borrar(index)
    #obtiene los valores del formulario y crea un nuevo Paciente
    def obtenerDetalles(self):
        return self.form.crearPacienteDesdeFormulario()
    #Ver estado de Paciente en formulario de Pacientes
    def verPacienteEnForm(self, paciente):
        self.form.mostrarEstadoPacienteEnFormulario(paciente)
    def verINCPaciente(self,datos,texto):
        self.INC=tk.StringVar()
        self.TEXT=tk.StringVar()
        self.INC.set(datos)
        self.TEXT.set(texto)
        self.top=tk.Toplevel()
        self.top.title("INC")
        self.labelINC=tk.Label(self.top,text="INC").grid(row=0,column=0)
        self.labelComposicion=tk.Label(self.top,text="Composición Corporal").grid(row=1,column=0)
        self.entryInc=tk.Entry(self.top,textvariable=self.INC).grid(row=0,column=1)
        self.entryTexto=tk.Entry(self.top,textvariable=self.TEXT).grid(row=1,column=1)
        self.btnVolver=tk.Button(self.top,text="Volver",command=self.top.destroy).grid(row=2,column=1)
        
        