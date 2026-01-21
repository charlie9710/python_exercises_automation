import os
import shutil

#Organizador de descargas:
#Desarrolla un programa que mueva archivos de tu carpeta de descargas a carpetas
#organizadas por tipo (Documentos, Imágenes, Videos, Otros) según su extensión.

def organizador_descargas():
  ruta_descargas = input("Ingresa tu ruta de descargas").strip('"')
  ruta_descargas_copy= r'C:\Users\carfe\OneDrive\Desktop\pythonLearning\descargas'
  if(os.path.exists(ruta_descargas)):
    os.chdir(ruta_descargas)
    lista_archivos = os.listdir()
    for i in lista_archivos:
      ruta_original = os.path.join(ruta_descargas, i)
      if os.path.isdir(ruta_original):
                continue
      raiz,extension = os.path.splitext(i)

      if extension in ['.jpg', '.jpeg', '.png', '.gif']:
        copy_files("imagenes",ruta_descargas_copy,ruta_descargas,i)
      elif extension in ['.mp4', '.mkv', '.mov', '.avi']:
          copy_files("videos",ruta_descargas_copy,ruta_descargas,i)
      elif extension in ['.pdf', '.docx', '.txt', '.xlsx']:
          copy_files("documentos",ruta_descargas_copy,ruta_descargas,i)
      else:
          copy_files("otros",ruta_descargas_copy,ruta_descargas,i)
  else:
    print("La ruta no existe")


def copy_files(tipo,ruta_descargas_copy,ruta_descargas,i):
  if not ( os.path.exists(os.path.join(ruta_descargas_copy,tipo))):
    os.mkdir(os.path.join(ruta_descargas_copy,tipo))
  shutil.copy(os.path.join(ruta_descargas,i),os.path.join(ruta_descargas_copy,tipo))
   
organizador_descargas()
