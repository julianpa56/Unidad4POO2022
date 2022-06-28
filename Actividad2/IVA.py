from tkinter import *
import tkinter as tk


class Aplicacion(object):
    __ventana= None
    __precio=None


    def __init__(self) -> None:
        self.__ventana= tk.Tk()
        self.__ventana.title("Calculadora de IVA")
        self.__precio= StringVar()
        self.__totalIva= StringVar()
        self.__precioTotal= StringVar()
        self.__rbIva1= IntVar()

        opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
        labelTitulo= tk.Label(self.__ventana,text="Cálculo de IVA",bg='light blue').grid(row=0,column=0,columnspan=4,**opts)
        contenedor= tk.Frame(self.__ventana).grid(row=2,column=0,rowspan=6,columnspan=4,**opts)
        labelPrecio= tk.Label(contenedor,text="Precio sin IVA").grid(row=1,column=0,columnspan=1,**opts)
        
        self.entradaPrecio= tk.Entry(contenedor,textvariable=self.__precio,justify='right').grid(row=1,column=3,columnspan=1,**opts)
        
        radioB1= tk.Radiobutton(contenedor,text="IVA 21 %",value=1,variable=self.__rbIva1).grid(row=3,column=1,**opts)
        radioB2= tk.Radiobutton(contenedor,text="IVA 10.5 %",value=0,variable=self.__rbIva1).grid(row=4,column=1,**opts)
        # iva
        labelIva= tk.Label(contenedor,text="IVA").grid(row=5,column=1,**opts)
        totalIva= tk.Entry(contenedor,textvariable= self.__totalIva, justify='right').grid(row=5,column=2,**opts)
        # precio con iva
        labelPrecioTotal= tk.Label(contenedor,text="Precio con IVA").grid(row=6,column=1)
        precioTotal= tk.Entry(contenedor,textvariable= self.__precioTotal, justify='right').grid(row=6,column=2,**opts)
        # botones
        botonCalcular= tk.Button(contenedor,text="Calcular",command=self.calcular,bg='light green').grid(row=7,column=1,**opts)
        botonSalir= tk.Button(contenedor,text="Salir",command= self.__ventana.destroy,bg='red').grid(row=7,column=2,**opts) 



        self.__ventana.mainloop()

    def calcular(self):
        iva=0
        if int(self.__rbIva1.get())==1:
            iva= float(self.__precio.get())*0.21
        else:
            iva= float(self.__precio.get())*0.105
        resultado= float(self.__precio.get()) + iva
        self.__totalIva.set(iva)
        self.__precioTotal.set(resultado)