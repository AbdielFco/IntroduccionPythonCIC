# f-strings

xnombre = 'Victor'
xedad = 25
print(f"hola soy {xnombre} y mi edad es {xedad} años.")

class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def __str__(self):
        return f"hola que tal soy {self.nombre} {self.apellido} y tengo {self.edad} años."
nuevo_estudiante = Estudiante('juanito','alimaña',23)
print(f"{nuevo_estudiante}")
