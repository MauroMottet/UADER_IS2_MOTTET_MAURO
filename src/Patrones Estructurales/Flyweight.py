# Situación: caracteres en un editor de texto (muchos repetidos)
class Caracter:
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def mostrar(self, contexto):
        print(f"{self.simbolo} en posición {contexto}")

class FabricaCaracteres:
    _caracteres = {}

    def obtener(self, simbolo):
        if simbolo not in self._caracteres:
            self._caracteres[simbolo] = Caracter(simbolo)
        return self._caracteres[simbolo]

# Uso
fabrica = FabricaCaracteres()
texto = "abracadabra"

for i, c in enumerate(texto):
    char = fabrica.obtener(c)
    char.mostrar(i)