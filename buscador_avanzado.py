import os
import glob

# Buscador avanzado de archivos:
# Crea un script que permita al usuario buscar archivos usando patrones complejos 
# (por ejemplo, todos los archivos que empiecen con "reporte" y terminen en .pdf o .docx) en una carpeta 
# y sus subcarpetas, mostrando el tamaño de cada archivo encontrado.


def buscador_avanzado():
  empieza = input("Dime como empiezan los archivos que buscas: \n")
  termina = input("Dime como terminan los archivos que buscas: \n")

  ruta = input("Coloca la ruta de busqueda: \n").strip('"')
  patron = os.path.join(ruta, f"{empieza}*{termina}")

  lista_archivos = glob.glob(patron, recursive=True)

  if not lista_archivos:
      print("No se encontraron archivos que coincidan.")
  else:
      print(f"\nSe encontraron {len(lista_archivos)} archivos:")
      for i in lista_archivos:
          print(os.path.getsize(i))
          print(os.path.basename(i))

buscador_avanzado()