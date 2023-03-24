

class Animal:
    def __init__(self, especie, ):
        self.especie = especie
    def esanimal(self):
        print("Soy un",  type(self).__name__, ",un Animal tipo", self.especie)

class Mamifero(Animal):
    pass

class Oviparo(Animal):
    pass

class Pollo(Oviparo):
    pass

class Ornitorrinco(Mamifero, Oviparo):
    pass

class Gato(Mamifero):
    pass

esgato = Gato('mamífero')
esgato.esanimal()

#gato hereda de mamifero que a su vez hereda de animal



#Animal
#Mamífero
#Ovíparo
#Pollo
#Gato
#Ornitorrinco
