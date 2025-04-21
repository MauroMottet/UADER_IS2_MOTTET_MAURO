from Avion import   Avion , AvionBuilder , AvionComercialBuilder , Director 
from Boton import Ventana , Boton , BotonWindows , VentanaWindows , GUIFactory , WindowsFactory
from CalculadoraImpuestos import  CalculadoraImpuestos
from Prototype import Prototipo , Documento
from Hamburguesa import Hamburguesa , Mostrador , RetiroCliente , Delivery , HamburguesaFactory
from Factura import Factura , FacturaExento , FacturaFactory , FacturaNoInscripto , FacturaResponsable
from FactorialSingleton import FactorialSingleton 
# PRUEBA DE CLASES DE PATRONES DE CREACIÓN

# 1. Singleton - Factorial
fact = FactorialSingleton()
print("Factorial de 5:", fact.calcular_factorial(5))

# 2. Singleton - Cálculo de impuestos
calc = CalculadoraImpuestos()
print("Total con impuestos sobre $1000:", calc.calcular_total(1000))

# 3. Factory Method - Hamburguesa
h1 = HamburguesaFactory.crear("mostrador")
h2 = HamburguesaFactory.crear("retiro")
h3 = HamburguesaFactory.crear("delivery")
h1.entregar()
h2.entregar()
h3.entregar()

# 4. Factory Method - Factura
f1 = FacturaFactory.crear_factura("responsable", 1500)
f2 = FacturaFactory.crear_factura("no inscripto", 2000)
f3 = FacturaFactory.crear_factura("exento", 2500)
f1.imprimir()
f2.imprimir()
f3.imprimir()

# 5. Builder - Avión
builder = AvionComercialBuilder()
director = Director(builder)
director.construir_avion()
avion = director.obtener_avion()
avion.mostrar()

# 6. Prototype - Documento
doc_original = Documento("Este es el documento original.")
doc_copia = doc_original.clonar()
doc_original.mostrar()
doc_copia.mostrar()

# 7. Abstract Factory - GUI
fabrica = WindowsFactory()
boton = fabrica.crear_boton()
ventana = fabrica.crear_ventana()
boton.dibujar()
ventana.abrir()