class Boton:
    def dibujar(self):
        raise NotImplementedError()

class Ventana:
    def abrir(self):
        raise NotImplementedError()

# Implementaciones Windows
class BotonWindows(Boton):
    def dibujar(self):
        print("Botón estilo Windows")

class VentanaWindows(Ventana):
    def abrir(self):
        print("Ventana estilo Windows")

# Abstract Factory
class GUIFactory:
    def crear_boton(self): pass
    def crear_ventana(self): pass

class WindowsFactory(GUIFactory):
    def crear_boton(self):
        return BotonWindows()

    def crear_ventana(self):
        return VentanaWindows()