# Clases, una clase es como una plantilla para crear un objeto.
# Instancia, se crea usando el constructor de una clase...
# ... una vez que el objeto es creado se conoce como instancia de esa clase.
# Tipos de metodos: Estaticos, Clase, Instancia.
# Metodo clase, puede ser llamado sin crear una instancia.
# Metodo estatico, // además no tiene acceso al exterior, no puede acceder a otros atributos.

import math

# Clase
class Pastel:
    def __init__(self,ingredientes):
        self.ingredientes = ingredientes

    def __repr__(self):
        return f'pastel({self.ingredientes !r})'

    @classmethod
    def Pastel_chocolate(cls):
        return cls(['harina','leche','chocolate'])
    
    @classmethod
    def Pastel_vainilla(cls):
        return cls(['harina','leche','vainilla'])

print(Pastel.Pastel_chocolate())

# Estatico
class Bizcocho:
    def __init__(self,ingredientes,tamano):
        self.ingredientes = ingredientes
        self.tamano = tamano

    def __repr__(self):
        return (f'Bizcocho({self.ingredientes}, 'f'{self.tamano})')
    def area(self):
        return self.tamano_area(self.tamano)
    
    @staticmethod
    def tamano_area(A):
        return A * 2 * math.pi
    
nuevo_bizcocho = Bizcocho(['harina','azucar','leche','fresa','zanahoria','crema'],4)

print(nuevo_bizcocho.tamano_area(12))
print(nuevo_bizcocho.ingredientes)