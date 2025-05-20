class Observer:
    def __init__(self, id):
        self.id = id

    def update(self, id):
        if self.id == id:
            print(f"ID {id} coincide con el de {self.__class__.__name__}")

class ObserverA(Observer):
    pass

class ObserverB(Observer):
    pass

class ObserverC(Observer):
    pass

class ObserverD(Observer):
    pass

# Test
observers = [ObserverA("ABCD"), ObserverB("EFGH"), ObserverC("IJKL"), ObserverD("MNOP")]

ids = ["ABCD", "EFGH", "IJKL", "MNOP", "XYZZ", "EFGH", "ABCD", "MNOP"]

for id in ids:
    for observer in observers:
        observer.update(id)