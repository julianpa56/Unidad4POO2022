

class Provincia(object):
    __nombre= None
    __capital= None
    __cantidadHabitantes= None
    __cantidadDepartamentos= None

    def __init__(self,nom,cap,cantH,cantD):
        self.__nombre= self.requerido(nom,"Nombre es requerido")
        self.__capital= self.requerido(cap,"Capital es requerida")
        self.__cantidadHabitantes= self.requerido(cantH,"Cantidad de habitantes es requerido")
        self.__cantidadDepartamentos= self.requerido(cantD,"Cantidad de departamentos es requerido")
        
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def getNombre(self):
        return self.__nombre
    
    def getCapital(self):
        return self.__capital

    def getCantidadH(self):
        return self.__cantidadHabitantes

    def getCantidadD(self):
        return self.__cantidadDepartamentos

    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                                nombre=self.__nombre,
                                capital=self.__capital,
                                cantidadHabitantes=self.__cantidadHabitantes,
                                cantidadDepartamentos=self.__cantidadDepartamentos
                            )
        )
        return d