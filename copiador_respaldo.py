import shutil
import os
from datetime import datetime

# Copiador de respaldo:
# Crea un script que copie un archivo específico a una carpeta de respaldos,
#  agregando la fecha actual al nombre del archivo copiado.

def copiador_respaldo():
  archivo_mover = input("Ingresa un archivo para mover de la ruta actual: ")
  ruta_origen = os.path.join(os.getcwd(),archivo_mover)
  ruta_destino = os.path.join(os.getcwd(),'respaldo')

  if os.path.exists(ruta_origen):
    ahora = datetime.now()
    fecha_formateada= ahora.strftime("%Y-%m-%d")
    raiz, extension = os.path.splitext(archivo_mover)
    os.rename(archivo_mover,f"{raiz}_{fecha_formateada}{extension}")
    ruta_origen = os.path.join(os.getcwd(),f"{raiz}_{fecha_formateada}{extension}")
    shutil.move(ruta_origen,ruta_destino)
    print(f"Archivo {archivo_mover} se movio con exito")
  else:
    print("El archivo no existe.")

copiador_respaldo()