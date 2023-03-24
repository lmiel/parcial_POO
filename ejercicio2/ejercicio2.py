
class Animal:
    def __init__(self, especie):
        self.especie = especie


class Mamifero(Animal):
    def _init_(self,name):
        Animal._init_(self,name)
    pass

class Oviparo(Animal):
    def _init_(self,name):
        Animal._init_(self,name)    
    pass

class Pollo(Oviparo):
    def _init_(self,name):
        Oviparo._init_(self,name)
    pass

class Ornitorrinco(Mamifero, Oviparo):
    def _init_(self,name):
        Mamifero._init_(self,name)
        Oviparo._init_(self,name)
    pass

class Gato(Mamifero):
    def _init_(self,name):
        Mamifero._init_(self,name)
    pass


#gato hereda de mamifero que a su vez hereda de animal



#Animal
#Mamífero
#Ovíparo
#Pollo
#Gato
#Ornitorrinco
