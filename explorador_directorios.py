import os
# Explorador de directorios:
# Crea un script que liste todos los archivos y carpetas en tu directorio actual,
# indicando cuáles son archivos y cuáles son carpetas.
def explorar_directorio():
  ruta_actual= os.getcwd()

  lista_archivos = os.listdir()
  for i in lista_archivos:
    ruta_completa = os.path.join(ruta_actual, i)
    if os.path.isdir(ruta_completa):
      print(f"{i} es un directorio")
    else:
      print(f"{i} es un archivo")


explorar_directorio()