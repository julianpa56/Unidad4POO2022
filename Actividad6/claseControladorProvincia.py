


from Clases import NuevaProvincia, VistaProvincia


class ControladorProvincias(object):

    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincias = list(repo.obtenerListaProvincias())
    # comandos de que se ejecutan a través de la vista
    def crearProvincia(self):
        nuevaProvincia = NuevaProvincia(self.vista).show()
        if nuevaProvincia:
            provincia = self.repo.agregarPovincia(nuevaProvincia)
            self.provincias.append(provincia)
            self.vista.agregarProvincia(provincia)
    def seleccionarProvincia(self, index):
        self.seleccion = index
        provincia = self.provincias[index]
        self.vista.verProvinciaEnForm(provincia)
    def modificarProvincia(self):
        if self.seleccion==-1:
            return
        rowid = self.provincias[self.seleccion].rowid
        detallesProvincia = self.vista.obtenerDetalles()
        detallesProvincia.rowid = rowid
        provincia = self.repo.modificarProvincia(detallesProvincia)
        self.provincias[self.seleccion] = provincia
        self.vista.modificarProvincia(provincia, self.seleccion)
        self.seleccion=-1
    def borrarProvincia(self):
        if self.seleccion==-1:
            return
        provincia = self.provincias[self.seleccion]
        self.repo.borrarProvincia(provincia)
        self.provincias.pop(self.seleccion)
        self.vista.borrarProvincia(self.seleccion)
        self.seleccion=-1
    def start(self):
        for prov in self.provincias:
            self.vista.agregarProvincia(prov)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.repo.grabarDatos()