class TrenLaminador:
    def producir(self):
        pass

class Tren5mts(TrenLaminador):
    def producir(self):
        return "Producida lámina de 5 mts"

class Tren10mts(TrenLaminador):
    def producir(self):
        return "Producida lámina de 10 mts"

class Lamina:
    def __init__(self, tren: TrenLaminador):
        self.tren = tren

    def producir(self):
        return self.tren.producir()