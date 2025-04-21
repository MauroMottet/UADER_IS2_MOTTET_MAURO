class Factura:
    def __init__(self, importe):
        self.importe = importe

    def imprimir(self):
        raise NotImplementedError()

class FacturaResponsable(Factura):
    def imprimir(self):
        print(f"Factura A (IVA Responsable) - Importe: {self.importe}")

class FacturaNoInscripto(Factura):
    def imprimir(self):
        print(f"Factura C (IVA No Inscripto) - Importe: {self.importe}")

class FacturaExento(Factura):
    def imprimir(self):
        print(f"Factura E (IVA Exento) - Importe: {self.importe}")

class FacturaFactory:
    @staticmethod
    def crear_factura(condicion, importe):
        if condicion.lower() == "responsable":
            return FacturaResponsable(importe)
        elif condicion.lower() == "no inscripto":
            return FacturaNoInscripto(importe)
        elif condicion.lower() == "exento":
            return FacturaExento(importe)
        else:
            raise ValueError("Condición no válida")