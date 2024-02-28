import random

class Instrumentos:
    def __init__(self):
        self.conjunto = ['guitarra','ukelele','tambor','guacharaca','arpa','maracas','bajo','acordeaon','Requinto','Gaita',]


    def afinar(self):
        pass
        
    
    def tocar(self):
        pass
    

class Musicos(Instrumentos):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def afinar(self,):
        for i in range (10):
            i_aleatorio = random.choice(self.conjunto)
            print ("El musico", self.nombre,"esta afinando su", i_aleatorio)

class BandaZawer (Musicos, Instrumentos):
    def __init__(self, nombre, banda):
       # Instrumentos.__init__(self,conjunto)
        Musicos.__init__(self, nombre)
        self.nombre = nombre
        self.banda = banda


banda1 = BandaZawer ("Juan", "Guns n roses")
banda1.afinar()
