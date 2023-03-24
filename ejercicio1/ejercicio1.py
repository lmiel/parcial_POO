#Escriba una clase que permita describir un libro y situar los valores asociados. Dar un ejemplo de uso en Python.

class libro():
    def eslibro(self):
        print("El libro de llama", self.Titulo, "y fue escrito por", self.Autor, "en", self.Ano, "y publicado por", self.Editorial)
    def __init__(self, Titulo, Autor, Editorial, Ano):
        self.Titulo = Titulo
        self.Autor = Autor
        self.Editorial = Editorial
        self.Ano = Ano

libro1 = libro("El principito", "Antoine de Saint-Exupéry", "Salamandra", 1943)
libro2 = libro("El señor de los anillos", "J. R. R. Tolkien", "Minotauro", 1954)
libro3 = libro("El nombre del viento", "Patrick Rothfuss", "Minotauro", 2007)

#print(libro1.Titulo, libro1.Autor, libro1.Editorial, libro1.Ano)
#print(libro2.Titulo, libro2.Autor, libro2.Editorial, libro2.Ano)
#print(libro3.Titulo, libro3.Autor, libro3.Editorial, libro3.Ano)

libro1.eslibro()
libro2.eslibro()
libro3.eslibro()


