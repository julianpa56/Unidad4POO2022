import tkinter as tk
from tkinter import messagebox
import json
from urllib.request import urlopen

from claseProvincia import Provincia


class ListaProvincias(tk.Frame):
    def __init__(self,master,**styles): # ------ falta agregar **styles
        super().__init__(master)
        self.lb = tk.Listbox(self,**styles) # ------ falta agregar **styles
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, provincia:Provincia, index=tk.END):
        text = "{}".format(provincia.getNombre())
        self.lb.insert(index, text)
    
    def borrar(self, index):
        self.lb.delete(index, index)

    def modificar(self, contact, index):
        self.borrar(index)
        self.insertar(contact, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)


class FormularioProvincias(tk.LabelFrame):
    listaLabels=("Nombre","Capital","Cantidad de habitantes","Cantidad de departamentos","Temperatura","Sensacion Termica","Humedad")

    def __init__(self,master,**styles): # ------ falta agregar **styles
        super().__init__(master, text="Datos Provincia", padx=10, pady=10,**styles) # ------ falta agregar **styles
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.listaLabels)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, provincia:Provincia):
        values = (provincia.getNombre(), provincia.getCapital(),
                provincia.getCantidadH(), provincia.getCantidadD())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearProvinciaDesdeFormulario(self):
        values = [e.get() for e in self.entries]
        provincia=None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class NuevaProvincia(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.form = FormularioProvincias(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    def confirmar(self):
        self.provincia = self.form.crearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia

class ActualizarProvincia(FormularioProvincias):
    def __init__(self, master,**styles): #------------- falta **styles
        super().__init__(master,**styles) #------------- falta **styles
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
    def bind_save(self, callback):
        self.btn_save.config(command=callback)
    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)


class VistaProvincia:
    __ventana= None

    def __init__(self):
        self.__ventana= tk.Tk()
        self.__ventana.title("Aplicación del clíma")
        self.listaProvincias = ListaProvincias(self.__ventana)
        self.updateProvinciaForm= ActualizarProvincia(self.__ventana)
        self.btn_new = tk.Button(self.__ventana, text="Agregar Provincia")        
        self.listaProvincias.pack(side=tk.LEFT, padx=10, pady=10)
        self.updateProvinciaForm.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
        self.btn_new.config(command=ctrl.crearProvincia)
        self.listaProvincias.bind_doble_click(ctrl.seleccionarProvincia)
        self.updateProvinciaForm.bind_save(ctrl.modificarProvincia)
        self.updateProvinciaForm.bind_delete(ctrl.borrarProvincia)
    def agregarProvincia(self, provincia):
        self.listaProvincias.insertar(provincia)
    def modificarProvincia(self, provincia, index):
        self.listaProvincias.modificar(provincia, index)
    def borrarProvincia(self, index):
        self.updateProvinciaForm.limpiar()
        self.listaProvincias.borrar(index)
    def obtenerDetalles(self):
        return self.updateProvinciaForm.crearProvinciaDesdeFormulario()
    def verProvinciaEnForm(self, provincia):
        self.updateProvinciaForm.mostrarEstadoProvinciaEnFormulario(provincia)

        self.__ventana.mainloop()

    def datosProvincia(self):
        base_template = 'https://api.openweathermap.org/data/2.5/weather?q=*provincia*&appid=f708bb9e0d23c03bfda6a7a284db5033'
        url_template= base_template.replace("*provincia*","variable de provincia")
        response = urlopen(url_template)
        resultado = json.loads(response.read().decode())
        temperatura= str(resultado[0]["main"]["temp"])
        sensacionTermica= str(resultado[0]["main"]["feels_like"])
        humedad= str(resultado[0]["main"]["humidity"])


        # °C = K − 273.15