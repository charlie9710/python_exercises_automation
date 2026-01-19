import os

#Script para obtener variables de entorno

resultado = os.environ

for value in resultado:
  print(f"La variable es {value} y su valor es {resultado[value]}")