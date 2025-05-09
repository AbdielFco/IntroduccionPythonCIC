# Polimorfismo, es la capacidad que tienen los objetos para usar...
# ... un atributo con mismo nombre pero diferente valor

class Auto:
    rueda = 4
    def desplazamiento(self):
        print(f'el auto se desplaza a 4 ruedas')

class Moto:
    rueda = 2
    def desplazamiento(self):
        print(f'el auto se desplaza a 2 ruedas')


# Ej 2
class Animales:
    def __init__(self,nombre):
        self.nombre = nombre
    def tipo_animal(self):
        pass
class Leon(Animales):
    def tipo_animal(self):
        print('animal salvaje')

class Perro(Animales):
    def tipo_animal(self):
        print('animal domestico')

nuevo_animal = Leon('SIMBA')
nuevo_animal.tipo_animal()

nuevo_animal = Perro('BLACKY')
nuevo_animal.tipo_animal()
