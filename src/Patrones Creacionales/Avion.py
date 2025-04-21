class Avion:
    def __init__(self):
        self.body = None
        self.turbinas = None
        self.alas = None
        self.tren_aterrizaje = None

    def mostrar(self):
        print(f"Avión con: {self.body}, {self.turbinas}, {self.alas}, {self.tren_aterrizaje}")

class AvionBuilder:
    def construir_body(self): pass
    def construir_turbinas(self): pass
    def construir_alas(self): pass
    def construir_tren(self): pass
    def obtener_avion(self): pass

class AvionComercialBuilder(AvionBuilder):
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        self.avion.body = "Fuselaje comercial"

    def construir_turbinas(self):
        self.avion.turbinas = "2 turbinas comerciales"

    def construir_alas(self):
        self.avion.alas = "2 alas grandes"

    def construir_tren(self):
        self.avion.tren_aterrizaje = "Tren reforzado"

    def obtener_avion(self):
        return self.avion

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_avion(self):
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren()

    def obtener_avion(self):
        return self.builder.obtener_avion()