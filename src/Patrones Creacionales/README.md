# TP3 - Patrones de Creación (Python)

Este proyecto contiene la implementación en Python de los distintos **patrones de diseño creacionales** solicitados en el Trabajo Práctico 3 de la materia **Ingeniería de Software II**.

## Estructura del Proyecto

- `singleton.py`: Implementa el patrón Singleton aplicado al cálculo de factorial y al cálculo de impuestos.
- `factory.py`: Contiene dos ejemplos del patrón Factory Method:
  - Entrega de hamburguesas (mostrador, retiro o delivery).
  - Generación de facturas según condición impositiva del cliente.
- `builder.py`: Implementa el patrón Builder para construir un objeto `Avion` paso a paso.
- `prototype.py`: Contiene una clase que implementa el patrón Prototype con capacidad de clonación.
- `abstract_factory.py`: Ejemplo del patrón Abstract Factory para interfaces gráficas (botón y ventana estilo Windows).
- `main.py`: Script de prueba que instancia y utiliza todas las clases implementadas.

## Cómo usar

1. Asegurate de tener Python 3 instalado.
2. Ejecutá el archivo `Pruebas.py` para ver ejemplos de uso de cada patrón.

```bash
python Pruebas.py