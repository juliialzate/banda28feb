from musicos import *
from random import choice, randint

class Banda: 

    def __init__(self):
        self.musicos = []
        self.instrumentos = [Guitarra(), Guacharaca(), Tambor()]
        self.amigos = ["juan", "miguel", "maria", "ana", "juana", "pedro"]

    def crear_banda(self, cantidad_musicos):
        for i in range(cantidad_musicos):
            self.musicos.append(Musico(choice(self.amigos)))
            self.musicos[-1].asignar_instrumento(choice(self.instrumentos))
    
    def mostrar_banda(self):
        for m in self.musicos:
            print(m.nombre)
            print(m.nombre)
            print(type(m.instrumento))

if __name__ == "__main__":
    b = Banda()
    b.crear_banda(3)
    b.mostrar_banda()