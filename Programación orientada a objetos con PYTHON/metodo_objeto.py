# metodos
class Ropa:
    def __init__(self):
        self.marca = 'willow'
        self.talla = 'M'
        self.color = 'rojo'

camisa = Ropa()
print(camisa.talla)

#
class Calculadora:
    def __init__(self,n1,n2): # Iniciador
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 % n2
        self.division = n1 / n2

operacion = Calculadora(2,3)
print(operacion.suma)