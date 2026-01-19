import glob

# Contador de archivos Python:
# Crea un script que encuentre todos los archivos .py en tu carpeta actual y muestre cuántos hay en total.
def contador_archivos_python():
  lista_archivos_python = glob.glob('*.py')
  contador_archivos= 0
  for i in lista_archivos_python:
    contador_archivos+=1
  print(f"La cantidad de archivos de python son {contador_archivos}")

contador_archivos_python()