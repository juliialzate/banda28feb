class Instrumento:
    
    def afinar(self):
        pass 

    def tocar(self):
        pass 

    def mostrar(self):
        return "instrumento: " + (str(type(self)).split(".")[-1][:-2])

class Guitarra(Instrumento):

    def afinar (self):
        return "Afinano guitarra"

    def tocar (self):
        return "Tocando guitarra"

class Guacharaca(Instrumento):

    def afinar (self):
        return "Afinano guacharaca"

    def tocar (self):
        return "Tocando  guacharaca"

class Tambor(Instrumento):

    def afinar (self):
        return "Afinano tambor"

    def tocar (self):
        return "Tocando tambor"

class Flauta(Instrumento):

    def afinar (self):
        return "Afinano flauta"

    def tocar (self):
        return "Tocando flauta"

class Ukelele(Instrumento):

    def afinar (self):
        return "Afinano Ukelele"

    def tocar (self):
        return "Tocando Ukelele"

class Bajo(Instrumento):

    def afinar (self):
        return "Afinano bajo"

    def tocar (self):
        return "Tocando bajo"
        
class Saxo(Instrumento):

    def afinar (self):
        return "Afinano saxo"

    def tocar (self):
        return "Tocando saxo"

class Bateria(Instrumento):

    def afinar (self):
        return "Afinano bateria"

    def tocar (self):
        return "Tocando bateria"

class Arpa(Instrumento):

    def afinar (self):
        return "Afinano arpa"

    def tocar (self):
        return "Tocando arpa"
class Acordeon(Instrumento):

    def afinar (self):
        return "Afinano acordeon"

    def tocar (self):
        return "Tocando acordeon"
        