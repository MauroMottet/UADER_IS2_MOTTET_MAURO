# TP8 - Ingeniería Reversa, Re-factoría y Re-Ingeniería

## 👨‍💻 Materia
Ingeniería de Software II – UADER – FCyT

## 👤 Autor
**Mauro Mottet**

## 📝 Descripción

Este trabajo práctico tiene como objetivo aplicar conceptos de ingeniería de software avanzada, específicamente **ingeniería reversa**, **refactorización** y **reingeniería**, utilizando un programa base (`getJason.py`) y mejorándolo con:

- **Automatización del proceso de pagos**
- **Selección automática de cuenta bancaria**
- Implementación de los patrones de diseño:
  - Singleton
  - Chain of Responsibility (Cadena de Responsabilidad)
  - Iterator (Iterador)

## 🚀 Funcionalidad

El sistema simula la gestión automática de pagos bancarios. Se manejan dos cuentas (`token1`, `token2`) con saldos iniciales predefinidos.

Cada vez que se solicita un pago:

- Se elige automáticamente una cuenta con saldo suficiente.
- Se alterna entre cuentas para mantener balance.
- Se registra cada transacción con número de pedido, token usado, clave asociada y timestamp.
- Se lista el historial cronológico de pagos.

Si ninguna cuenta tiene saldo suficiente, el sistema **rechaza el pago** sin producir errores.



