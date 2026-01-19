import os
# Creador de estructura de proyecto:
# Crea un programa que genere automáticamente una estructura de carpetas para un proyecto 
# (por ejemplo: proyecto/datos, proyecto/scripts, proyecto/resultados) 
# y cree un archivo README.txt vacío en la carpeta principal.
def crear_proyecto(ruta):

  try:
    carpetas = f"proyecto/{ruta}"
    os.mkdir('proyecto')
  except FileExistsError:
    print('La carpeta de proyectos ya existe.')
  
  try:
    os.mkdir(carpetas)
    print(f"Proyecto creado en la ruta proyecto/{ruta}")
  except FileExistsError:
    print('La carpeta del proyecto ya existe .')


proyecto = input('Ingresa el nombre del proyecto: ')
crear_proyecto(proyecto)