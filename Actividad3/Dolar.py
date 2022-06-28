from tkinter import *
import tkinter as tk
import json
from urllib.request import urlopen


class Aplicacion(object):
    __ventana= None
    __resultadoApi= None
    __entradaDolar=None


    def __init__(self) -> None:
        self.__ventana= tk.Tk()
        self.__ventana.title("Conversor de moneda")
        # -----variables a usar de entrada
        self.__entradaDolar= StringVar()
        self.__entradaDolar.trace("w",self.resultado)
        self.__resultadoConversion= StringVar()
        # -----
        opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
        entradaDolar= tk.Entry(self.__ventana,textvariable=self.__entradaDolar).grid(row=0, column=1,**opts)
        labelEntradaDolar= tk.Label(self.__ventana, text="USD", justify="center").grid(row=0,column=2,**opts)
        labelEquivalente= tk.Label(self.__ventana, text="es equivalente a ", justify="center").grid(row=1,column=0,**opts)
        labelCantidadEquivalente= tk.Label(self.__ventana,textvariable=self.__resultadoConversion, justify="center").grid(row=1,column=1,**opts)
        botonSalir= tk.Button(self.__ventana,text="Salir",command=self.__ventana.destroy,bg='red').grid(row=2,column=2,**opts)

        self.__ventana.mainloop()


    def resultado(self,*args):
        if self.__entradaDolar.get() != '':
            aux= str(self.__entradaDolar.get())
            aux= aux.replace(",",".")
            aux= float(aux)
            dolarOficial= self.datosDolar()
            aux2= dolarOficial* aux
            self.__resultadoConversion.set(aux2)


    def datosDolar(self):
        url_template = 'https://www.dolarsi.com/api/api.php?type=dolar'
        response = urlopen(url_template)
        resultado = json.loads(response.read().decode())
        dolarOficial= str(resultado[0]['casa']['compra']) 
        dolarOficial= dolarOficial.replace(",",".")
        dolarOficial= float(dolarOficial)
        return dolarOficial