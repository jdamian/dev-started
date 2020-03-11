class Instrumento:
    def __init__(self, precio):
        super().__init__()
        self.precio = precio
    
    def tocar(self):
        print("Estamos tocando musica")

    def romper(self):
        print("Esto lo pagas tu")
        print("Son "+self.precio+" $$$")

class Bateria(Instrumento):
    pass

class Guitarra(Instrumento):
    pass