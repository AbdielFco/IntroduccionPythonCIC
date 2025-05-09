# Clase - Contenedor que almacena propiedades de un objeto
# CLASS = Nombre de la clase.
# DEF = Nombre del metodo.
# SELF = Ejecutar un metodo.
# __init__ = Iniciador.

class Auto: # Clase
    marca = "" # Atributos
    modelo = 0
    placa = ""

taxi = Auto() # Objeto
print(taxi.modelo)

# Clase 2

class Persona:
    doctor = 'Victor'

print(Persona.doctor)

#
class Jugadores:
    j1= 'messi'
    j2= 'c.ronaldo'

print(Jugadores.j2)

#
class nombre:
    pass

victor = nombre()
maria = nombre()

victor.edad = 30
victor.sexo = 'masculino'
victor.pais = 'bolivia'

maria.edad = 25
maria.sexo = 'femenino'
maria.pais = 'colombia'

print(victor.edad, maria.edad)



