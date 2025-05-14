class Numero:
    def __init__(self, valor):
        self.valor = valor

    def operar(self):
        return self.valor

class OperadorDecorator(Numero):
    def __init__(self, numero):
        self.numero = numero

class Sumar2(OperadorDecorator):
    def operar(self):
        return self.numero.operar() + 2

class Multiplicar2(OperadorDecorator):
    def operar(self):
        return self.numero.operar() * 2

class Dividir3(OperadorDecorator):
    def operar(self):
        return self.numero.operar() / 3

# Ejemplo
n = Numero(9)
print("Original:", n.operar())
print("Sumar 2:", Sumar2(n).operar())
print("Multiplicar por 2:", Multiplicar2(n).operar())
print("Dividir por 3:", Dividir3(n).operar())

# Encadenamiento
combinado = Dividir3(Multiplicar2(Sumar2(n)))
print("Combinado (Sumar2 -> Multiplicar2 -> Dividir3):", combinado.operar())