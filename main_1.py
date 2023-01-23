"""
1. Crear un módulo en Python que se llame ApiCommons,
el cual en un principio solo tenga un método que se llame fetch_value.
El método deberá iterar sobre una lista de diccionarios que tengan como
llaves los nombre key y value, para encontrar el value correspondiente
al name que se le pasa como input. Ejemplo:

arr = [
  {
    "name": "Guia",
    "value": "1234"
  },
  {
    "name": "Orden de Compra",
    "value": "88331"
  },
  {
    "name": "Boleto",
    "value": "321"
  }
]

fetch_value(arr, "Boleto") debería retornar "321".
"""

class ApiCommons:
    def fetch_value(self, lst, name):
        name = name
        list = lst

        for dict in list:
            if dict[name]:
                return dict["value"]
            else:
                return "Error"


