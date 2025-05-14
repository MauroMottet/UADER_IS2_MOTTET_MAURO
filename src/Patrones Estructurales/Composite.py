class Componente:
    def mostrar(self, nivel=0):
        pass

class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Pieza: {self.nombre}")

class SubConjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"SubConjunto: {self.nombre}")
        for c in self.componentes:
            c.mostrar(nivel + 1)

# Construcción
producto = SubConjunto("Producto Principal")
for i in range(1, 4):
    sub = SubConjunto(f"SubConjunto {i}")
    for j in range(1, 5):
        sub.agregar(Pieza(f"Pieza {i}.{j}"))
    producto.agregar(sub)

# Subconjunto opcional
sub_opcional = SubConjunto("SubConjunto Opcional")
for k in range(1, 5):
    sub_opcional.agregar(Pieza(f"Pieza opcional {k}"))
producto.agregar(sub_opcional)

producto.mostrar()