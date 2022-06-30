from claseProvincia import Provincia
from claseObjectEncoder import ObjectEncoder
from claseManejadorProvincia import ManejadorProvincia
class RespositorioProvincias(object):
    __conn=None
    __manejador=None
    def __init__(self, conn):
        self.__conn = conn
        diccionario=self.__conn.leerJSONArchivo()
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)
    def to_values(self, provincia:Provincia):
        return provincia.getNombre(), provincia.getCapital(), provincia.getCantidadH(), provincia.getCantidadD()
    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()
    def agregarProvincia(self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia
    def modificarProvincia(self, provincia):
        self.__manejador.updateProvincia(provincia)
        return provincia
    def borrarProvincia(self, provincia):
        self.__manejador.deleteProvincia(provincia)
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())