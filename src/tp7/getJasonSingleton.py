#!/usr/bin/env python3
"""
getJason.py - Programa para extraer el valor de 'token1' de un archivo JSON
Copyright UADERFCyT-IS2©2024 todos los derechos reservados

Este programa implementa una clase Singleton para manejo del archivo JSON,
valida los parámetros y controla errores de forma robusta.
"""

import json
import sys
import os


class GetJasonSingleton:
    """Singleton para manejar la extracción del token del archivo JSON."""

    _instance = None
    VERSION = "1.1"
    JSON_KEY = 'token1'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GetJasonSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def ejecutar(self, args):
        """Ejecuta la lógica principal con validación robusta."""
        if len(args) == 1:
            self._mostrar_uso()
            return 1

        # Mostrar versión si el argumento es -v
        if len(args) == 2 and args[1] == '-v':
            print(f"getJason versión {self.VERSION}")
            return 0

        # Validar número de argumentos correcto (programa + archivo)
        if len(args) != 2:
            print("Error: Número incorrecto de argumentos.")
            self._mostrar_uso()
            return 1

        jsonfile = args[1]

        # Validar que el archivo existe
        if not os.path.isfile(jsonfile):
            print(f"Error: El archivo '{jsonfile}' no existe.")
            return 1

        # Leer y procesar el archivo JSON
        try:
            with open(jsonfile, 'r') as f:
                data = f.read()
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return 1

        try:
            obj = json.loads(data)
        except json.JSONDecodeError as e:
            print(f"Error al parsear JSON: {e}")
            return 1

        # Extraer el valor para JSON_KEY
        if self.JSON_KEY not in obj:
            print(f"Error: La clave '{self.JSON_KEY}' no está en el archivo JSON.")
            return 1

        print(str(obj[self.JSON_KEY]))
        return 0

    def _mostrar_uso(self):
        print("Uso:")
        print("  getJason.py <archivo_json>")
        print("  getJason.py -v  # muestra la versión")


def main():
    programa = GetJasonSingleton()
    exit_code = programa.ejecutar(sys.argv)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
