# Propiedades

class Empleado:
    def __init__(self,nombre,salario):
        self.__nombre = nombre
        self.__salario = salario

    def getnombre(self):
        return self.__nombre
    def getsalario(self):
        return self.__salario
    def setnombre(self, nombre): # propiedad
        self.__nombre = nombre
    def setsalario(self, salario):
        self.__salario = salario

empleado = Empleado('victor',2000)
print(empleado.getnombre(),',',empleado.getsalario())