# python_test

1. Crear un módulo en Python que se llame ApiCommons, el cual en un principio solo tenga un método que se llame fetch_value. El método deberá iterar sobre una lista de diccionarios que tengan como llaves los nombre key y value, para encontrar el value correspondiente al name que se le pasa como input. Ejemplo:

 

 

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

 
2. En base a la programación orientada a objetos deberás crear un pequeño conector para una API, para ello, deberás utilizar una clase padre llamada "LastMile API" que contenga todos los elementos básicos para comunicarte con la API, y adicionalmente, tendrás que crear dos clases relacionadas, una que se llame Route y la otra que se llame Guide que contenga los siguientes métodos de la API: 

Route:

    Create Route
    Update Route
    Show Route


Dispatch:

    Create Dispatch
    Show Dispatch

Documentación API: LastMile API
**Para el token utiliza un token representativo "api_token"
