# metodo constructor
class Persona:
    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre,self.año)
    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre,frase)

doctor = Persona('JOSE',26)
print(doctor.descripcion())
print(doctor.comentario("Hola que tal"))