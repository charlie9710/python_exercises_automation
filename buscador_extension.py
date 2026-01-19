

import os 
# Buscador de archivos por extensión:
# Desarrolla un script que recorra un directorio y todos sus subdirectorios,
# y genere un reporte mostrando cuántos archivos hay de cada tipo (.txt, .py, .jpg, etc.) y sus rutas completas.
def buscador_extension():
  ruta_base = os.getcwd()
  diccionario = {}
  for ruta_actual, directorios, archivos in os.walk(ruta_base):
    for i in archivos:
      print(f"El archivo {i} esta en la ruta: {ruta_actual + '/' + i}")
      raiz,extension = os.path.splitext(i)
      if extension in diccionario:
        diccionario[extension]+=1

      else:
        diccionario[extension]=1
  for extension, numero in diccionario.items():
    print(f"La extension {extension} tiene {numero} elementos")

buscador_extension()