class FactorialSingleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def calcular_factorial(self, n):
        if n < 0:
            raise ValueError("El número debe ser no negativo.")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    