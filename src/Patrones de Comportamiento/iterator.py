class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def forward(self):
        if self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
            return char
        return None

    def backward(self):
        if self.index > 0:
            self.index -= 1
            return self.string[self.index]
        return None

# Test
iterator = StringIterator("Hola Mundo")

# Recorrer en dirección normal
print("Dirección normal:")
char = iterator.forward()
while char:
    print(char, end=" ")
    char = iterator.forward()

# Recorrer en dirección inversa
print("\nDirección inversa:")
char = iterator.backward()
while char:
    print(char, end=" ")
    char = iterator.backward()