from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter as tk

class Aplicacion(object):
    __ventana=None
    __peso=None
    __altura=None

    def __init__(self):
        self.__ventana= tk.Tk()
        self.__ventana.title("Calculadora de IMC")

        # --------- CREACION DE LOS LABEL, ENTRY Y DEMAS
        self.peso= StringVar()
        self.altura= StringVar()
        self.fuente = font.Font(weight='bold')
        label_altura=tk.Label(self.__ventana, text="Altura", bg="green")
        self.__altura=tk.Entry(self.__ventana,textvariable=self.altura ,justify='right')
        label_cm=tk.Label(self.__ventana,text="cm",bg="grey")
        label_peso=tk.Label(self.__ventana,text="Peso",bg="green")
        self.__peso=tk.Entry(self.__ventana,textvariable=self.peso, justify='right')
        self.__mensaje = StringVar()
        self.__diagnostico= StringVar()
        label_kg=tk.Label(self.__ventana,text="kg",bg="grey")
        botonCalcular=tk.Button(self.__ventana,text="Calcular",command=self.calcular)
        botonLimpiar=tk.Button(self.__ventana,text="Limpiar",command=self.limpiar)
        botonSalir=tk.Button(self.__ventana,text="Salir",command=self.__ventana.destroy)
        self.resultado = tk.Label(self.__ventana, textvariable=self.__mensaje, font=self.fuente, foreground='blue')
        self.diagnostico= tk.Label(self.__ventana,textvariable=self.__diagnostico, font=self.fuente, foreground='blue')
        opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }       
            #  ---------- POSICIONAMIENTO DE LOS ELEMENTOS
        label_altura.grid(row=0, column=0, **opts)
        self.__altura.grid(row=0,column=1,columnspan=4,**opts)
        label_cm.grid(row=0,column=5,**opts)
        label_peso.grid(row=1,column=0,**opts)
        self.__peso.grid(row=1,column=1,columnspan=4,**opts)
        label_kg.grid(row=1,column=5,**opts)
        botonCalcular.grid(row=2,column=0,columnspan=2,**opts)
        botonLimpiar.grid(row=2,column=2,columnspan=2,**opts)
        botonSalir.grid(row=2,column=4,columnspan=2,**opts)
        self.resultado.grid(row=3,column=1,columnspan=4,**opts)
        self.diagnostico.grid(row=4,column=1,columnspan=4,**opts)
        self.__ventana.mainloop()
        #  --------------- FUNCIONES -------------------- 
    def calcular(self):
        try:
            if int(self.__altura.get())>0:
                try:
                    peso= float(self.__peso.get())
                    altura= float(self.__altura.get())
                    imc = peso / (altura/100)**2
                    self.resultado.configure(foreground='green')
                    self.__mensaje.set("Tu IMC es {} Kg/m2".format(round(imc,2)))
                    if imc < 18.5:
                        self.__diagnostico.set("Peso inferior al normal")
                    elif imc < 24.9:
                        self.__diagnostico.set("Peso normal")
                    elif imc < 29.9:
                        self.__diagnostico.set("Peso superior al normal")
                    else:
                        self.__diagnostico.set("Obesidad")

                except ValueError:
                    self.resultado.configure(foreground='red')
                    self.__mensaje.set("Error")
                    self.diagnostico.configure(foreground='red')
                    self.__diagnostico.set("Ingrese datos validos")
            else:
                self.resultado.configure(foreground='red')
                self.__mensaje.set("Datos invalidos")
                self.diagnostico.configure(foreground='red')
                self.__diagnostico.set("La altura debe ser mayor a 0")
        except ValueError:
            self.resultado.configure(foreground='red')
            self.__mensaje.set("Error")
            self.diagnostico.configure(foreground='red')
            self.__diagnostico.set("Ingrese datos validos")

    def limpiar(self):
        self.peso.set('')
        self.altura.set('')
        self.__mensaje.set('')
        self.__diagnostico.set('')

def testAPP():
    mi_app = Aplicacion()
    
if __name__ == '__main__':
    testAPP()