class Fecha():
    def __init__(self):
        super().__init__()
        self.__dia = 1
    
    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
        else:
            print("error")

    dia = property(getDia, setDia)  # using properties

mi_fecha = Fecha()
mi_fecha.setDia(33)
mi_fecha.setDia(28)
print(mi_fecha.getDia())

mi_fecha.dia = 10
print(mi_fecha.dia)