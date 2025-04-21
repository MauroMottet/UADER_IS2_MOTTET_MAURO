import copy

class Prototipo:
    def clonar(self):
        return copy.deepcopy(self)

class Documento(Prototipo):
    def __init__(self, contenido):
        self.contenido = contenido

    def mostrar(self):
        print(f"Contenido: {self.contenido}")