class Animal:

    def __init__(self):
        self.num_ojos = 2

    def respirar(self):
        print("Inhale, exhale")

class Pez(Animal):

    def __init__(self):
        super().__init__()
        super().num_ojos = 3

    def respirar(self):
        super().respirar()
        
        print("Glu glu")
    
    #Metodo propio
    def nadar(self):
        print("Nadaremos nadaremos en el mar el mar el mar")

nemo = Pez() #1
gaviota = Animal() #2
#nemo.respirar()
gaviota.respirar()