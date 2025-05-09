# herencia multiple

class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print('llamando...')
    def ocupado(self):
        print('ocupado...')

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print('tomando foto...')

class Reproduccion:
    def __init__(self):
        pass
    def reproducciondemusica(self):
        print('reproduciendo musica')
    def reproducirvideo(self):
        print('reproducir video')

class Smartphone(Telefono,Camara,Reproduccion):
    def __del__(self):
        print('telefono apagado')

movil = Smartphone()
print(movil.fotografia())