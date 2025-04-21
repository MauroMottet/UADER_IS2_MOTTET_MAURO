class Hamburguesa:
    def entregar(self):
        raise NotImplementedError()

class Mostrador(Hamburguesa):
    def entregar(self):
        print("Entregada en mostrador.")

class RetiroCliente(Hamburguesa):
    def entregar(self):
        print("Retirada por el cliente.")

class Delivery(Hamburguesa):
    def entregar(self):
        print("Enviada por delivery.")

class HamburguesaFactory:
    @staticmethod
    def crear(tipo):
        if tipo == "mostrador":
            return Mostrador()
        elif tipo == "retiro":
            return RetiroCliente()
        elif tipo == "delivery":
            return Delivery()
        else:
            raise ValueError("Tipo no válido")