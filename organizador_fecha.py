import glob
import os

# Organizador por fecha:
# Haz un programa que busque todos los archivos de imagen (*.jpg, *.png, *.gif) en una carpeta y
# los liste ordenados por fecha de modificación.
def organizador_fecha():
  ruta = r'C:\Users\carfe\OneDrive\Desktop\Fondos\*'
  todos_los_archivos = glob.glob(ruta)

  extensiones_validas = ('.jpg', '.png', '.gif', '.jpeg')
  lista_archivos = [f for f in todos_los_archivos if f.lower().endswith(extensiones_validas)]
  lista_ordenada = sorted ( lista_archivos, key= os.path.getmtime)
  print("La lista ordenada por fecha de modificacion es: \n")
  for i in lista_ordenada:
    print(f"{os.path.basename(i)} \n")

organizador_fecha()