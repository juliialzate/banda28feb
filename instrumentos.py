class Instrumento:
    
    def afinar(self):
        pass 

    def tocar(self):
        pass 

class Guitarra(Instrumento):

    def afinar (self):
        print("Afinano guitarra")

    def tocar (self):
        print("Tocando guitarra")

class Guacharaca(Instrumento):

    def afinar (self):
        print("Afinano guacharaca")

    def tocar (self):
        print("Tocando  guacharaca")

class Tambor(Instrumento):

    def afinar (self):
        print("Afinano tambor")

    def tocar (self):
        print("Tocando tambor")
        