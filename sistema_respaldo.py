import os
import shutil
import glob
from datetime import datetime

#Sistema de respaldo completo:
#Crea un script que haga una copia completa de una carpeta de proyecto a una carpeta de respaldos,
#comprimiendo el resultado en un archivo .zip con la fecha actual en el nombre,
#y que elimine respaldos antiguos si hay más de 5.

def sistema_respaldo():
  fecha_actual = datetime.now()
  fecha_actual_formateada = fecha_actual.strftime("%Y-%m-%d_%H-%M-%S") 
  ruta = input("Ingresa la ruta de tu proyecto: ").strip('"')
  format = 'zip'
  max_respaldos = 5

  if os.path.exists(ruta):
    # Carpeta destino principal
    carpeta_destino = os.path.join(os.getcwd(), "respaldo_example_3")
    os.makedirs(carpeta_destino, exist_ok=True)
    
    # Nombre de la carpeta original
    nombre_carpeta = os.path.basename(ruta) 
    
    # Ruta completa donde se copiará
    ruta_carpeta_copiada = os.path.join(carpeta_destino, nombre_carpeta)
    
    # Copiar la carpeta completa
    shutil.copytree(ruta, ruta_carpeta_copiada, dirs_exist_ok=True)
    print(f"✅ Carpeta copiada a: {ruta_carpeta_copiada}")
    
    nombre_zip = os.path.join(carpeta_destino, f"{nombre_carpeta}_{fecha_actual_formateada}")
    shutil.make_archive(nombre_zip, format, ruta_carpeta_copiada)
    print(f"✅ ZIP creado: {nombre_zip}.{format}")
    
    print(f"✅ ZIP creado: {nombre_zip}.{format}")
    shutil.rmtree(ruta_carpeta_copiada)
    print(f"🗑️ Carpeta temporal eliminada: {ruta_carpeta_copiada}")

    patron_busqueda = os.path.join(carpeta_destino, f"{nombre_carpeta}_*.zip")
    archivos_zip = glob.glob(patron_busqueda)

    archivos_zip.sort(key=os.path.getmtime)

    if len(archivos_zip) > max_respaldos:
      archivos_a_eliminar = archivos_zip[:-max_respaldos]  # Todos excepto los últimos 5
      
      for archivo in archivos_a_eliminar:
        os.remove(archivo)
        print(f"🗑️ Respaldo antiguo eliminado: {os.path.basename(archivo)}")
      
      print(f"✅ Se mantienen los últimos {max_respaldos} respaldos")
    else:
      print(f"ℹ️ Total de respaldos: {len(archivos_zip)}")
  else:
    print("No existe la ruta especificada.")


sistema_respaldo()