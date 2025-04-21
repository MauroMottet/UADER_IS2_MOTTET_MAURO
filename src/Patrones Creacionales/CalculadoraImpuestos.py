class CalculadoraImpuestos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def calcular_total(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012
        return base_imponible + iva + iibb + contribuciones